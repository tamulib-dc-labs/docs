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

* Example item: `Brazos Maps <https://archipelago-dev.library.tamu.edu/do/c7d1a1e2-e0a2-43f9-ad52-e67597c714ec>`_

--------------------
Creative Work Series
--------------------

* Parent object, has child ADOs.

* May be part of a collection

* Child objects open in Mirador in a prescribed order

* Examples: Building History Collection, Bulletin/Committee on South Asian Women Collection

* Example item: `Bachelor Hall and Buggy House <https://archipelago-dev.library.tamu.edu/do/5524c1f2-de1b-4700-a033-c9d485bf65de#page/1>`_

----
Book
----

* OCR/HOCR

* 1-n canvases

* Typed

* Opens in Mirador

* File types: pdf, jpg, jp2

* Examples: Yearbooks, Yellbooks

* Example item: `The Olio <https://archipelago-dev.library.tamu.edu/do/d767aa3a-5f75-48c6-897d-c500cdceb75b#page/128/mode/2up>`_

-----
Image
-----

* 1-n canvases

* Opens in Mirador

* File types: jpg, jp2

* Examples: Wheelan, Berger-Cloonan

* Example item: `Military Parade 1 <https://archipelago-dev.library.tamu.edu/do/a10a570a-4bb1-436b-9209-f195c73d7450>`_

-----------
Web Archive
-----------

* Metadata: url from original site.

* User can navigate the site inside the viewer

* File type: wacz, warc

* Example: AAVPT Biennial Symposia

* Example item: `AAVPT Biennial Symposia <https://archipelago-dev.library.tamu.edu/do/6b86bd2a-8212-4d3c-8788-3100e9249f33#url=https%3A%2F%2Faavptbiennial-ojs-tamu.tdl.org%2Faavptbiennial&ts=20251205202838>`_

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

* Example item: `Bryan-College Station Bicycle Plan <https://archipelago-dev.library.tamu.edu/do/97c56fb9-3ab7-43ee-9f3c-00e505274076#page/1>`_

-----------
AudioObject
-----------

* Opens in audio player

* Includes synced vtt transcript

* Metadata: url from Avalon object

* File types: mp3

* Examples: `Bill Scott, Forest Ranger: "Forest Aflame" <https://archipelago-dev.library.tamu.edu/do/026b4752-bbf1-4e09-b5e0-28b7a8469e8f>`_

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

* File types: may have a vtt or pdf if the metadata is for audio/video

* Example: Dallas Women's Gallery

-----------------
Downloadable File
-----------------

* No viewer

* User is expected to download the file from the dropdown

* Clear direction on the site so the user knows how to view the file

* Example: Amazing, Fascinating, Weird: Science Fiction in Texas