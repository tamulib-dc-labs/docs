========================
ADO Types in Archipelago
========================

Archipelago Digital Objects (ADOs) require a :code:`type` value upon ingest. This tells Archipelago what kind of template to create for that specific object.

Below is a list of TAMU Archipelago worktypes:

----------
Collection
----------

* Parent object, has child ADOs.

* Has metadata that only appears on Collection page

* May be part of another collection

* Thumbnail

* No viewer

* Example item: `Brazos Maps <https://archipelago-dev.library.tamu.edu/do/c7d1a1e2-e0a2-43f9-ad52-e67597c714ec>`_

------------------
CreativeWorkSeries
------------------

* Parent object, has child ADOs.

* May be part of a collection

* Child objects open in Mirador in a prescribed order

* Example item: `Bachelor Hall and Buggy House <https://archipelago-dev.library.tamu.edu/do/5524c1f2-de1b-4700-a033-c9d485bf65de#page/1>`_

----
Book
----

* OCR/HOCR

* 1-n canvases

* Typed

* Opens in Mirador

* File types: pdf, jpg, jp2

* Example item: `The Olio <https://archipelago-dev.library.tamu.edu/do/d767aa3a-5f75-48c6-897d-c500cdceb75b#page/128/mode/2up>`_

-----
Image
-----

* 1-n canvases

* Opens in Mirador

* File types: jpg, jp2

* Example item: `Military Parade 1 <https://archipelago-dev.library.tamu.edu/do/a10a570a-4bb1-436b-9209-f195c73d7450>`_

-------
WebPage
-------

* Metadata: url from original site.

* User can navigate the site inside the viewer

* File type: wacz, warc

* Example item: `AAVPT Biennial Symposia <https://archipelago-dev.library.tamu.edu/do/6b86bd2a-8212-4d3c-8788-3100e9249f33#url=https%3A%2F%2Faavptbiennial-ojs-tamu.tdl.org%2Faavptbiennial&ts=20251205202838>`_

----------
Manuscript
----------

* HTR on handwritten text

* 1-n canvases

* Opens in Mirador

* File types: jpg, jp2

* Example item: `Letter to Louis L. McInnis from H. H. Dinwiddie, August 6, 1887 <https://archipelago-dev.library.tamu.edu/do/7964408b-f800-458a-bffd-cce3d799b0f1#page/1>`_

---
Map
---

* 1-n canvases

* May be very large files

* Opens in Mirador

* File types: jpg, jp2

* Example item: `Bryan-College Station Bicycle Plan <https://archipelago-dev.library.tamu.edu/do/97c56fb9-3ab7-43ee-9f3c-00e505274076#page/1>`_

-----------
AudioObject
-----------

* Opens in audio player

* Includes synced transcript

* File types: mp3, vtt

* Example item: `Bill Scott, Forest Ranger: "Forest Aflame" <https://archipelago-dev.library.tamu.edu/do/026b4752-bbf1-4e09-b5e0-28b7a8469e8f>`_

-----------
VideoObject
-----------

* Opens in video player

* Includes synced captions

* File types: mp4, vtt

* Example item: `Jeff Bailey - part 1 interview <https://archipelago-dev.library.tamu.edu/do/0b220a77-19d6-4695-9645-e00d269b3652>`_

--------------
AnnotatedImage
--------------

* Opens in default viewer

* 1-n canvases

* IIIF manifest has annotations

* File types: jpg, jp2, must be imported through IIIF

* Example item: `Downs Natatorium in 1980 <https://archipelago-dev.library.tamu.edu/do/f4edce17-70fe-4ad3-8866-fff14c4af653>`_
-------------
MetadataOnly
-------------

* No viewer

* File types: vtt if this is audio/video hosted on Avalon

* If there is a transcript/caption, it is not intended for users to download but is only included for discoverability

* Example item: `Interview with Ann Stautberg <https://archipelago-dev.library.tamu.edu/do/792b193a-7d28-41db-b5b0-7878ddfa1f57>`_

-----------------
DownloadableFile
-----------------

* No viewer

* File types: ppt, pptx

* User is expected to download the file from the dropdown

* Clear direction on the site so the user knows how to view the file

* Example item: `Race in Fandom: Experiences from the Margins <https://archipelago-dev.library.tamu.edu/do/fee8fad9-8916-4ad7-aa3f-256a54024e4e>`_