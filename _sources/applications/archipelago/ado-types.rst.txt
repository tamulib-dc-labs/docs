========================
ADO Types in Archipelago
========================

Archipelago Digital Objects (ADOs) require a :code:`type` value upon ingest. This tells Archipelago what kind of template to create for that specific object.

Below is a list of TAMU Archipelago worktypes:

----------
Collection
----------

* Metadata:
    * Technical/Structural:
        * Has child ADOs
        * May be part of another collection
    * Descriptive  
        * No unique fields
* Structure:
    * Should have its associated files set up for "collections as data"
    * May have a thumbnail
* Display/viewer
    * None
* File types: jpg (thumbnail)
* Example item: `Brazos Maps <https://archipelago-dev.library.tamu.edu/do/c7d1a1e2-e0a2-43f9-ad52-e67597c714ec>`_

All child ADOs are displayed at the bottom of the page.

.. image:: docs/source/_static/images/exemplar-collection.png
    :alt: Screenshot of a Digital Object Collection ADO.

Things missing from this ADO
    * Collections as data

------------------
CreativeWorkSeries
------------------

* Metadata:
    * Technical/Structural:
        * Has child ADOs in a prescribed order
        * May be part of a collection
    * Descriptive  
        *  No unique fields
* Structure:
    * Should have its associated files set up for "collections as data"
* Display/viewer
    * Mirador - user can scroll through child ADOs
* File types: None
* Example collections:
    * Building History Collection
* Example item: `Bachelor Hall and Buggy House <https://archipelago-dev.library.tamu.edu/do/5524c1f2-de1b-4700-a033-c9d485bf65de#page/1>`_
* Collection vs. CreativeWorkSeries
    * Like a collection, a CreativeWorkSeries displays all ADOs at the bottom of the ADO page.
    * Unlike a Collection, a CreativeWorkSeries includes a Mirador viewer with all ADOs in order. The user can scroll through enlarged ADOs without clicking off the page.
    * Unlike a Collection, a CreativeWorkSeries has no thumbnail.

.. image:: ../_static/images/exemplar-cws-mirador.png
    :alt: Screenshot of the Mirador viewer of a CreativeWorkSeries ADO.

Things missing from this ADO
    * Collections as data

-----
Image
-----

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Descriptive  
        * No unique fields
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * Individual canvases can be downloaded
    * Not paged
* Display/viewer
    * Mirador
* File types: jpg, jp2
* Example collections:
    * WWI Postcards
    * Wheelan Collection
    * Berger Cloonan
* Example item: `Military Parade 1 <https://archipelago-dev.library.tamu.edu/do/a10a570a-4bb1-436b-9209-f195c73d7450>`_

---
Map
---

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Descriptive  
        * Projection
        * Edition of the map / state of the map
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * Not paged
    * May have a watermark
* Display/viewer 
    * Mirador
    * x, y, w, h of the watermark to the original canvas
* File types: jpg, jp2
* Example collections:
    * Brazos Maps
    * WWII Service Maps
* Example item: `Bryan-College Station Bicycle Plan <https://archipelago-dev.library.tamu.edu/do/97c56fb9-3ab7-43ee-9f3c-00e505274076#page/1>`_
* Image vs. Map
    * A Map will be annotated with a watermark, but an Image will not
    * A Map contains unique metadata not included in any other worktype

.. image:: ../_static/images/exemplar-map.png
    :alt: Screenshot of a Map ADO.

Things missing from this exemplar
    * Projection and edition metadata
    * No watermark on this exemplar

----
Book
----

* Metadata:
    * Technical/Structural:
        * Structures and Ranges
        * Checksums for files
    * Descriptive  
        * No unique fields
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * OCR and HOCR or AltoXML for each canvases
    * Entire work can be downloaded as a PDF with OCR embedded
    * Should have its text and associated files set up for "collections as data"
    * Not paged
    * Searchable
* Display/viewer
    * Mirador
* File types: pdf, jpg, jp2
* Image vs. Book
    * A Book has OCR, an Image does not
    * A Book is searchable, an Image is not
    * Users can download an entire Book as a pdf, but Images must be downloaded individually as their original filetype (jpg or jp2).
* Example collections:
    * Yearbooks
    * Committee on South Asian Women
    * Cherokee Freedmen
* Example item: `The Olio <https://archipelago-dev.library.tamu.edu/do/d767aa3a-5f75-48c6-897d-c500cdceb75b#page/128/mode/2up>`_

.. image:: ../_static/images/exemplar-book-search.png
    :alt: Screenshot of the search function on a Book ADO.

Here is the extracted text tab on the book:

.. image:: ../_static/images/exemplar-book-ocr.png
    :alt: Screenshot of the extracted text tab of a Book ADO.

Things missing from this ADO
    * Collections as data
    * PDF for users to download

----------
Manuscript
----------

* Metadata:
    * Technical/Structural:
        * Structures and ranges
        * Checksums for files
    * Descriptive  
        * HTR
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * HTR for each canvas
    * Entire work can be downloaded as a PDF with HTR embedded
    * Should have its text and associated files set up for "collections as data"
    * Not paged
    * Searchable
* Display/viewer
    * Mirador
* File types: pdf, jpg, jp2
* Book vs. Manuscript
    * A Manuscript does not have OCR or Extracted Text
    * A Manuscript has HTR instead
* Example collections
    * AMC Early Presidents
    * Houston Oil Company Minutes
* Example item: `Letter to Louis L. McInnis from H. H. Dinwiddie, August 6, 1887 <https://archipelago-dev.library.tamu.edu/do/7964408b-f800-458a-bffd-cce3d799b0f1#page/1>`_

.. image:: ../_static/images/exemplar-manuscript.png
    :alt: Screenshot of a Manuscript ADO.

Things missing from this ADO
    * HTR
    * Collections as data
    * PDF for users to download

-----------
AudioObject
-----------

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Descriptive  
        * Link to Avalon
* Structure:
    * 1 - n audio files
    * File and transcript can be downloaded
    * Searchable transcript
* Display/viewer
    * Audio player
* File types: mp3, vtt
* Example collections:
    * Science Fiction Radio Show Collection
    * Owens Folk Music
    * Edge Grant Oral Histories
* Example item: `Bill Scott, Forest Ranger: "Forest Aflame" <https://archipelago-dev.library.tamu.edu/do/026b4752-bbf1-4e09-b5e0-28b7a8469e8f>`_

In the example, the audio and transcript are synced and there is a button where the user can download the vtt.

.. image:: ../_static/images/exemplar-audio.png
    :alt: Screenshot of an AudioObject ADO.

The vtt shows up as extracted text.

.. image:: ../_static/images/exemplar-audio-text.png
    :alt: Screenshot of the extracted text of an AudioObject ADO.

-----------
VideoObject
-----------

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Descriptive  
        * Link to Avalon
* Structure:
    * 1 - n video files
    * File and transcript can be downloaded
    * Searchable captions
* Display/viewer
    * Video player
* Example collection:
    * Veterans of the Valley
    * NASA A/V Recordings
* Example item: `Jeff Bailey - part 1 interview <https://archipelago-dev.library.tamu.edu/do/0b220a77-19d6-4695-9645-e00d269b3652>`_

.. image:: ../_static/images/exemplar-video.png
    :alt: Screenshot of a VideoObject ADO.

The vtt shows up as extracted text.

.. image:: ../_static/images/exemplar-video-text.png
    :alt: Screenshot of the extracted text of a Videobject ADO.


--------------
AnnotatedImage
--------------

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Descriptive  
        * No unique fields
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * Entire work can be downloaded as a PDF
    * Not paged
    * Annotated manifest
* Display/viewer
    * Full view
* File types: jpg, jp2, must be imported through IIIF
* AnnotatedImage vs. Image
    * Image opens in Mirador, AnnotatedImage opens in Full view
    * AnnotatedImage is part of a CreativeWorkSeries
* Example item: `Downs Natatorium in 1980 <https://archipelago-dev.library.tamu.edu/do/f4edce17-70fe-4ad3-8866-fff14c4af653>`_

-------------
MetadataOnly
-------------

* Metadata:
    * Technical/Structural:
    * Descriptive  
        * url to item
* Structure:
    * Searchable transcript/captions (or nothing)
* Display/viewer
    * None
* File types: vtt if this is audio/video hosted on Avalon
* Example collection:
    * Dallas Women's Gallery
* Example item: `Interview with Ann Stautberg <https://archipelago-dev.library.tamu.edu/do/792b193a-7d28-41db-b5b0-7878ddfa1f57>`_

The user can download supplemental files but not the file the metadata is about.

.. image:: ../_static/images/exemplar-metadataonly-vtts.png
    :alt: Screenshot of a MetadataOnly ADO menu allowing the user to download two vtts.

In this exemplar, the vtts are used to create extracted text, similar to that of a VideoObject or AudioObject.

.. image:: ../_static/images/exemplar-metadataonly-text.png
    :alt: Screenshot of the extracted text of a MetadataOnly ADO.

-------
WebPage
-------

* Metadata:
    * Technical/Structural:
    * Descriptive  
        * url from orginal site
* Structure:
    * Searchable
* Display/viewer
    * WARC Replay.web Widget
* File types: wacz, warc
* Example collection:
    * OJS Journals
    * Archived exhibits
* Example item: `AAVPT Biennial Symposia <https://archipelago-dev.library.tamu.edu/do/6b86bd2a-8212-4d3c-8788-3100e9249f33#url=https%3A%2F%2Faavptbiennial-ojs-tamu.tdl.org%2Faavptbiennial&ts=20251205202838>`_
* MetadataOnly vs. WebPage 
    * While both MetadataOnly and WebPage require a link to another site, WebPage is intended for archived sites and MetadataOnly is more of a tool for discoverability
    * WebPage opens a viewer so the user can navigate the site inside Archipelago
    * WebPage asks the user to upload a warc, not just entering a link.

The user can navigate the site in the viewer as if it were the original website

.. image:: ../_static/images/exemplar-webpage.png
    :alt: Screenshot of a WebPage ADO.

In the metadata, the URL of the original site must be included: 

.. image:: ../_static/images/exemplar-webpage-metadata.png
    :alt: Screenshot of the metadata of a WebPage ADO.