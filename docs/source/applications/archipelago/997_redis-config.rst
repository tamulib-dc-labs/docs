Redis Cache Configuration Change
=================================

.. note::

   This document explains the changes made to ``settings.php`` as part of
   the investigation into Redis (``archipelago`` namespace) running at its
   memory ceiling and evicting cache entries -- including expensive IIIF
   manifests for large creative-work-series objects -- well before any
   reasonable TTL.

Background
----------

Redis in the ``archipelago`` namespace was found running continuously at
its configured memory ceiling, evicting cache entries under
``allkeys-lru`` eviction rather than expiring them on a normal TTL
schedule. This was originally misdiagnosed as "cache busting after ~30
minutes," but investigation showed it was pure LRU eviction under memory
pressure, unrelated to expiration.

Initial evidence (captured 2026-08-26, production
``redis-595986b5b6-hpkbh``)::

    used_memory: 1023.99M
    maxmemory: 1.00G          # container pinned at its configured ceiling
    maxmemory_policy: allkeys-lru
    evicted_keys: 2,754,491   # lifetime evictions
    expired_keys: 0           # confirms this is NOT TTL-driven
    keyspace_hits: 37,865,703
    keyspace_misses: 10,064,972   # ~21% miss rate

``expired_keys: 0`` ruled out expiration as the cause -- every loss was a
forced eviction from ``allkeys-lru``, which discards keys once memory is
full regardless of how expensive they were to regenerate.

Investigation Summary
----------------------

Several avenues were tested in sequence before arriving at the
``settings.php`` change documented here.

Raising ``maxmemory`` (partial fix)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``-maxmemory`` on the ``redis`` deployment was raised from ``1024mb`` to
``1300mb``, staying under the pod's ``1536Mi`` resource limit. This is a
low-risk, config-only change with no application code impact.

Result after several days at steady state: ``used_memory`` remained
pinned within 1MB of the new ``1300mb`` ceiling, and eviction continued
at a sustained rate of roughly **64 evictions/minute (~92,000/day)** over
a 3.1-day observation window. The miss rate improved modestly, from
~21% to ~17%, but the underlying problem was not resolved -- the working
set simply grew to fill the larger ceiling, the same pattern as before.

**Conclusion:** raising ``maxmemory`` alone is not sufficient. The
working set genuinely exceeds the available memory under normal
production traffic.

TTL audit and eviction policy (``allkeys-lru`` vs. ``volatile-lru``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A full census of the live keyspace (198,225 of 198,176 keys -- effectively
100% coverage) was taken to determine whether switching
``maxmemory-policy`` from ``allkeys-lru`` to ``volatile-lru`` would
meaningfully protect expensive manifest-related cache bins.

Findings:

* Virtually every key in every cache bin (99.9%+) carries a TTL of
  approximately 360-365 days. This is not a real expiration policy --
  it is the Redis module's technical "permanent cache" convention,
  which gives ``CACHE_PERMANENT`` items a long safety-net TTL rather
  than true infinite expiry.
* Because this ~1-year TTL is applied nearly uniformly across *all*
  bins -- including manifest-adjacent bins (``page``, ``data``,
  ``dynamic_page_cache``, ``render``) and cheap, high-churn bins
  (``entity``, ``default``) alike -- TTL does not differentiate
  "expensive to regenerate" from "cheap to regenerate" data in this
  dataset.
* A handful of true no-TTL keys exist (7-8 keys total, out of ~198,000),
  but they are negligible in size and pose no meaningful OOM risk under
  ``volatile-lru``.

**Conclusion:** switching to ``volatile-lru`` would be *safe* but would
not provide the targeted protection originally hoped for, since manifest
keys are not distinguishable from cheap keys by TTL. The eviction policy
was not pursued further as the primary fix; ``allkeys-lru`` was retained.

``settings.php`` cache bin configuration (this change)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the memory-ceiling and eviction-policy avenues explored, attention
turned to ``settings.php`` itself, where the site's Redis configuration
was compared against the Redis module's current recommended setup
(module version 1.11.0, ``example.settings.php`` /
``example.services.yml``).

Root Cause
----------

Two categories of gaps were found between the site's Redis configuration
and the module's current recommended pattern.

1. Legacy bootstrap cache bin routing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The site was forcing four early-boot cache bins to the database backend
instead of Redis::

    $settings['cache']['bins']['bootstrap']  = 'cache.backend.database';
    $settings['cache']['bins']['config']     = 'cache.backend.database';
    $settings['cache']['bins']['container']  = 'cache.backend.database';
    $settings['cache']['bins']['discovery']  = 'cache.backend.database';

This is the *pre-1.11.0* conservative pattern. It exists historically
because the ``container`` bin caches the built dependency-injection
container itself -- Drupal cannot ask the not-yet-built container for a
Redis cache service to cache itself with, so early Redis module versions
simply routed all four early-boot bins to the database as a safe
fallback.

No ``$settings['bootstrap_container_definition']`` (the mechanism that
solves this bootstrapping problem) was present anywhere in
``settings.php``, and no site-specific ``services.yml`` existed to
provide an alternative route to the same result.

**Impact:** ``bootstrap``, ``config``, and ``discovery`` caches are read
on essentially every request, very early in the page lifecycle. Routing
them to MySQL instead of an in-memory Redis lookup is a small but
constant per-request performance cost, independent of the eviction
issue.

2. Missing memory-relevant Redis module settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comparing against the module's shipped example configuration surfaced
two settings that bear directly on the memory-pressure problem driving
this investigation, neither of which was set:

``redis_compress_length``
    Compresses cache entries larger than a configured byte threshold
    before storing them in Redis. Without this set, large cache entries
    -- and IIIF manifests for creative-work-series objects are exactly
    the kind of entry this affects -- are stored uncompressed, consuming
    more of the available ``maxmemory`` ceiling than necessary.

``redis_invalidate_all_as_delete``
    Changes cache-tag invalidation behavior so that invalidated entries
    are actually deleted from Redis rather than left in memory as stale,
    unusable data until naturally overwritten or evicted. Without this
    set, invalidated-but-undeleted cache data may have been consuming
    real memory for no benefit, causing the ``maxmemory`` ceiling to be
    reached sooner than the live working set alone would require.

A third setting, ``redis_ttl_offset``, staggers actual cache expiration
to avoid a "thundering herd" of simultaneous regeneration when many
entries share a nominal TTL. This is a performance/stability nicety
rather than a direct contributor to the memory-pressure problem.

The Change
----------

The following was added to ``settings.php``, and the four
database-backend cache bin overrides were commented out (not deleted,
to allow a fast one-line revert if needed):

.. code-block:: php

    $settings['redis.connection']['interface'] = 'PhpRedis';
    $settings['redis.connection']['host']      = 'redis';
    $settings['redis.connection']['port']      = 6379;
    $settings['cache']['default'] = 'cache.backend.redis';

    // bootstrap/config/container/discovery no longer forced to the
    // database backend -- see bootstrap_container_definition below.
    // $settings['cache']['bins']['bootstrap']  = 'cache.backend.database';
    // $settings['cache']['bins']['config']     = 'cache.backend.database';
    // $settings['cache']['bins']['container']  = 'cache.backend.database';
    // $settings['cache']['bins']['discovery']  = 'cache.backend.database';

    $settings['lock']['backend_factory']     = 'redis.lock.backend.redis';
    $settings['lockSlow']['backend_factory'] = 'redis.lock.backend.redis';
    $settings['cache_prefix'] = 'archipelago_';

    $settings['redis_compress_length'] = 100;
    $settings['redis_ttl_offset'] = 3600;
    $settings['redis_invalidate_all_as_delete'] = TRUE;

    $settings['container_yamls'][] = 'modules/contrib/redis/example.services.yml';
    $settings['container_yamls'][] = 'modules/contrib/redis/redis.services.yml';

    $class_loader->addPsr4('Drupal\\redis\\', 'modules/contrib/redis/src');

    $settings['bootstrap_container_definition'] = [
      'parameters' => [],
      'services' => [
        'redis.factory' => [
          'class' => 'Drupal\redis\ClientFactory',
        ],
        'cache.backend.redis' => [
          'class' => 'Drupal\redis\Cache\CacheBackendFactory',
          'arguments' => ['@redis.factory', '@cache_tags_provider.container', '@serialization.phpserialize'],
        ],
        'cache.container' => [
          'class' => '\Drupal\redis\Cache\PhpRedis',
          'factory' => ['@cache.backend.redis', 'get'],
          'arguments' => ['container'],
        ],
        'cache_tags_provider.container' => [
          'class' => 'Drupal\redis\Cache\RedisCacheTagsChecksum',
          'arguments' => ['@redis.factory'],
        ],
        'serialization.phpserialize' => [
          'class' => 'Drupal\Component\Serialization\PhpSerialize',
        ],
      ],
    ];

Testing and Rollout
--------------------

.. warning::

   This change affects Drupal's earliest bootstrap phase. A mistake in
   ``bootstrap_container_definition`` can produce confusing failures
   (blank pages, container errors) rather than a clear error message.
   Deploy to staging first.

Before production rollout:

#. Confirm PHP syntax is valid (``php -l settings.php``).
#. Deploy to staging and verify the site loads normally, with no errors
   in the Drupal log or PHP error log related to the container or cache
   services.
#. Confirm the exact semantics of ``redis_invalidate_all_as_delete``
   against the installed Redis module version's ``README.md`` --
   documented here based on general module knowledge, not a direct
   citation of this site's module version.
#. Verify whether the ``addPsr4`` classloader line is actually necessary
   on this Composer-managed site, or already redundant with Composer's
   own autoloader (harmless either way if redundant).
#. Once stable in staging and promoted to production, re-run the same
   Redis monitoring used to evaluate the ``maxmemory`` change
   (``evicted_keys`` rate, ``used_memory`` vs. ``maxmemory``, miss rate)
   over a comparable multi-day window, to determine whether
   ``redis_compress_length`` and ``redis_invalidate_all_as_delete``
   meaningfully reduce eviction pressure.

Result (production, 2026-09-18, 30-minute monitoring window post-deploy):
``evicted_keys`` did not increase at all -- 0 evictions across the full
window, versus a sustained ~64 evictions/minute under the ``maxmemory``-only
configuration at the same 1300mb ceiling. ``used_memory`` held steady
several MB below the ceiling rather than pinned against it. Miss rate was
unchanged (~17%), as expected -- this fix targets eviction, not cache
misses. A longer (24-48 hour) monitoring window covering peak traffic is
still recommended to confirm this holds under all load conditions, but the
initial result strongly supports the diagnosis in `Root Cause`_.

Related Follow-up: Redis Persistence (Ticket Item #2)
-------------------------------------------------------

This change addresses eviction *pressure* (why Redis was full), but does
nothing to protect the cache from being wiped out entirely by a pod
restart or OOM event -- the concern behind the original ticket's item #2
(mount a PVC for persistence).

As of this writing, the ``redis`` deployment has no RDB/AOF persistence
configured to a durable volume. If the pod restarts for any reason --
scheduled restart, node maintenance, or an actual OOM kill -- the entire
cache is lost and every subsequent request, including the expensive
creative-work-series manifests this whole investigation is about, is
regenerated from scratch simultaneously. This produces the same
symptom (slow page loads, expensive manifest regeneration) as the
eviction and cron issues, just triggered by a pod event rather than
ongoing memory pressure or a scheduled cache-tag invalidation.

This was independently flagged in a community Slack discussion (Diego
Pino, Archipelago Commons, 2026-09-18/19; see References), who recommended:

* Confirming the ``redis`` deployment's memory limit and host kernel
  overcommit settings are sane, since Redis is prone to being OOM-killed
  without proper memory accounting -- worth checking pod logs and node
  events for any history of this, even though eviction (not OOM) was
  confirmed as the primary driver of the original symptom.
* Enabling periodic RDB snapshotting to a volume that survives pod
  restarts, rather than relying on an always-warm in-memory cache. A
  starting point along the lines of ``save 3600 1`` (snapshot at least
  hourly, if at least one key changed) balances snapshot overhead against
  how much regeneration work a cold start would otherwise cause.

**Recommended next step:** revisit ticket item #2 -- mount a PVC for the
``redis`` deployment and enable ``save`` directives (or AOF, if stronger
durability is wanted) pointing at it, so a pod restart no longer means
starting from a completely empty cache.

References
----------

* ``web/modules/contrib/redis/example.settings.php`` (module 1.11.0)
* ``web/modules/contrib/redis/example.services.yml``
* Production Redis pod: ``redis-595986b5b6-hpkbh`` (``archipelago``
  namespace)
* Drupal Redis module commit `ce798336
  <https://git.drupalcode.org/project/redis/-/commit/ce798336f759d75c01fa1530f68899b9f2adf2b8>`_,
  "Enable performance-enhancing settings by default" -- independent
  confirmation that ``redis_compress_length`` / ``redis_invalidate_all_as_delete``
  are the module's current recommended defaults.
* Archipelago Commons Slack, #general (Diego Pino, 2026-09-18/19) --
  community discussion of eviction policy, compression, and Redis
  persistence; referenced ``archipelago-deployment-live`` `docker-compose
  example
  <https://github.com/esmero/archipelago-deployment-live/blob/c98d4f8d65b53f1323f094400ce7961e3e17e357/deploy/ec2-docker/docker-compose-aws-s3.yml#L223>`_
  showing a ``save`` directive pattern.
