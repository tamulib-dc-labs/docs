=========================================================
Warming the IIIF Image Cache Before a Browsertrix Crawl
=========================================================

Overview
========

When Browsertrix crawls a page with a IIIF viewer, it captures every image
request the viewer makes while the page loads. If our IIIF image server
(Cantaloupe) has to generate those derivatives on the fly, some requests can
be slow enough to time out or fail during the crawl. Those requests are then
missing from the WACZ, and the archived page replays with broken or blank
tiles.

The fix is to request every image ahead of time so Cantaloupe generates the
derivatives and stores them in its derivative cache. When Browsertrix runs
afterward, the same requests are served quickly from cache.

Warming happens in two passes:

#. **Collection-wide.** Crawl the IIIF collection with ``iiif_crawl.py``. It
   reads every manifest and requests every canvas, every image, and (optionally)
   every image service's ``info.json``. This covers every item in the
   collection, including ones nobody opens by hand before the crawl.
#. **Page-specific.** Capture the exact tile URLs a viewer requests on the
   pages you plan to crawl, and request those with ``check-images.sh``.

The first pass gets every source image read and every item's base derivatives
cached. The second catches the viewport-specific tiles the first pass can't
predict.

This page covers:

* running ``iiif_crawl.py`` against a IIIF collection
* capturing the image URLs a page requests, using the browser's Network panel
* running ``check-images.sh`` to request every URL and log the results
* reading the results to find and fix failures before the crawl

When to Use This
================

Use this process when:

* You are about to crawl pages that embed IIIF viewers (for example, exhibit
  pages or item pages with deep zoom).
* A previous crawl replayed with missing or broken image tiles.
* You want to confirm that every image on a page actually resolves before
  archiving it.

It is less necessary for pages whose images were viewed recently (and are
likely already cached) or that only use a few small static images.

Prerequisites
=============

* Python 3.9 or later with the ``requests`` package (``pip install requests``)
* ``bash`` and ``curl`` (on Windows, use Git Bash or WSL)
* ``jq`` for extracting URLs from the HAR file
* Firefox or Chrome
* Cantaloupe's derivative cache enabled. Without it, warming has no lasting
  effect. In ``cantaloupe.properties``, check:

  .. code-block:: properties

     cache.server.derivative.enabled = true
     cache.server.derivative = FilesystemCache
     # 0 = never expire; otherwise make sure the TTL outlasts the crawl
     cache.server.derivative.ttl_seconds = 0

  If you use ``--info-json`` in Step 1, also enable the info cache so those
  responses are kept:

  .. code-block:: properties

     cache.server.info.enabled = true

.. important::

   The cache only helps when Browsertrix requests the **exact same URLs** you
   warmed. A IIIF image URL encodes region, size, rotation, quality, and
   format, and viewers choose tiles and sizes based on the viewport. Step 1
   warms the image URLs listed in the manifests, which are usually full-size
   images, not viewer tiles. Steps 2 through 4 are what cover the tiles. When
   capturing, use a browser window roughly the same size as the Browsertrix
   crawler's browser, and interact with the viewer (zoom, page through
   canvases) the same way the crawl will.

Step 1: Warm the Whole IIIF Collection
======================================

Run ``iiif_crawl.py`` with the URL of the IIIF collection that holds the items
you are about to crawl:

.. code-block:: bash

   python iiif_crawl.py --info-json --workers 4 -o iiif-results.csv \
     "https://api.library.tamu.edu/iiif-service/fedora/collection/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/london-maps-batch-2"

The script:

#. Reads the collection and gathers every manifest URL. It follows
   sub-collections and paged collections (``first`` and ``next``).
#. Fetches each manifest and finds every canvas and every image on each
   canvas.
#. Requests the ``@id`` of every canvas, then the ``@id`` of every image on
   each canvas. Image responses are downloaded and discarded, which is what
   makes Cantaloupe generate and cache them.
#. With ``--info-json``, also requests each image service's ``info.json``,
   which is the first thing a viewer asks for.

It works with both IIIF Presentation 2 (``sequences`` → ``canvases`` →
``images`` → ``resource``) and Presentation 3 (``items`` → ``AnnotationPage``
→ ``Annotation`` → ``body``) manifests, including ``Choice`` images. Requests
that return ``429`` or a ``5xx`` status are retried up to four times with
backoff.

As it runs, the script prints one line per manifest with its canvas and image
counts, and prints every failure. When it finishes, it prints a total of
successes and failures.

Options
-------

``-o``, ``--output``
   Path for the results CSV. Default ``iiif_crawl_results.csv``.

``--workers``
   Number of simultaneous requests within each manifest. Default ``8``. As
   with ``PARALLEL`` for ``check-images.sh``, keep this modest (``4`` is a
   good start) so you don't overload Cantaloupe while it generates
   derivatives. Large maps are especially expensive.

``--image-method``
   ``get`` (default) downloads each image and discards it. This is what
   warms the cache. ``head`` only checks that each image URL resolves. Use it
   for a quick check, not for warming.

``--info-json``
   Also request each image service's ``info.json``.

Output
------

The script writes one row per request:

.. code-block:: text

   level,manifest,canvas,url,status,ms,error

``level`` is ``manifest``, ``canvas``, ``image``, or ``info.json``. ``ms`` is
the response time in milliseconds. ``status`` is empty when there was no HTTP
response at all, and ``error`` then says why (timeout, connection reset, and
so on).

.. note::

   In Presentation 2 manifests, canvas ``@id`` values are often identifiers
   that were never meant to be dereferenced. A ``404`` on a ``canvas`` row
   does not necessarily mean anything is broken. Focus on ``manifest``,
   ``image``, and ``info.json`` failures.

For what the status codes on ``image`` and ``info.json`` rows mean, see
`Step 5: Review the Results`_.

The Script
----------

.. code-block:: python

   #!/usr/bin/env python3
   """
   Crawl a IIIF collection: fetch every manifest (recursing into sub-collections),
   request the id of every canvas, then request the id of every image on each canvas.

   Handles IIIF Presentation 2 (@id, sequences/canvases/images/resource) and
   Presentation 3 (id, items/AnnotationPage/Annotation/body).

   Usage:
       pip install requests
       python iiif_crawl.py URL [--workers 8] [--image-method get] [--info-json] [-o results.csv]

   Every request is written to a CSV row (level, manifest, canvas, url, status, ms, error),
   so you can filter for failures afterward.
   """
   import argparse
   import csv
   import sys
   import threading
   import time
   from concurrent.futures import ThreadPoolExecutor, as_completed

   import requests
   from requests.adapters import HTTPAdapter
   from urllib3.util.retry import Retry

   USER_AGENT = "TAMU-DigitalCollections-IIIF-Crawler/1.0 (mark.baggett@tamu.edu)"


   def make_session(workers):
       s = requests.Session()
       retry = Retry(total=4, backoff_factor=1.0,
                     status_forcelist=(429, 500, 502, 503, 504),
                     allowed_methods=("GET", "HEAD"))
       adapter = HTTPAdapter(max_retries=retry, pool_connections=workers, pool_maxsize=workers)
       s.mount("http://", adapter)
       s.mount("https://", adapter)
       s.headers["User-Agent"] = USER_AGENT
       return s


   def get_id(obj):
       if isinstance(obj, str):
           return obj
       if isinstance(obj, dict):
           return obj.get("@id") or obj.get("id")
       return None


   def get_type(obj):
       t = obj.get("@type") or obj.get("type") or ""
       return t.split(":")[-1]  # "sc:Manifest" -> "Manifest"


   # ---------- collection traversal ----------

   def iter_manifest_urls(session, collection_url, seen=None):
       """Yield manifest URLs from a collection, recursing into sub-collections."""
       seen = seen if seen is not None else set()
       if collection_url in seen:
           return
       seen.add(collection_url)

       r = session.get(collection_url, timeout=60)
       r.raise_for_status()
       coll = r.json()

       children = []
       # Presentation 2
       children += [(m, "Manifest") for m in coll.get("manifests", [])]
       children += [(c, "Collection") for c in coll.get("collections", [])]
       for m in coll.get("members", []):
           children.append((m, get_type(m)))
       # Presentation 3
       for item in coll.get("items", []):
           children.append((item, get_type(item)))

       for child, ctype in children:
           cid = get_id(child)
           if not cid:
               continue
           if ctype == "Collection":
               yield from iter_manifest_urls(session, cid, seen)
           else:
               yield cid

       # Paged collections (v2 "next"/"first")
       for key in ("first", "next"):
           nxt = get_id(coll.get(key)) if coll.get(key) else None
           if nxt and nxt not in seen:
               yield from iter_manifest_urls(session, nxt, seen)


   # ---------- manifest parsing ----------

   def canvases_and_images(manifest):
       """Return [(canvas_id, [image_ids...]), ...] for a v2 or v3 manifest."""
       out = []
       if "sequences" in manifest:  # Presentation 2
           for seq in manifest.get("sequences", []):
               for canvas in seq.get("canvases", []):
                   imgs = []
                   for anno in canvas.get("images", []):
                       res = anno.get("resource", {})
                       # Choice / multiple images
                       if get_type(res) in ("Choice", "oa:Choice"):
                           for r in [res.get("default")] + list(res.get("item", [])):
                               if r and get_id(r):
                                   imgs.append(get_id(r))
                       elif get_id(res):
                           imgs.append(get_id(res))
                   out.append((get_id(canvas), imgs))
       else:  # Presentation 3
           for canvas in manifest.get("items", []):
               imgs = []
               for page in canvas.get("items", []):
                   for anno in page.get("items", []):
                       body = anno.get("body", {})
                       bodies = body.get("items", []) if get_type(body) == "Choice" else [body]
                       for b in bodies:
                           if isinstance(b, dict) and get_id(b):
                               imgs.append(get_id(b))
               out.append((get_id(canvas), imgs))
       return out


   def image_service_ids(manifest):
       """Map image id -> image service id (for optional info.json checks)."""
       mapping = {}

       def svc_id(res):
           svc = res.get("service")
           if isinstance(svc, list):
               svc = svc[0] if svc else None
           return get_id(svc) if svc else None

       if "sequences" in manifest:
           for seq in manifest["sequences"]:
               for canvas in seq.get("canvases", []):
                   for anno in canvas.get("images", []):
                       res = anno.get("resource", {})
                       if get_id(res) and svc_id(res):
                           mapping[get_id(res)] = svc_id(res)
       else:
           for canvas in manifest.get("items", []):
               for page in canvas.get("items", []):
                   for anno in page.get("items", []):
                       b = anno.get("body", {})
                       if isinstance(b, dict) and get_id(b) and svc_id(b):
                           mapping[get_id(b)] = svc_id(b)
       return mapping


   # ---------- requests ----------

   def probe(session, url, method="get"):
       """Request a URL; for GET, stream and discard the body. Returns (status, ms, error)."""
       t0 = time.monotonic()
       try:
           if method == "head":
               r = session.head(url, timeout=120, allow_redirects=True)
               if r.status_code == 405:  # HEAD not allowed -> fall back to GET
                   return probe(session, url, "get")
           else:
               r = session.get(url, timeout=300, stream=True)
               for _ in r.iter_content(chunk_size=1 << 16):
                   pass
           return r.status_code, int((time.monotonic() - t0) * 1000), ""
       except requests.RequestException as e:
           return None, int((time.monotonic() - t0) * 1000), str(e)


   def main():
       ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
       ap.add_argument("collection")
       ap.add_argument("-o", "--output", default="iiif_crawl_results.csv")
       ap.add_argument("--workers", type=int, default=8, help="parallel requests (default 8)")
       ap.add_argument("--image-method", choices=["get", "head"], default="get",
                       help="GET downloads (and discards) each image, e.g. to warm a Cantaloupe cache; "
                            "HEAD only checks it resolves")
       ap.add_argument("--info-json", action="store_true",
                       help="also request each image service's info.json")
       args = ap.parse_args()

       session = make_session(args.workers)
       lock = threading.Lock()
       counts = {"ok": 0, "fail": 0}

       out = open(args.output, "w", newline="", encoding="utf-8")
       writer = csv.writer(out)
       writer.writerow(["level", "manifest", "canvas", "url", "status", "ms", "error"])

       def record(level, manifest, canvas, url, status, ms, err):
           with lock:
               writer.writerow([level, manifest, canvas, url, status, ms, err])
               ok = status is not None and 200 <= status < 400
               counts["ok" if ok else "fail"] += 1
               if not ok:
                   print(f"  FAIL [{level}] {status} {url} {err}", file=sys.stderr)

       def process_manifest(murl):
           try:
               r = session.get(murl, timeout=120)
               r.raise_for_status()
               manifest = r.json()
               record("manifest", murl, "", murl, r.status_code, int(r.elapsed.total_seconds() * 1000), "")
           except Exception as e:
               record("manifest", murl, "", murl, getattr(getattr(e, "response", None), "status_code", None), 0, str(e))
               return murl, 0, 0

           pairs = canvases_and_images(manifest)
           services = image_service_ids(manifest) if args.info_json else {}
           tasks = []
           for canvas_id, imgs in pairs:
               tasks.append(("canvas", canvas_id, canvas_id, "get"))
               for img in imgs:
                   tasks.append(("image", canvas_id, img, args.image_method))
                   if img in services:
                       tasks.append(("info.json", canvas_id, services[img].rstrip("/") + "/info.json", "get"))

           with ThreadPoolExecutor(max_workers=args.workers) as pool:
               futs = {pool.submit(probe, session, url, method): (level, cid, url)
                       for level, cid, url, method in tasks}
               for f in as_completed(futs):
                   level, cid, url = futs[f]
                   record(level, murl, cid, url, *f.result())
           n_img = sum(len(i) for _, i in pairs)
           return murl, len(pairs), n_img

       print(f"Reading collection {args.collection}")
       manifest_urls = list(dict.fromkeys(iter_manifest_urls(session, args.collection)))
       print(f"Found {len(manifest_urls)} manifests\n")

       start = time.monotonic()
       for i, murl in enumerate(manifest_urls, 1):
           _, nc, ni = process_manifest(murl)
           print(f"[{i}/{len(manifest_urls)}] {nc} canvases, {ni} images  {murl}")
           out.flush()

       out.close()
       mins = (time.monotonic() - start) / 60
       print(f"\nDone in {mins:.1f} min: {counts['ok']} OK, {counts['fail']} failed -> {args.output}")


   if __name__ == "__main__":
       main()

Step 2: Capture the Image Requests
==================================

Firefox
-------

#. Open Developer Tools and go to the **Network** panel.
#. In the gear menu, enable **Persist Logs**.
#. Check **Disable Cache** so every image shows up as a real request.
#. Load the page and interact with the viewer as the crawl will.
#. Right-click any request and choose **Save All As HAR**. Save the file as
   ``capture.har``.

.. note::

   **Copy All As HAR** also works, but large captures can be truncated when
   pasted from the clipboard. **Save All As HAR** is more reliable.

Chrome
------

#. Open Developer Tools and go to the **Network** panel.
#. Check **Preserve log** and **Disable cache**.
#. Load the page and interact with the viewer.
#. Click the **Export HAR** (download arrow) button and save as
   ``capture.har``.

Step 3: Extract the Image URLs
==============================

Filter on the request URL rather than the response type. Failed requests have
no MIME type, and those are exactly the ones we need to find:

.. code-block:: bash

   jq -r '.log.entries[]
     | select(.request.url | test("\\.jpg(\\?|$)"; "i"))
     | .request.url' capture.har | sort -u > image-urls.txt

To check how many requests the HAR contains before filtering:

.. code-block:: bash

   jq '.log.entries | length' capture.har

If the viewer also requests other formats (for example, ``.png`` or
``.webp``), widen the pattern: ``test("\\.(jpg|png|webp)(\\?|$)"; "i")``.

Step 4: Run the Script
======================

.. code-block:: bash

   chmod +x check-images.sh
   ./check-images.sh image-urls.txt results.csv

The script requests every URL with ``curl``, discards the image data, and
writes one row per URL to ``results.csv``:

.. code-block:: text

   status,time_s,bytes,content_type,url

When it finishes, it prints a count of requests by status code and a list of
every failure.

Options
-------

Options are set as environment variables:

``PARALLEL``
   Number of simultaneous requests. Default ``4``. Keep this modest when
   warming a cache so you don't overload Cantaloupe while it generates
   derivatives.

``TIMEOUT``
   Maximum seconds per request. Default ``60``.

.. code-block:: bash

   PARALLEL=8 TIMEOUT=120 ./check-images.sh image-urls.txt results.csv

The Script
----------

.. code-block:: bash

   #!/usr/bin/env bash
   # Request every URL in a list and record the result.
   #
   # Usage:
   #   ./check-images.sh [input-file] [output-csv]
   #   PARALLEL=20 ./check-images.sh image-urls.txt results.csv
   #
   # Defaults: input = image-urls.txt, output = results.csv, PARALLEL = 4
   # Status 000 means no HTTP response at all (timeout, connection refused/reset, DNS, TLS).

   set -uo pipefail

   input="${1:-image-urls.txt}"
   out="${2:-results.csv}"
   parallel="${PARALLEL:-4}"
   timeout="${TIMEOUT:-60}"

   if [[ ! -f "$input" ]]; then
     echo "Input file not found: $input" >&2
     exit 1
   fi

   echo "status,time_s,bytes,content_type,url" > "$out"

   # Strip blank lines and Windows line endings, dedupe, then fetch in parallel.
   # The body is discarded; only the status and timing are kept.
   grep -v '^[[:space:]]*$' "$input" | tr -d '\r' | sort -u |
     xargs -P "$parallel" -I{} \
       curl -s -o /dev/null --max-time "$timeout" \
         -w '%{http_code},%{time_total},%{size_download},%{content_type},%{url_effective}\n' \
         "{}" >> "$out"

   total=$(( $(wc -l < "$out") - 1 ))
   echo "Checked $total URLs -> $out"
   echo
   echo "By status:"
   awk -F, 'NR>1 {c[$1]++} END {for (s in c) printf "  %s  %d\n", s, c[s]}' "$out" | sort
   echo
   echo "Failures (000 or >= 400):"
   awk -F, 'NR>1 && ($1=="000" || $1+0>=400) {printf "  %s  %ss  %s\n", $1, $2, $5}' "$out"

Step 5: Review the Results
==========================

These apply to ``results.csv`` and to the ``image`` and ``info.json`` rows in
``iiif-results.csv``. In ``iiif-results.csv``, a request with no HTTP response
has an empty ``status`` instead of ``000``.

``200``
   Success. The derivative now exists in the cache.

``000``
   No HTTP response at all: a timeout, a refused or reset connection, or a
   DNS or TLS error. Often these are large derivatives that took longer than
   ``TIMEOUT`` to generate. Rerun them with a longer timeout.

``4xx``
   Usually a bad identifier, an invalid region or size, or a missing source
   image. Check the identifier and Cantaloupe's logs.

``5xx``
   Cantaloupe failed to produce the image. Check its logs for the affected
   identifiers (common causes are unreadable source files, memory limits, or
   unsupported source formats).

Step 6: Verify the Cache, Then Crawl
====================================

Run both scripts a second time:

.. code-block:: bash

   python iiif_crawl.py --info-json --workers 4 -o iiif-results-pass2.csv "<collection URL>"
   ./check-images.sh image-urls.txt results-pass2.csv

Every ``image`` and ``info.json`` row, and every row in
``results-pass2.csv``, should now be ``200``. The ``ms`` and ``time_s`` values
should be much lower than in the first pass. That drop is how you can tell the
derivatives are being served from cache. Once the second pass is clean, run
the Browsertrix crawl.

Troubleshooting
===============

**Everything succeeds in the script but still fails in the browser.**
   ``curl`` and ``requests`` do not enforce CORS, but browsers do. Check that
   Cantaloupe (or the proxy in front of it) sends the right
   ``Access-Control-Allow-Origin`` header.

**Failures appear only at higher concurrency.**
   Try ``PARALLEL=20`` to mimic a viewer requesting many tiles at once. If
   failures appear, look at Cantaloupe's resource limits, ingress or proxy
   timeouts, and any rate limiting.

**Full-size images fail in Step 1 but tiles work.**
   The manifest's image ``@id`` is often a full-size image (``full/full`` or
   ``full/max``). For very large maps, Cantaloupe may refuse these because of
   its ``max_pixels`` or ``max_scale`` limits, or take long enough to generate
   that a proxy times out. If the ``info.json`` rows succeed and the page
   viewer works, these failures may not affect the crawl. Rely on Steps 2
   through 4 for those items.

**Lots of ``404`` responses on canvas rows.**
   Expected for many Presentation 2 manifests. Canvas ``@id`` values are
   identifiers, not necessarily resolvable URLs. See the note under
   `Output`_.

**The second pass is not faster.**
   The derivative cache is probably disabled, expiring too quickly, or using
   a cache location that is not shared across Cantaloupe replicas. Check the
   ``cache.server.derivative`` settings.

**The crawl still has broken tiles after warming.**
   Browsertrix likely requested different tile URLs than the ones you
   captured. Recapture with a browser window closer to the crawler's
   viewport size, interact with the viewer the same way the crawl does, and
   warm again.