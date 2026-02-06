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
* File types: None, except maybe a jpg thumbnail
* Example item: `Brazos Maps <https://archipelago-dev.library.tamu.edu/do/c7d1a1e2-e0a2-43f9-ad52-e67597c714ec>`_

At the bottom, the user can see all child ADOs.

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
        * No unique fields
* Structure:
    * Should have its associated files set up for "collections as data"
* Display/viewer
    * Mirador - user can scroll through child ADOs
* File types: None
* Example item: `Bachelor Hall and Buggy House <https://archipelago-dev.library.tamu.edu/do/5524c1f2-de1b-4700-a033-c9d485bf65de#page/1>`_

At the bottom, the user can see all child ADOs.

.. image:: ../_static/images/exemplar-cws.png
    :alt: Screenshot of a CreativeWorkSeries ADO.

Up close, the user can see the Mirador viewer with all ADOs in order.

.. image:: ../_static/images/exemplar-cws-mirador.png
    :alt: Screenshot of the Mirador viewer of a CreativeWorkSeries ADO.

Things missing from this ADO
    * Collections as data

----
Book
----

* Metadata:
    * Technical/Structural:
        * Structures and Ranges
        * Checksums for files
    * Descriptive  
        * Author, Illustrator, Editor (can be added using creator roles)
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
* Example item: `The Olio <https://archipelago-dev.library.tamu.edu/do/d767aa3a-5f75-48c6-897d-c500cdceb75b#page/128/mode/2up>`_

.. image:: ../_static/images/exemplar-book.png
    :alt: Screenshot of a Book ADO.

Here is the extracted text tab on the book:

.. image:: ../_static/images/exemplar-book-ocr.png
    :alt: Screenshot of the extracted text tab of a Book ADO.

Things missing from this ADO
    * Collections as data
    * PDF for users to download

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
* Example item: `Military Parade 1 <https://archipelago-dev.library.tamu.edu/do/a10a570a-4bb1-436b-9209-f195c73d7450>`_

.. image:: ../_static/images/exemplar-image.png
    :alt: Screenshot of an Image ADO.

Here is the metadata, showing repeatable fields: 

.. image:: ../_static/images/exemplar-image-metadata.png
    :alt: Screenshot of the metadata of an Image ADO.

Here is the linked data: 

.. image:: ../_static/images/exemplar-image-linkeddata.png
    :alt: Screenshot of the linked data of an Image ADO.

-------
WebPage
-------

* Includes archived exhibits
* Metadata:
    * Technical/Structural:
    * Descriptive  
        * url from orginal site
* Structure:
    * Searchable
* Display/viewer
    * WARC Replay.web Widget
* File types: wacz, warc
* Example item: `AAVPT Biennial Symposia <https://archipelago-dev.library.tamu.edu/do/6b86bd2a-8212-4d3c-8788-3100e9249f33#url=https%3A%2F%2Faavptbiennial-ojs-tamu.tdl.org%2Faavptbiennial&ts=20251205202838>`_

The user can navigate the site in the viewer as if it was the original website

.. image:: ../_static/images/exemplar-webpage.png
    :alt: Screenshot of a WebPage ADO.

In the metadata, the URL of the original site must be included: 

.. image:: ../_static/images/exemplar-webpage-metadata.png
    :alt: Screenshot of the metadata of a WebPage ADO.

----------
Manuscript
----------

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Descriptive  
        * No unique fields
* Structure:
    * Multiple High Resolution Images as Canvases
    * 1 to n canvases
    * HTR for each canvases
    * Entire work can be downloaded as a PDF with OCR embedded
    * Should have its text and associated files set up for "collections as data"
    * Not paged
    * Searchable
* Display/viewer
    * Mirador
* File types: pdf, jpg, jp2
* Example item: `Letter to Louis L. McInnis from H. H. Dinwiddie, August 6, 1887 <https://archipelago-dev.library.tamu.edu/do/7964408b-f800-458a-bffd-cce3d799b0f1#page/1>`_

.. image:: ../_static/images/exemplar-manuscript.png
    :alt: Screenshot of a Manuscript ADO.

Things missing from this ADO
    * HTR
    * Collections as data
    * PDF for users to download

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
* Example item: `Bryan-College Station Bicycle Plan <https://archipelago-dev.library.tamu.edu/do/97c56fb9-3ab7-43ee-9f3c-00e505274076#page/1>`_

.. image:: ../_static/images/exemplar-map.png
    :alt: Screenshot of a Map ADO.

Things missing from this exemplar
    * Projection and edition metadata
    * No watermark on this exemplar

-----------
AudioObject
-----------

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Descriptive  
        * No unique fields
* Structure:
    * 1 - n audio files
    * File and transcript can be downloaded
    * Searchable transcript
* Display/viewer
    * Audio player
* File types: mp3, vtt
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
        * No unique fields
* Structure:
    * 1 - n video files
    * File and transcript can be downloaded
    * Searchable captions
* Display/viewer
    * Video player
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
* Example item: `Interview with Ann Stautberg <https://archipelago-dev.library.tamu.edu/do/792b193a-7d28-41db-b5b0-7878ddfa1f57>`_

In this MetadataOnly ADO, the URL points to the item hosted on Avalon.

.. image:: ../_static/images/exemplar-metadataonly.png
    :alt: Screenshot of a MetadataOnly ADO.

The user can download both vtts but not the video file itself.

.. image:: ../_static/images/exemplar-metadataonly-vtts.png
    :alt: Screenshot of a MetadataOnly ADO menu allowing the user to download two vtts.

These vtts are used to create extracted text, similar to that of a VideoObject or AudioObject.

.. image:: ../_static/images/exemplar-metadataonly-text.png
    :alt: Screenshot of the extracted text of a MetadataOnly ADO.

-----------------
DownloadableFile
-----------------

* Metadata:
    * Technical/Structural:
        * Checksums for files
    * Descriptive  
        * No unique fields
* Structure:
    * 1 - n files
    * Searchable
* Display/viewer
    * None
    * Clear instructions to download the file
* File types: ppt, pptx
* Example item: `Race in Fandom: Experiences from the Margins <https://archipelago-dev.library.tamu.edu/do/fee8fad9-8916-4ad7-aa3f-256a54024e4e>`_

Powerpoints are not compatible with any Archipelago media viewer. Therefore, this powerpoint needs to be downloaded by the user.

.. image:: ../_static/images/exemplar-downloadable.png
    :alt: Screenshot of a DownloadableFile ADO.

The user must use the Download menu to download the file. It does not show up in the player.

.. image:: ../_static/images/exemplar-downloadable.png
    :alt: Screenshot of a DownloadableFile ADO menu allowing the user to download a powerpoint.

Things missing from this exemplar
    * Message explaining how to download