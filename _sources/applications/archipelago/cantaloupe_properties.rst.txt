.. _cantaloupe-properties:

=====================================
Cantaloupe Configuration Reference
=====================================

Overview
========

`Cantaloupe <https://cantaloupe-project.github.io/>`_ is the IIIF Image API
server used by Archipelago. It reads source images (TIFF, JP2, JPEG, PDF,
video, etc.) from storage, processes them on request (crop, scale, rotate,
convert), and returns derivatives to IIIF viewers such as Mirador, Universal
Viewer, and Clover.

``cantaloupe.properties`` is a Java properties file. Each line is a
``key = value`` pair, and lines beginning with ``#`` are comments. The file is
organized into these major sections:

#. :ref:`cp-server` — HTTP/HTTPS listeners and request limits
#. :ref:`cp-delegate` — optional Ruby delegate script
#. :ref:`cp-endpoints` — IIIF, admin, API, and health endpoints
#. :ref:`cp-sources` — where source images are read from
#. :ref:`cp-processors` — which library decodes each image format
#. :ref:`cp-client-cache` — ``Cache-Control`` headers sent to browsers
#. :ref:`cp-server-cache` — server-side source and derivative caching
#. :ref:`cp-overlays` — watermarks
#. :ref:`cp-logging` — application, error, and access logs

.. note::

   Most settings take effect without a restart. Settings marked with ``!!``
   in the file's comments **require a restart** of Cantaloupe (in Archipelago,
   restart the ``esmero-cantaloupe`` container or pod).

.. note::

   Empty values (``key =``) mean "use Cantaloupe's default." The file header
   notes that empty values may also be supplied by ``docker-compose`` (or a
   Kubernetes manifest) through environment variables, so the effective value
   in a running deployment may differ from what appears here.


Quick Summary of This Configuration
===================================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Concern
     - Current setting
   * - Listening on
     - HTTP ``0.0.0.0:8182`` (HTTPS disabled)
   * - IIIF Image API
     - Versions 2 and 3 enabled; version 1 disabled
   * - Image source
     - ``S3Source`` → MinIO at ``http://esmero-minio:9000``, bucket ``archipelago``
   * - Processor selection
     - ``ManualSelectionStrategy`` (per-format mapping)
   * - JPEG 2000 decoding
     - ``OpenJpegProcessor``
   * - Server cache
     - ``FilesystemCache`` at ``/var/cache/cantaloupe``
   * - Derivative cache lifetime
     - 30 days
   * - Browser cache lifetime
     - 7 days
   * - Admin panel and API
     - **Enabled, with default credentials** (see :ref:`cp-security`)
   * - Watermarks
     - Disabled
   * - Logging
     - ``info`` level to console only


.. _cp-server:

Server and Request Limits
=========================

Temporary directory
-------------------

.. code-block:: properties

   temp_pathname =

Blank uses the JVM's default temp directory (usually ``/tmp``). Cantaloupe
writes temporary files here when processing, so the location needs enough
free space for the largest source images being processed concurrently.

HTTP and HTTPS listeners
------------------------

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Key
     - Value
     - Meaning
   * - ``http.enabled``
     - ``true``
     - Serve plain HTTP.
   * - ``http.host``
     - ``0.0.0.0``
     - Listen on all interfaces inside the container.
   * - ``http.port``
     - ``8182``
     - Standard Cantaloupe port.
   * - ``https.enabled``
     - ``false``
     - TLS is not terminated by Cantaloupe.
   * - ``https.key_store_*``
     - placeholders
     - Unused while HTTPS is disabled.

In Archipelago, TLS is normally terminated upstream (nginx or an ingress
controller), which proxies to Cantaloupe over plain HTTP. The keystore values
are sample placeholders and are ignored.

Thread pool and queue
---------------------

.. code-block:: properties

   http.min_threads =
   http.max_threads =
   http.accept_queue_limit =

Blank values use Cantaloupe's defaults. Tune these only if you observe request
queuing or thread exhaustion under load.

Reverse-proxy URIs
------------------

.. code-block:: properties

   base_uri =
   slash_substitute =

``base_uri``
   Overrides the base URL used in ``info.json`` ``id``/``@id`` values and
   ``Link`` headers. Leave blank when the proxy sends correct
   ``X-Forwarded-Host``, ``X-Forwarded-Proto``, ``X-Forwarded-Port``, and
   ``X-Forwarded-Path`` headers. If viewers receive ``info.json`` documents
   pointing at ``http://esmero-cantaloupe:8182/...`` instead of the public
   hostname, either fix the forwarded headers or set this value.

``slash_substitute``
   Archipelago identifiers are S3 object keys that can contain ``/``. If a
   proxy decodes ``%2F`` before it reaches Cantaloupe, define a substitute
   character sequence here. Blank means slashes must arrive as ``%2F``.

Size limits
-----------

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Key
     - Value
     - Meaning
   * - ``max_pixels``
     - ``400000000``
     - Refuse responses larger than 400 megapixels. Protects memory.
   * - ``max_scale``
     - ``1.0``
     - Never upscale beyond the source's native resolution.

Meta-identifiers
----------------

.. code-block:: properties

   meta_identifier.transformer = StandardMetaIdentifierTransformer
   meta_identifier.transformer.StandardMetaIdentifierTransformer.delimiter = ;

A *meta-identifier* extends an image identifier with extra information such as
a page number. With the ``;`` delimiter, ``my-file.pdf;3`` requests page 3 of a
multi-page source (PDF, multi-page TIFF). Archipelago relies on this for
paged PDFs.

Error reporting
---------------

.. code-block:: properties

   log_error_responses = true
   print_stack_trace_on_error_pages = true

``log_error_responses`` logs every 4xx/5xx response, which is useful for
diagnosing missing images. ``print_stack_trace_on_error_pages`` includes Java
stack traces in HTTP error bodies.

.. warning::

   Stack traces on public error pages reveal internal class names, paths, and
   versions. Set ``print_stack_trace_on_error_pages = false`` in production.


.. _cp-delegate:

Delegate Script
===============

.. code-block:: properties

   delegate_script.enabled = false
   delegate_script.pathname = delegates.rb

The delegate script is an optional Ruby (JRuby) file that customizes
Cantaloupe's behavior per request: authorization, dynamic source lookup,
per-request processor or overlay choices, and so on. It is **disabled** in
this configuration, so every setting below that offers a
``ScriptLookupStrategy`` or ``ScriptStrategy`` option uses its ``Basic``
equivalent instead.

Enable it if you need IIIF Auth, restricted-access images, or identifier
rewriting that ``BasicLookupStrategy`` cannot express.


.. _cp-endpoints:

Endpoints
=========

IIIF Image API
--------------

.. list-table::
   :header-rows: 1
   :widths: 40 15 45

   * - Key
     - Value
     - Meaning
   * - ``endpoint.iiif.1.enabled``
     - ``false``
     - ``/iiif/1`` is off (legacy, rarely needed).
   * - ``endpoint.iiif.2.enabled``
     - ``true``
     - ``/iiif/2`` is on.
   * - ``endpoint.iiif.3.enabled``
     - ``true``
     - ``/iiif/3`` is on.
   * - ``endpoint.iiif.min_size``
     - ``64``
     - Smallest size advertised in ``info.json`` ``sizes``.
   * - ``endpoint.iiif.min_tile_size``
     - ``512``
     - Smallest tile size advertised in ``info.json`` ``tiles``.
   * - ``endpoint.iiif.restrict_to_sizes``
     - ``false``
     - Clients may request arbitrary sizes, not only advertised ones.

Example request patterns:

.. code-block:: text

   https://<host>/cantaloupe/iiif/2/<identifier>/info.json
   https://<host>/cantaloupe/iiif/3/<identifier>/full/max/0/default.jpg

The public path prefix depends on how your proxy or ingress routes to
Cantaloupe.

Control Panel and HTTP API
--------------------------

.. code-block:: properties

   endpoint.admin.enabled = true
   endpoint.admin.username = admin
   endpoint.admin.secret = archipelago

   endpoint.api.enabled = true
   endpoint.api.username = admin
   endpoint.api.secret = archipelago

``/admin``
   Web Control Panel for viewing and editing configuration and status.

HTTP API
   Administrative API used for tasks such as purging cached items for an
   identifier (for example, after replacing a master file).

.. warning::

   The file header says ``endpoint.admin.enabled`` is set to ``false``, but in
   this copy it is **set to** ``true``. Both the Control Panel and the API use
   the well-known default credentials ``admin`` / ``archipelago``.
   See :ref:`cp-security`.

Health check
------------

.. code-block:: properties

   endpoint.health.enabled = true
   endpoint.health.dependency_check = false

``/health`` returns a quick status suitable for Kubernetes liveness and
readiness probes. With ``dependency_check = false`` the check does not probe
S3 or caches, which keeps it fast and avoids pod restarts when MinIO is
briefly unavailable.


.. _cp-sources:

Sources
=======

A *source* tells Cantaloupe where to find the original image for an
identifier.

.. code-block:: properties

   source.static = S3Source
   source.delegate = false

All requests use ``S3Source``. Because ``source.delegate`` is ``false``, there
is no per-request source selection.

S3Source (active)
-----------------

.. list-table::
   :header-rows: 1
   :widths: 45 25 30

   * - Key
     - Value
     - Notes
   * - ``S3Source.endpoint``
     - ``http://esmero-minio:9000``
     - Archipelago's MinIO service. Only needed for non-AWS S3.
   * - ``S3Source.region``
     - ``us-east-2``
     - Ignored by most MinIO setups, but must be a valid value.
   * - ``S3Source.access_key_id``
     - ``minio``
     - Default MinIO credential.
   * - ``S3Source.secret_key``
     - ``minio123``
     - Default MinIO credential.
   * - ``S3Source.lookup_strategy``
     - ``BasicLookupStrategy``
     - Identifier maps directly to an object key.
   * - ``S3Source.BasicLookupStrategy.bucket.name``
     - ``archipelago``
     - Bucket holding Archipelago files.
   * - ``S3Source.BasicLookupStrategy.path_prefix``
     - *(blank)*
     - Nothing prepended to the identifier.
   * - ``S3Source.BasicLookupStrategy.path_suffix``
     - *(blank)*
     - Nothing appended to the identifier.

How identifiers resolve
~~~~~~~~~~~~~~~~~~~~~~~

With an empty prefix and suffix, the IIIF identifier *is* the object key in
the ``archipelago`` bucket:

.. code-block:: text

   /iiif/3/2a%2Fe1%2Fimage-abc123.jp2/full/max/0/default.jpg
                 │
                 ▼
   s3://archipelago/2a/e1/image-abc123.jp2

Chunked reads
~~~~~~~~~~~~~

.. code-block:: properties

   S3Source.chunking.enabled = true
   S3Source.chunking.chunk_size = 512K
   S3Source.chunking.cache.enabled = true
   S3Source.chunking.cache.max_size = 5M

Cantaloupe fetches the object in 512 KB ranged requests rather than all at
once. For tiled pyramidal formats (JP2, tiled TIFF) this can avoid
downloading the whole file to serve one tile. Downloaded chunks are cached in
memory for the life of a single request, up to 5 MB.

.. note::

   If your deployment uses an external S3 service instead of the bundled
   MinIO container, ``S3Source.endpoint``, credentials, bucket, and region are
   the values to change (or override via environment variables).

Inactive sources
----------------

The following sections are present but unused because ``source.static`` is
``S3Source``. Their values are upstream samples.

``FilesystemSource``
   Reads from a local directory (``path_prefix = /home/myself/images/``).

``HttpSource``
   Fetches images from a URL prefix (``http://localhost/images/``), with
   optional Basic auth, HEAD-vs-ranged-GET probing, and chunking.

``AzureStorageSource``
   Reads from an Azure Blob Storage container.

``JdbcSource``
   Reads image blobs from a database (requires delegate methods and a JDBC
   driver).


.. _cp-processors:

Processors
==========

A *processor* decodes a source format and produces the requested derivative.

Selection strategy
------------------

.. code-block:: properties

   processor.selection_strategy = ManualSelectionStrategy

With ``ManualSelectionStrategy``, each format is explicitly mapped to a
processor. The alternative, ``AutomaticSelectionStrategy``, picks the "best"
available processor at runtime.

Format-to-processor map
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Format
     - Processor
     - Notes
   * - ``jp2``
     - ``OpenJpegProcessor``
     - Required on ARM64. On x86/AMD64, ``KakaduNativeProcessor`` is faster
       if available.
   * - ``jpg``, ``png``, ``tif``
     - ``Java2dProcessor``
     - Pure Java, no native dependencies.
   * - ``pdf``
     - ``PdfBoxProcessor``
     - Rasterizes PDF pages; use ``;N`` meta-identifiers for page N.
   * - ``avi``, ``flv``, ``mov``, ``mp4``, ``mv4``, ``mpg``, ``webm``
     - ``FfmpegProcessor``
     - Extracts still frames from video (e.g., poster images).
   * - ``bmp``, ``gif``, ``xpm``
     - *(blank)*
     - Fall through to the fallback.
   * - **fallback**
     - ``Java2dProcessor``
     - Used for any format not listed.

Retrieval strategy
------------------

.. code-block:: properties

   processor.stream_retrieval_strategy = StreamStrategy
   processor.fallback_retrieval_strategy = CacheStrategy
   processor.purge_incompatible_from_source_cache = true

``S3Source`` is a *stream* source. Some processors (notably
``OpenJpegProcessor`` and ``FfmpegProcessor``) need a real file on disk.

* ``StreamStrategy`` streams directly whenever the processor allows it.
* When it doesn't, ``CacheStrategy`` downloads the object into the
  **source cache** (``FilesystemCache``) and processes it from there. Later
  requests for the same image reuse the local copy instead of fetching it
  from S3 again.
* Files in the source cache whose format cannot be determined are purged.

.. tip::

   Because JP2 requests go through the source cache, the volume behind
   ``/var/cache/cantaloupe`` should be sized for your working set of JP2
   masters, not just derivatives.

Global processing options
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 20 40

   * - Key
     - Value
     - Meaning
   * - ``processor.dpi``
     - ``150``
     - Rasterization resolution for vector sources such as PDF.
   * - ``processor.background_color``
     - ``white``
     - Fill for rotation and alpha flattening.
   * - ``processor.downscale_filter``
     - ``bicubic``
     - Resampling filter when shrinking.
   * - ``processor.upscale_filter``
     - ``bicubic``
     - Resampling filter when enlarging (moot with ``max_scale = 1.0``).
   * - ``processor.downscale_linear``
     - ``false``
     - Linear-light downscaling off (faster).
   * - ``processor.sharpen``
     - ``0``
     - No unsharp mask.
   * - ``processor.jpg.progressive``
     - ``true``
     - Output progressive JPEGs.
   * - ``processor.jpg.quality``
     - ``80``
     - JPEG output quality (1–100).
   * - ``processor.tif.compression``
     - ``LZW``
     - Compression for TIFF output.

ImageIO plugin preferences
--------------------------

All ``processor.imageio.*`` keys are blank, so Cantaloupe's default Java
ImageIO readers and writers are used. These should not normally be changed.

Processor binary paths
----------------------

.. code-block:: properties

   FfmpegProcessor.path_to_binaries =
   OpenJpegProcessor.path_to_binaries =
   GrokProcessor.path_to_binaries =

Blank means the binaries (``ffmpeg``/``ffprobe``, ``opj_decompress``,
``grk_decompress``) are found on the container's ``PATH``.

PDF memory handling
-------------------

.. code-block:: properties

   processor.pdf.scratch_file_enabled = true
   processor.pdf.max_memory_bytes = -1

PDFBox may spill to disk while loading PDFs, with no cap on in-memory use.
Very large PDFs can still consume significant heap; set a positive byte limit
if PDF requests cause memory pressure.


.. _cp-client-cache:

Client-Side Caching
===================

These keys build the ``Cache-Control`` header on image responses.

.. code-block:: properties

   cache.client.enabled = true
   cache.client.max_age = 604800
   cache.client.public = true
   cache.client.must_revalidate = true
   cache.client.no_transform = true

Resulting header:

.. code-block:: http

   Cache-Control: public, max-age=604800, must-revalidate, no-transform

* Browsers and shared caches (CDNs, proxies) may store responses for
  **7 days**.
* After expiry, caches must revalidate before reusing a response.
* ``no-transform`` stops intermediaries from recompressing images.


.. _cp-server-cache:

Server-Side Caching
===================

Cantaloupe keeps three kinds of server-side cache.

.. list-table::
   :header-rows: 1
   :widths: 20 25 20 35

   * - Cache
     - Backend
     - Lifetime
     - Contents
   * - Source
     - ``FilesystemCache``
     - 3 days (``259200`` s)
     - Full copies of S3 source files needed by file-based processors.
   * - Derivative
     - ``FilesystemCache``
     - 30 days (``2592000`` s)
     - Processed tiles and images, and ``info.json`` responses.
   * - Info
     - JVM heap
     - Process lifetime
     - In-memory "level 1" cache of image info in front of the derivative
       cache.

Related behavior:

``cache.server.resolve_first = false``
   Cached derivatives are served without confirming the source still exists.
   Faster, but a deleted or replaced master may continue to be served from
   cache until it expires or is purged.

``cache.server.purge_missing = true``
   Purge cached data for sources reported missing. Because
   ``resolve_first`` is ``false``, this is effectively inactive.

``cache.server.worker.enabled = true`` / ``interval = 86400``
   A background worker removes expired cache items once per day.

.. tip::

   When a master file is replaced in Archipelago under the same identifier,
   purge that identifier through the HTTP API (or wait for TTL expiry);
   otherwise viewers will keep seeing old tiles.

FilesystemCache
---------------

.. code-block:: properties

   FilesystemCache.pathname = /var/cache/cantaloupe
   FilesystemCache.dir.depth = 3
   FilesystemCache.dir.name_length = 2

Cached files live under ``/var/cache/cantaloupe`` in a three-level directory
tree with two-character directory names (e.g. ``a1/b2/c3/...``), keeping the
number of entries per directory manageable. In a container this path should
be a persistent volume. Purge the cache after changing ``depth`` or
``name_length``.

Inactive cache backends
-----------------------

``HeapCache``, ``JdbcCache``, ``S3Cache``, ``AzureStorageCache``, and
``RedisCache`` are configured with sample values but are not used, since both
source and derivative caches are set to ``FilesystemCache``.

``S3Cache`` is the most likely alternative in a Kubernetes deployment, because
it lets multiple Cantaloupe replicas share one derivative cache without a
shared filesystem volume. Its endpoint is already pointed at MinIO but its
credentials and bucket are blank.


.. _cp-overlays:

Overlays (Watermarks)
=====================

.. code-block:: properties

   overlays.strategy = BasicStrategy
   overlays.BasicStrategy.enabled = false

Overlays are **disabled**. If enabled, ``BasicStrategy`` can stamp either a PNG
image or a text string onto every derivative above a size threshold
(400×300 pixels by default), at a configurable position and inset. The text,
font, and image values in the file are upstream samples.


.. _cp-logging:

Logging
=======

Application log
---------------

.. code-block:: properties

   log.application.level = info
   log.application.ConsoleAppender.enabled = true

Application messages at ``info`` and above go to standard output, where
``docker logs`` or ``kubectl logs`` can read them. File, rolling-file, and
syslog appenders are disabled; their paths are placeholders. Logstash JSON
encoding is available for each appender but disabled.

.. note::

   Don't enable ``FileAppender`` and ``RollingFileAppender`` at the same time.

Error log
---------

All error-log appenders are disabled. When enabled, they copy ``WARN`` and
above into a separate file.

Access log
----------

All access-log appenders, including the console appender, are disabled, so
individual image requests are not logged. Enable
``log.access.ConsoleAppender.enabled`` temporarily when debugging viewer
request patterns, or rely on your proxy/ingress access logs instead.


.. _cp-security:

Security Checklist
==================

This file ships with development-friendly defaults. Before running it in
production, review the following.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Setting
     - Recommendation
   * - ``endpoint.admin.enabled = true``
     - Disable, or change ``endpoint.admin.secret`` and block ``/admin`` at
       the proxy.
   * - ``endpoint.api.secret = archipelago``
     - Change to a strong secret; restrict the API to internal networks.
   * - ``S3Source.access_key_id`` / ``secret_key``
     - Replace ``minio`` / ``minio123`` and supply via environment variables
       or Kubernetes secrets rather than this file.
   * - ``print_stack_trace_on_error_pages = true``
     - Set to ``false``.
   * - ``https.key_store_password = myPassword``
     - Harmless while HTTPS is off, but remove or replace if HTTPS is
       enabled.


Further Reading
===============

* `Cantaloupe user manual <https://cantaloupe-project.github.io/manual/>`_
* `IIIF Image API 3.0 <https://iiif.io/api/image/3.0/>`_
* `Archipelago documentation <https://docs.archipelago.nyc/>`_