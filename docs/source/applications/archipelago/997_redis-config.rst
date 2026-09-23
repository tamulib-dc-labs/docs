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

Follow-up Investigation: Manifest-Specific Cache Behavior (2026-09)
---------------------------------------------------------------------

With eviction pressure addressed by the change above, a separate thread
looked at why *individual* manifests -- particularly large
creative-work-series objects -- still behaved differently from other
cached content: busting faster than expected, or being disproportionately
expensive relative to everything else in their bin. Several distinct,
independent mechanisms were identified; none of them require further
``settings.php`` changes on their own, but they are documented here since
they will very likely resurface in future performance investigations.

Cron-driven embargo cache tag invalidation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A specific "manifests bust cache within ~30 minutes even with no
data/twig changes" symptom was traced to source, not inferred:
``format_strawberryfield_cron()`` (``format_strawberryfield.module``)
unconditionally invalidates a ``format_strawberryfield:embargo:<today's
date>`` cache tag on *every* cron run, because its
``$dayssince = ceil($timesincerun/60/60/24)`` always rounds up to at
least 1 for any positive elapsed time under 24 hours -- so ``$i=0``
always resolves to today's date regardless of how recently cron last
ran. (The broader ``format_strawberryfield:all_embargo`` tag only fires
if cron hasn't run in over 7 days.)

This tag is only ever attached to a manifest's render dependencies by
``MetadataExposeDisplayController`` when ``EmbargoResolver::embargoInfo()``
finds that *specific object* currently has an active, future-dated
``date_embargo_lift`` value. In other words: this is **not** a blanket
"cron busts all manifests" bug. It only affects an object whose own
configured embargo happens to be lifting soon. To check whether it
applies to any given object, inspect that node's ``date_embargo_lift``
JSON value directly.

AMI ingest and genuine Redis eviction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A live ingest event was observed causing widespread cache ``MISS`` and
intermittent 5xx/curl errors for roughly an hour. A concurrent
``eviction_monitor.sh`` run confirmed **real** eviction throughout the
window (46-81 evictions/min, ``used_memory`` pinned at the ceiling),
stopping almost exactly when the ingest finished per the operator's own
timestamp -- a tight before/after correlation. Separately, Redis's own
``INFO`` polling never lagged or failed during the same window, which
argues against "Redis too resource-starved to respond" as the mechanism
behind the MISS pattern; the accompanying 5xx/curl errors are more
plausibly explained by PHP-FPM/web-tier worker exhaustion during bulk
ingest -- a different layer entirely from Redis memory pressure, and not
yet investigated (``pm.max_children``, per-worker ``memory_limit``,
``max_execution_time``, and nginx/php-fpm timeout settings are the
likely next place to look).

``maxmemory`` sizing and an open discrepancy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With resourcing explicitly not a constraint, a working recommendation of
roughly 4096mb (~3x the confirmed working set), with the pod memory
limit set to 1.5-2x that to leave headroom for Redis's own overhead and
RDB fork/copy-on-write spikes, was given as a starting point; 8GB was
separately discussed as reasonable in community correspondence (see
References).

**Open item:** a community Slack exchange (Diego Pino) referenced a
Redis instance at only ~1.3GB used memory with ``maxmemory-policy`` set
to ``volatile-lru`` -- inconsistent with both this document's confirmed
production baseline (``allkeys-lru``, deliberately retained -- see `TTL
audit and eviction policy`_) and the scale of the eviction problem
described above. It is not yet confirmed whether this figure describes
production or a staging/lower environment. Before acting further on
recommendations from that thread, confirm which environment is being
discussed, and separately confirm whether ``volatile-lru`` reflects a
durable change in the deployment YAML or a transient ``CONFIG SET`` that
would reset on pod restart.

Cache bin "pollution" and key-count vs. key-size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All cache bins under ``cache.backend.redis`` share a single flat memory
pool with a single LRU policy. A high-churn, low-value bin can crowd out
and cause premature eviction of a low-volume, high-value bin (e.g.
``render`` vs. ``page``, the latter holding expensive manifest
responses) purely through LRU recency, independent of which bin's
contents actually matter more. Drupal supports routing individual bins
to a different backend for exactly this reason::

    $settings['cache']['bins']['render'] = 'cache.backend.database';

**This has deliberately not been applied.** Per explicit caution from
the community discussion this idea originated in, the correct direction
depends on real data and could just as easily be the opposite of the
obvious guess -- this is a lever to pull only after the analysis below
(or its successors) confirms which bin, if any, is actually the
problem.

To investigate this, a small tool (``render_key_sizer.sh``, see
`Diagnostic tooling`_) was built to rank keys in a given bin by actual
Redis ``MEMORY USAGE`` rather than raw key count, since a bin can have
tens of thousands of small keys and a handful of huge ones, and a plain
``--scan`` listing shows neither.

Two concrete findings came out of using it against production:

Cache-context cardinality, not key size, drives the ``render`` bin
   Sampling all 13 cache entries belonging to a single node (59022)
   showed a normal-sized set (1.1-6.2 KB each, ~2.9 KB average) --
   but the same node produced 13 separate entries purely from cache
   *context* permutations: different view modes, permission-hash
   variants (anonymous / admin / specific role hash), referring pages,
   and -- notably -- one entry keyed on a full AJAX search request URL
   including the free-text search term itself
   (``search_api_fulltext=...``). Because Drupal's render cache
   includes the full request URL as a cache context for that view, each
   distinct search query effectively mints its own cache entry that is
   unlikely to ever be reused. This is a much better explanation for
   the ``render`` bin's ~85,000+ key count than either raw ingest
   volume or oversized individual entries, and it is a concrete,
   testable lead: excluding volatile query arguments (e.g.
   ``search_api_fulltext``) from that view's render cache keys, or
   disabling render caching on the search results view in favor of
   Dynamic Page Cache, is worth prototyping.

A genuine outsized entry does exist -- in ``page``, not ``render``
   The manifest at ``/do/20e7ff15-8932-447b-9030-dcf386c28532/metadata/iiifmanifest3cws/default.jsonld``
   -- previously flagged as likely using the legacy "CWS" (Creative
   Work Series, per-ADO-canvas) manifest formatter rather than the
   newer "IIIF Presentation API 3 Series Manifest Unified" formatter
   (shipped since ``format_strawberryfield`` 1.6.0) -- has a Drupal
   internal Page Cache entry (``page`` bin) measuring **165,092 bytes
   (~161 KB)** via ``MEMORY USAGE``. That is roughly 56x the ``render``
   bin's average key size and ~9x the largest individual entry found in
   a 500-key ``render`` bin sample. This is the first concrete
   confirmation, in this investigation, of a genuinely outsized single
   cache entry -- just not where or why it was originally guessed
   (community discussion suspected AI/ML-generated listings in
   ``render``; the actual outlier found is a legacy manifest formatter's
   full response in ``page``).

   **Not yet done:** confirming whether this is typical of CWS-formatted
   objects generally (scan ``archipelago_:page:*iiifmanifest3cws*`` and
   size the results) or unusual even among them, and quantifying how
   much smaller the same object's manifest would be under the Unified
   formatter, would settle whether migrating remaining CWS objects is
   worth prioritizing as its own fix.

Correction: ``performance.cache.page.max_age`` does not disable internal Page Cache storage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Earlier working notes in this investigation assumed the site's
``performance.cache.page.max_age = 0`` setting meant Drupal's internal
(Redis-backed) Page Cache was not storing responses for anonymous
requests at all, and that the ``Cache-Control: must-revalidate,
no-cache, private`` header seen on manifest responses confirmed this.
The discovery of a live ``page`` bin entry for the manifest above
disproves that: Drupal core's ``PageCache::getCacheId()``
(``web/core/modules/page_cache/src/StackMiddleware/PageCache.php``)
keys and stores full responses independent of ``max_age``. That setting
governs only the *outbound* browser-facing ``Cache-Control`` /
``Expires`` headers Drupal generates -- not whether the internal Redis
store is written to or read from. ``x-drupal-cache: HIT`` and a
``no-cache`` browser header on the same response are consistent, not
contradictory.

.. _diagnostic-tooling:

Diagnostic tooling
~~~~~~~~~~~~~~~~~~~

Several small standalone scripts were built over the course of this
investigation and are likely to be reusable for future cache
performance work. None are checked into this repository yet; each is a
single self-contained bash script run against production or pre via the
existing ``kubectl -n archipelago port-forward`` pattern.

``eviction_monitor.sh``
    Polls ``redis-cli INFO`` at a fixed interval and logs
    ``used_memory``, ``evicted_keys``, and related counters to CSV --
    used to confirm genuine eviction (vs. expiration or unrelated
    errors) during both steady-state monitoring and the AMI ingest
    event above.

``ttl_audit.sh``
    Cursor-loop census of TTLs across the live keyspace, bin by bin --
    used to determine that ~99.9% of keys carry the Redis module's
    ~360-365 day "permanent cache" TTL convention rather than a
    meaningful expiration policy (see `TTL audit and eviction policy`_).

``cache_watch.sh``
    Polls a single URL at a fixed interval and reports exactly when
    ``x-drupal-cache`` flips HIT/MISS, with how long the prior state
    held -- answers "how long does this specific page actually stay
    cached" in a way a single ``curl -I`` snapshot cannot. Deliberately
    avoids ``set -e``/``pipefail`` in its polling loop so a transient
    network blip doesn't silently kill a run meant to last hours.

``render_key_sizer.sh``
    Samples keys matching a glob pattern (any bin, not just
    ``render``) via cursor-loop ``SCAN``, then ranks them by actual
    ``MEMORY USAGE`` rather than key count -- the tool behind both
    findings in `Cache bin "pollution" and key-count vs. key-size`_
    above. Usage: ``REDIS_CLI="redis-cli -h 127.0.0.1 -p 6379"
    ./render_key_sizer.sh [PATTERN] [SAMPLE_LIMIT] [TOP_N]``.

Open Next Steps
~~~~~~~~~~~~~~~~~

* Confirm whether the community-discussion Redis figures (1.3GB,
  ``volatile-lru``) describe production or a different environment
  before acting on recommendations from that thread.
* Prototype excluding volatile query arguments (e.g.
  ``search_api_fulltext``) from the search results view's render cache
  keys, or moving that view off render caching entirely, to address the
  cache-context cardinality driver identified above.
* Scan and size all ``iiifmanifest3cws``-pattern ``page`` bin entries to
  determine whether the 165KB finding is typical of CWS-formatted
  objects or unusual even among them.
* Determine which objects are still served via the legacy CWS formatter
  vs. the newer Unified formatter, and estimate the memory/performance
  benefit of migrating the remainder.
* Investigate PHP-FPM (``pm.max_children``, per-worker ``memory_limit``,
  ``max_execution_time``) and nginx/php-fpm proxy timeout settings as
  the likely direct cause of 5xx errors on large manifests during bulk
  ingest.
* Capture a before/after "keys per cache bin" diff around a planned
  ~500-page book ingest.
* Only after the above data is in hand, decide whether to implement
  selective cache-bin-to-database routing (`Cache bin "pollution" and
  key-count vs. key-size`_) -- not as a default fix, but as a
  data-justified change to a specific bin.

``redis-cli`` Tips and Tricks
--------------------------------

A running reference of ``redis-cli`` commands that came up repeatedly
during this investigation. All of these were run against production/pre
via the existing port-forward pattern::

    kubectl -n archipelago port-forward deploy/redis 6379:6379 &
    # then either prefix every command with -h 127.0.0.1 -p 6379,
    # or just run `redis-cli -h 127.0.0.1 -p 6379` interactively.

Finding keys
~~~~~~~~~~~~~

Never use ``KEYS *`` (or ``KEYS <pattern>``) against production -- it
blocks the whole server while it walks the entire keyspace. ``SCAN``
does the same job incrementally without blocking::

    redis-cli --scan --pattern "archipelago_:render:*" | head -20

``--scan --pattern`` is a convenience wrapper around the cursor-based
``SCAN`` command; it's fine for a quick look, but for anything you want
to count reliably or feed into a size-ranking pass, loop the cursor
yourself (this is what ``render_key_sizer.sh`` and ``ttl_audit.sh`` do
under the hood -- see `Diagnostic tooling`_)::

    redis-cli SCAN 0 MATCH "archipelago_:render:*" COUNT 200

Note that ``MATCH`` filters results *after* Redis walks its internal
hash table -- a very narrow pattern can still take many round-trips to
finish if the total keyspace is large, even if very few keys actually
match (we saw this directly: 1,396 SCAN round-trips to find 13 matching
keys). That's normal, not a sign of a stuck query.

When you don't know which bin something lives in (e.g. a specific
node ID or object UUID, which can show up in ``render``, ``page``,
``dynamic_page_cache``, ``entity``, or ``data`` depending on what
triggered it), skip the bin prefix entirely and match on the
identifying text anywhere in the key::

    redis-cli --scan --pattern "*20e7ff15-8932-447b-9030-dcf386c28532*"
    redis-cli --scan --pattern "*node:59022*"

Sizing keys
~~~~~~~~~~~~

Key *count* and key *size* are independent questions -- a bin can have
80,000 tiny keys and a handful of huge ones, and ``--scan`` alone can't
tell you which. Size a specific key::

    redis-cli MEMORY USAGE '<key>' SAMPLES 0

(``SAMPLES 0`` forces an exact count rather than an estimate -- worth
the extra cost for a one-off check; for ranking many keys at once, use
``render_key_sizer.sh`` instead of looping this by hand, since it's one
round-trip per key and adds up fast on a big sample.)

Total dataset size, for a sanity-check against ``maxmemory``::

    redis-cli DBSIZE
    redis-cli INFO memory | grep used_memory:

Freshness / staleness of a specific key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Redis has no "key created at" timestamp. Two proxies instead::

    redis-cli OBJECT IDLETIME '<key>'   # seconds since last read/write
    redis-cli TTL '<key>'               # seconds remaining

``OBJECT IDLETIME`` only works under an LRU eviction policy (it's
replaced by an access-frequency counter under LFU policies) -- fine
here since production runs ``allkeys-lru``. Since this site's Redis
module TTL convention is ~360-365 days for effectively all keys (see
`TTL audit and eviction policy`_), ``TTL`` can be used as a rough
stand-in for "how long ago was this written": ``31536000 -
<ttl_remaining>`` seconds. Neither command tells you whether a key was
rewritten with identical content since it was first created -- for that
you need to watch a key over time (``cache_watch.sh``), not inspect a
single snapshot.

Eviction policy and config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    redis-cli CONFIG GET maxmemory
    redis-cli CONFIG GET maxmemory-policy

Worth knowing: a ``CONFIG SET`` changes the running server only -- it
does not persist across a pod restart unless the same value is also set
in the deployment's startup args/config. If a policy or ceiling looks
different than expected, check both the live ``CONFIG GET`` value and
the deployment YAML before assuming one or the other is stale.

Eviction and hit-rate health
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    redis-cli INFO stats | grep -E "evicted_keys|expired_keys|keyspace_hits|keyspace_misses"

``evicted_keys`` increasing means Redis is discarding data under memory
pressure (LRU eviction); ``expired_keys`` increasing means normal
TTL-based expiration. The two are easy to conflate but mean very
different things -- this distinction (``expired_keys: 0`` alongside
climbing ``evicted_keys``) is what originally confirmed eviction, not
expiration, as the root cause documented in this report. For anything
beyond a single snapshot, ``eviction_monitor.sh`` (`Diagnostic
tooling`_) polls this on an interval and logs it to CSV.

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
  showing a ``save`` directive pattern; also discussed cache bin
  "pollution," ``maxmemory`` sizing, PHP-FPM/CPU exhaustion during
  ingest, and the CWS vs. Unified manifest formatter distinction (see
  `Follow-up Investigation: Manifest-Specific Cache Behavior (2026-09)`_).
* ``web/modules/contrib/format_strawberryfield/format_strawberryfield.module``,
  ``format_strawberryfield_cron()`` -- source of the cron-driven embargo
  cache tag invalidation described above.
* ``web/modules/contrib/format_strawberryfield/src/Controller/MetadataExposeDisplayController.php``
  and ``.../src/EmbargoResolver.php`` -- confirm the embargo cache tag is
  only attached to objects with a currently active
  ``date_embargo_lift``.
* ``web/core/modules/page_cache/src/StackMiddleware/PageCache.php``,
  ``getCacheId()`` -- confirms the internal Page Cache key format and
  that storage is independent of ``performance.cache.page.max_age``.
* Production manifest example used throughout the follow-up
  investigation: ``/do/20e7ff15-8932-447b-9030-dcf386c28532/metadata/iiifmanifest3cws/default.jsonld``
  (``page`` bin entry measured at 165,092 bytes via ``MEMORY USAGE``,
  2026-09-22); node ``59022`` used as the cache-context cardinality case
  study (13 render-bin entries, 1.1-6.2 KB each).
