============================================================
Archipelago 1.6.0 Upgrade Plan: Local Build, Lockfile Deploy
============================================================

:Date: 2026-10-15
:Author: Mark Baggett

Approach
========

Following guidance from Diego, we resolve and test the upgrade on a local Archipelago 1.6.0 running our
production config. Then we ship the tested ``composer.json`` and
``composer.lock`` to production and run ``composer install``. This follows
Diego's recommendation (Oct 15).

Why this way:

- No dependency resolution happens on the live server. ``composer install``
  installs exactly what we tested.
- Problems with custom modules (``google_tag``, ``saml_sp``) or config surface
  locally, not in production.
- No pod or image changes are needed. Code lives on the ``archipelago`` PVC,
  and 1.6.0 still uses the 1.5.0 PHP image.

.. important::

   ``composer install`` only changes code. Production still needs
   ``drush updatedb`` afterward.

Environment Facts
=================

Production already runs Archipelago 1.6.0 code on Drupal 10.5.10. This
upgrade finishes the job and moves core to 10.6.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Item
     - Value
   * - Namespace / PHP deployment
     - ``archipelago`` / ``esmero-php``
   * - Code + public/private files
     - ``archipelago`` PVC (50Gi, trident-nfs, RWX) mounted at ``/var/www/html``
   * - Database
     - External MariaDB/MySQL
   * - Object storage
     - External AWS S3
   * - Other PVCs
     - ``esmero-solr`` 30Gi (index); ``esmero-cantaloupe`` 250Gi and ``redis`` 40Gi (caches)
   * - Archipelago packages
     - strawberryfield 1.6.0, AMI 1.0.0, strawberry_runners 1.0.0, Fragaria 0.4.0
   * - Drupal core
     - 10.5.10 (scaffold and project-message at 10.6.9)
   * - Custom modules
     - ``drupal/google_tag``, ``drupal/saml_sp`` (SSO login)

Phase 1: Prep from Production (Read-Only)
=========================================

Nothing in this phase changes production.

- Export config and copy the folder off:

  .. code-block:: bash

     kubectl exec -n archipelago <php-pod> -- drush cex --destination=/var/www/html/config/backup-2026-10

- Copy ``/var/www/html/composer.json`` and ``composer.lock`` off the pod.
- Record the site UUID: ``drush cget system.site uuid``.
- Copy any custom code under ``web/modules/custom`` and ``web/themes/custom``.
- Check pending database updates: ``drush updatedb:status``.
- Confirm the storage mix:

  .. code-block:: bash

     drush sqlq "SELECT SUBSTRING_INDEX(uri,'://',1) AS scheme, COUNT(*) FROM file_managed GROUP BY scheme"

- Note prod's PHP version (``php -v``) and whether dev packages are installed.

Phase 2: Local Build and Test
=============================

The output of this phase is a tested ``composer.json`` and ``composer.lock``,
plus a config diff showing what the update hooks change.

#. Clone archipelago-deployment (1.6.0) and bring it up locally. Use the same
   PHP version as prod's ``esmero-php`` image so the lock resolves for the
   same platform.
#. Add our extra modules before importing config. The import fails if config
   references missing modules.

   .. code-block:: bash

      composer require drupal/google_tag drupal/saml_sp

   Add any custom code as well.
#. Set the local site UUID to prod's, or ``drush cim`` refuses:

   .. code-block:: bash

      drush cset system.site uuid <prod-uuid>

#. Import prod config:

   .. code-block:: bash

      drush cim --source=<exported folder>

#. Bump core (add ``drupal/core-dev:^10.6 --dev`` if prod has dev packages):

   .. code-block:: bash

      composer require drupal/core:^10.6 drupal/core-recommended:^10.6 \
        drupal/core-composer-scaffold:^10.6 drupal/core-project-message:^10.6 --no-update

#. Update and apply:

   .. code-block:: bash

      composer update -W
      drush updatedb
      drush cr

#. Test: ingest, AMI, search and facets, IIIF manifests, metadata displays,
   OAI. Test SAML login if it can be reached locally.
#. Run ``drush cex`` and diff against prod's export. The diff is what
   ``updatedb`` will change in prod's config.
#. Optional, stronger: load a prod database dump locally and rerun
   ``drush updatedb``. This exercises update hooks that migrate content,
   which config alone doesn't.
#. Commit the final ``composer.json`` and ``composer.lock``.

Phase 3: Dev Environment Rehearsal
==================================

Before touching production, we run the exact Phase 4 cutover on our dev
Kubernetes environment, using the same ``composer.json`` and
``composer.lock``. The local build proves the dependencies resolve. The dev
rehearsal proves the workflow works in our real setup: ``kubectl exec`` and
``kubectl cp``, the NFS-backed PVC, file permissions, the external database,
and S3.

Before the rehearsal
--------------------

- Confirm dev matches prod where it matters: the same ``esmero-php`` image and
  PHP version, the same composer.json and composer.lock currently installed,
  and code on a PVC mounted at ``/var/www/html``.
- Refresh the dev database from a recent prod dump, so ``drush updatedb``
  runs against realistic data. Use a separate dev database on the external
  server, never the production one.
- Check which S3 bucket dev points to (``drush cget s3fs.settings bucket``).
  If it's the production bucket, don't run ingest or AMI tests that write
  files, or switch dev to its own bucket first.
- Confirm SAML on dev points at a test identity provider or service provider
  entry, so login can be tested safely.

The rehearsal
-------------

#. Run every Phase 4 step on dev, in order, with the same commands. Only the
   namespace and pod name change.
#. Time each step, especially ``composer install`` and ``drush updatedb``.
   The total sets the length of the production maintenance window.
#. Run the full smoke test from Phase 4, plus ingest and AMI if dev has its
   own bucket.
#. Practice the rollback: restore the dev database and the PVC snapshot (or
   the old composer files), and confirm the site comes back. This proves the
   snapshot and restore process before we depend on it in production.
#. Run the upgrade again after the rollback, so dev ends on the new version.
#. Fix any steps in this document that didn't work as written.

Exit criteria
-------------

Move on to production only when all of these are true:

- ``composer install`` and ``drush updatedb`` complete without errors on dev.
- The smoke test passes on dev, including SAML login.
- The rollback has been tested on dev and works.
- We have a measured time for the maintenance window.

Phase 4: Production Cutover
===========================

Plan for a weekday morning, not a Friday. Every command runs in the existing
PHP pod via ``kubectl exec -n archipelago <php-pod> -- …``.

#. **Maintenance mode on:**

   .. code-block:: bash

      drush state:set system.maintenance_mode 1 && drush cr

#. **Back up:**

   - Snapshot the ``archipelago`` PVC (VolumeSnapshot or ONTAP snapshot). At
     minimum, keep copies of the current ``composer.json`` and
     ``composer.lock``.
   - Dump or snapshot the external database.

#. **Copy in the new files:** ``kubectl cp`` the tested ``composer.json`` and
   ``composer.lock`` into ``/var/www/html``.
#. **Loosen permissions** on ``web/sites/default`` so the scaffold step can
   rewrite files there.
#. **Install:** ``composer install`` (with ``--no-dev`` if prod has no dev
   packages).
#. **Update the database:** ``drush updatedb -y``, then ``drush cr``. Run it so
   a dropped ``kubectl exec`` session can't interrupt it.
#. **Optional:** a handpicked config import
   (``drush cim --partial --source=config/sync_handpicked``), and ``deploy.sh``
   to add the new 1.6.0 metadata display templates. Don't run
   ``update_deployed.sh``.
#. **Restore permissions** on ``web/sites/default``.
#. **Smoke test:** SAML login, an object page, IIIF manifest and Cantaloupe
   images, search, AMI, and ``drush status``.
#. **Maintenance mode off:**

   .. code-block:: bash

      drush state:set system.maintenance_mode 0 && drush cr

Rollback
========

Roll back if ``composer install`` or ``drush updatedb`` fails, or the smoke
test finds a blocking problem. Code and database must go back together.

#. Keep the site in maintenance mode.
#. Restore the external database from the Phase 4 dump or snapshot.
#. Restore code using one of these:

   - Revert the ``archipelago`` PVC to its snapshot. This also covers files.
   - Or copy back the old ``composer.json`` and ``composer.lock`` and run
     ``composer install``.

#. Run ``drush cr``, smoke test, then turn maintenance mode off.

Open Items
==========

- Is a VolumeSnapshotClass available (``kubectl get volumesnapshotclass``)?
  If not, arrange an ONTAP snapshot with the storage admin.
- Is the external database version supported by Drupal 10.6, and later by
  Drupal 11?
- Should ``archipelago_subtheme`` move from 1.5.0.x-dev to a 1.6.0 branch?
- Who built this environment 11 days ago, and did they run ``drush updatedb``
  or sync config then?
- Does any PHP pod other than ``esmero-php`` mount the ``archipelago`` PVC?
- Pick a cutover window and notify staff about the maintenance period.
- Container updates (Solr 9.10 + OCR highlight 0.9.5, nginx, Cantaloupe
  probes) are deferred to a separate change.
