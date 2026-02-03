========================
ADO Types in Archipelago
========================

Archipelago Digital Objects (ADOs) require a :code:`type` value upon ingest. This tells Archipelago what kind of template to create for that specific object.

Below is a list of TAMU Archipelago worktypes:

----------
Collection
----------

* Parent object, has child ADOs.

* Has description that applies to all child objects

* Has a summary that only appears on Collection page

* May be part of another collection

* Thumbnail

* No viewer

--------------------
Creative Work Series
--------------------

* Parent object, has child ADOs.

* May be part of a collection

* Child objects open in Mirador in a prescribed order

* Examples: Building History Collection, Bulletin/Committee on South Asian Women Collection

----
Book
----

* OCR/HOCR

* 1-n canvases

* Typed

* Opens in Mirador

* File types: pdf, jpg, jp2

* Examples: Yearbooks, Yellbooks

-----
Image
-----

* 1-n canvases

* Opens in Mirador

* File types: jpg, jp2

* Examples: Wheelan, Berger-Cloonan

-----------
Web Archive
-----------

* Metadata: url from original site.

* User can navigate the site inside the viewer

* File type: wacz, warc

* Example: AAVPT Biennial Symposia

----------
Manuscript
----------

* Transcribed text

* 1-n canvases

* Handwritten

* Opens in Mirador

* File types: jpg, jp2

* Example: AMC Early Presidents

---
Map
---

* 1-n canvases

* May be very large files

* Opens in Mirador

* File types: jpg, jp2

* Example: Brazos Maps, London Maps


-----------
AudioObject
-----------

* Opens in audio player

* Includes synced vtt transcript

* Metadata: url from Avalon object

* File types: mp3

* Examples: Science Fiction Radio Show, Owens Folk Music

-----------
VideoObject
-----------

* Opens in video player

* Includes synced captions

* Metadata: url from Avalon object

* File types: mp4

* Example: Veterans of the Valley

-----------------
Annotatable Image
-----------------

* Opens in default viewer

* 1-n canvases

* IIIF manifest has annotations

* File types: jpg, jp2, must be imported through IIIF

* Example: Building History, WWII Service Maps

-------------
Metadata Only
-------------

* No image/audio/video/document

* File types: none

* Example: Amazing, Fascinating, Weird: Science Fiction in Texas, Dallas Women's Gallery