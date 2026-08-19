========================
ADO Types in Archipelago
========================

Archipelago Digital Objects (ADOs) require a :code:`type` value upon ingest. This tells Archipelago what kind of template to create for that specific object.

Note that this list is subject to change as we work with more collections.

Below is a list of TAMU Archipelago worktypes:

----------
Collection
----------

* Metadata:
    * Technical/Structural:
        * Has child ADOs
        * May be part of another collection
    * Descriptive:
        * May have "about_collection"
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object Collection
* Structure:
    * Should have its associated files set up for "collections as data"
    * May have a thumbnail
* Display/viewer
    * No viewer
    * Includes 50 hyperlinked child ADO thumbnails at the bottom of the page
* File types: jpg (thumbnail)
* Example item: `Raiford Stripling Architecture Collection <https://digitalcollections.library.tamu.edu/do/1f3911b8-70ac-42ea-8dbf-60bb18430467>`_

------------------
CreativeWorkSeries
------------------

* Metadata:
    * Technical/Structural:
        * Has child ADOs in a prescribed order
        * May be part of a collection
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object Collection
* Structure:
    * Should have its associated files set up for "collections as data"
    * May have a thumbnail
* Display/viewer
    * Clover - user can scroll through child ADOs
    * Includes 25 hyperlinked child ADO thumbnails at the bottom of the page
* File types: any
* Example collections:
    * Building History Collection
* Example item: `Austin Hall <https://digitalcollections.library.tamu.edu/do/0f70681c-39ba-41cd-87bc-65b11b82eb80>`_

-----
Image
-----

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * Individual canvases can be downloaded
* Display/viewer
    * Clover
* File types: jpg, jp2
* Example collections:
    * WWI Postcards
    * Wheelan Collection
    * Berger Cloonan
* Example item: `Woman Fills a Syringe with a Fluid, number 2 <https://digitalcollections.library.tamu.edu/do/2147aee4-69b7-49ca-ac8f-f0e183ddd35b>`_

---
Map
---

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Descriptive  
        * Projection
        * Edition of the map / state of the map
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * May have watermarks
* Display/viewer 
    * Clover
    * x, y, w, h of the watermark to the original canvas
    * Canvases might be named using "canvas_labels" field
    * May have "Georeference" tab
* File types: jpg, jp2
* Example collections:
    * Brazos Maps
    * WWII Service Maps
* Example item: `Aeneae Troiani navigatio <https://digitalcollections.library.tamu.edu/do/de282a68-3667-42e5-90f7-087f33597779>`_

----
Book
----

* Metadata:
    * Technical/Structural:
        * Structures and Ranges
        * Checksums for files
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
        * Strawberry (Descriptive Metadata source) for Digital Object Collection
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * OCR and HOCR or AltoXML for each canvases
    * Entire work can be downloaded as a PDF with OCR embedded
    * Should have its text and associated files set up for "collections as data"
    * Searchable
* Display/viewer
    * Clover
* File types: pdf, jpg, jp2
* Example collections:
    * Yearbooks
    * Committee on South Asian Women
    * Cherokee Freedmen
* Example items: 
    * Digital Object Collection: `Committee on South Asian Women Newsletter Vol. 5, No. 1-2 <https://digitalcollections.library.tamu.edu/do/dcbd0593-69cd-4449-9244-dd5e3b76c742>`_
    * Digital Object: `Worlds imagined: the Maps of Imaginary Places Collection <https://digitalcollections.library.tamu.edu/do/c457673b-230b-4237-acee-33ccdb666496>`_

----
Page
----

* Metadata:
    * Technical/Structural:
        * Structures and Ranges
        * Checksums for files
    * Descriptive  
        * ispartof (must always be part of a Book)
        * sequence_id
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
* Structure:
    * Single High Resolution Image as Canvas
    * 1 canvas
    * OCR and HOCR or AltoXML for each canvases
    * Downloadable
    * Should have its text and associated files set up for "collections as data"
    * Searchable
* Display/viewer
    * Clover
* File types: jpg, jp2
* Example collections:
    * Yearbooks
    * Committee on South Asian Women
* Example items: 
    * `Page 2 of Committee on South Asian Women Newsletter Vol. 5, No. 1-2 <https://digitalcollections.library.tamu.edu/do/f2c1cc63-e88c-42a6-bed8-bc0f696a4d25>`_

----------
Manuscript
----------

* Metadata:
    * Technical/Structural:
        * Structures and ranges
        * Checksums for files
    * Descriptive  
        * transcription in the "annotations" metadata field
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
        * Strawberry (Descriptive Metadata source) for Digital Object Collection
* Structure:
    * Single High Resolution Image as Canvas
    * 1 canvas
    * HTR for each canvas
    * Entire work can be downloaded as a PDF with HTR embedded
    * Should have its text and associated files set up for "collections as data"
    * Searchable
    * Metadata Bundle: Should always be "Strawberry (Descriptive Metadata source) for Digital Object"
* Display/viewer
    * Clover
* File types: jpg, jp2
* Example collections
    * AMC Early Presidents
    * Houston Oil Company Minutes
* Example item: 
    * `Letter from L. S. Ross to 'Major,' July 23, 1887 <https://digitalcollections.library.tamu.edu/do/abf26637-87df-4169-a856-6b86ffb4673e>`_

----
Leaf
----

* Metadata:
    * Technical/Structural:
        * Structures and ranges
        * Checksums for files
    * Descriptive  
        * transcription in the "annotations" metadata field
        * ispartof (must always be part of a Manuscript)
        * sequence_id
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * HTR for each canvas
    * Entire work can be downloaded as a PDF with HTR embedded
    * Should have its text and associated files set up for "collections as data"
    * Searchable
* Display/viewer
    * Clover
* File types: jpg, jp2
* Example collections
    * AMC Early Presidents
    * Houston Oil Company Minutes
* Example item: 
    * `Page 4 of Minutes of Houston Oil Company of Texas <https://digitalcollections.library.tamu.edu/do/c44f420c-b981-4416-a23f-fca53bac6349>`_

-----------
AudioObject
-----------

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
* Structure:
    * 1 - n audio files
    * File and transcript can be downloaded
    * Searchable, synced vtt transcript
* Display/viewer
    * Audio player
* File types: mp3, opus, vtt
* Example collections:
    * Basbanes Collection
    * Los Palabristas
* Example item: `Bill Scott, Forest Ranger: "Forest Aflame" <https://archipelago-dev.library.tamu.edu/do/026b4752-bbf1-4e09-b5e0-28b7a8469e8f>`_

-----------
VideoObject
-----------

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
* Structure:
    * 1 - n video files
    * File and transcript can be downloaded
    * Searchable captions
* Display/viewer
    * Video player
* Example collection:
    * Music Activities Collection
* Example item: `Jeff Bailey - part 1 interview <https://archipelago-dev.library.tamu.edu/do/0b220a77-19d6-4695-9645-e00d269b3652>`_

-----------
StreamingVideo
-----------

* Metadata:
    * Technical/Structural:
        * Checksums for files
        * Video file migrated from Avalon using "iiifmanifest" metadata field
    * Descriptive  
        * Link to Avalon
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
* Structure:
    * 1 - n audio files
    * File and transcript can be downloaded
    * Searchable, synced vtt transcript
* Display/viewer
    * Audio player
* File types: mp3, opus, vtt
* Example collections:
    * Veterans of the Valley
    * Oral Histories Collection
* Example item: `Spec Gammon: Interview: "Forest Aflame" <https://digitalcollections.library.tamu.edu/do/282d54ca-5bee-4833-a569-a3f6ad8c6f7d>`_

-------
WebPage
-------

* Metadata:
    * Technical/Structural:
    * Descriptive  
        * url from orginal site
    * Bundle
        * Strawberry (Descriptive Metadata source) for Digital Object
* Structure:
    * Searchable
* Display/viewer
    * WARC Replay.web Widget
* File types: wacz, warc
* Example collection:
    * OJS Journals
    * Archived exhibits
* Example item: `1940s Brazos County Aerial Photographs <https://digitalcollections.library.tamu.edu/do/1b4af164-3a6a-4ef9-bf52-e0529bc0afbc#view=pages>`_