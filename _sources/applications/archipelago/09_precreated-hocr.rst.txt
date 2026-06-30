=====================================
Uploading Pre-Created HOCR with Books
=====================================

When uploading a book-like object as a Creative Works Series (CWS), Archipelago can use
pre-created HOCR files instead of regenerating OCR with Tesseract. This is useful when you
already have high-quality HOCR output and want to avoid the time cost of reprocessing.

.. note::

   HOCR (HTML OCR) is an open standard for encoding the results of OCR in HTML format. Each HOCR
   file represents a single page and contains the recognized text along with bounding-box
   coordinates for every word.

------------------
How Matching Works
------------------

Archipelago does **not** match HOCR files to page images by file name (not exactly). Instead, it matches them
by **image dimensions**. When the OCR post-processor (Strawberry Runners) processes a page image,
it:

1. Reads the pixel width and height of the image.
2. Searches through all files stored under ``as:text`` in the ADO's JSON for files with
   MIME type ``text/html`` (keep this in mind as filename could affect this).
3. For each candidate, it checks that the HTML file is a valid HOCR page (the top-level
   ``<div>`` must have ``class="ocr_page"``).
4. It reads the ``bbox`` value from that div's ``title`` attribute
   (e.g. ``bbox 0 0 6312 9055``) and extracts the width and height.
5. If the bbox dimensions **exactly match** the image dimensions, Archipelago uses that
   HOCR file instead of running Tesseract.

If no matching HOCR is found, Tesseract runs as normal.

.. warning::

   Because matching is dimension-based, if multiple pages in your book share the **same pixel
   dimensions**, only the **first** HOCR file with those dimensions will be used and it will
   be applied to every page that shares those dimensions. This is why we must do things as a
   ``digita_collections_object``. For books where all pages are the same
   size, this means pre-created HOCR will not work as expected page-by-page. Dimension-based
   matching is most reliable when pages have unique sizes (e.g. mixed-format items or when each
   page image has been cropped differently).

---------------------------
Requirements for HOCR Files
---------------------------

For Archipelago to recognize and use a pre-created HOCR file, it must meet the following
requirements:

* **File extension:** ``.html`` (not ``.hocr``). The extension must produce a ``text/html``
  MIME type so the file is stored in ``as:text`` during ingest.
* **HOCR structure:** The file must be valid HOCR (XHTML). The ``<body>`` must contain a
  ``<div>`` with ``class="ocr_page"`` and a ``title`` attribute containing a ``bbox`` that
  matches the source image dimensions exactly. Example::

      <div class='ocr_page' title='image "/path/to/page.tif"; bbox 0 0 2550 3300; ppageno 0'>

* **Dimensions match exactly:** The bbox width and height must be integer-identical to the
  image's pixel dimensions. Off-by-one errors will cause the match to fail and Tesseract
  will run instead.
* **File name:** The file name does not affect matching. You may name the files anything
  you like, but a consistent convention such as ``page_0001.html``, ``page_0002.html``, etc.
  is recommended for your own organization.

-----------------------------------------
AMI Set Configuration
-----------------------------------------

When creating the AMI set, the HOCR files must be referenced in the correct column so they are
ingested as ``as:text`` (not ``as:image`` or ``as:document``). Follow these steps:

1. In your AMI CSV, add a column for text files (commonly called ``documents`` or ``texts``
   depending on your local spreadsheet template). List each HOCR ``.html`` filename in that
   column, separated by semicolons if there are multiple::

       https://some-server.edu/page_0001.html;https://some-server.edu/page_0002.html;https://some-server.edu/page_0003.html

   The page images go in the ``images`` column as usual.

2. When creating the AMI set (step 5 of the AMI upload process), make sure the text column
   is included in the list of selected file columns alongside the images column.

3. After ingest, Archipelago will classify the ``.html`` files as ``as:text`` (because their
   MIME type is ``text/html``) and the images as ``as:image``. When Strawberry Runners processes
   each page image, it will find the matching HOCR by dimension and skip Tesseract.

.. tip::

   After ingest, you can verify that HOCR files were stored under ``as:text`` by viewing the
   raw JSON of the ADO (``/node/<id>/edit`` → Strawberry field → view raw). Look for an
   ``as:text`` key containing entries with ``"dr:mimetype": "text/html"`` and
   ``"flv:exif": { "HtmlBodyDivClass": "ocr_page", ... }``.
