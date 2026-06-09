=============================
Cultural Heritage Collections
=============================

-----
About
-----

This section describes our cultural heritage collections, infrastructure, and long term plans.

-------------------------------------------------------------------------
150 Years and Counting: Celebrating 150 Years of the City of Bryan, Texas
-------------------------------------------------------------------------

About
=====

* **Homepage**: `Bryan 150 Exhibit <https://spotlight.library.tamu.edu/spotlight/bryan-150-exhibit>`_
* **Item Count**: 26 Works
* **Available on Digital Collections Page**: Yes
* **Curator**: Unclear

Current Stack
=============

* Fedora for Digital Asset Management
* iriiifservice for IIIF Presentation
* Delivery via Spotlight
* `StoryMaps (ArcGIS): for Georeferencing and Story Telling <https://storymaps.arcgis.com/stories/8f7ea1d1287c4a23be85cd1d363ad868>`_

Migration Plans
===============

* Archipelago for Digital Asset Management
* Exhibit Updated to Pull from Archipelago
* ADO Model: Image

Before Migration
================

* Add Georeferencing to `Migration Metadata <https://github.com/tamulib-dc-labs/charon-crossing/blob/main/ami_output/bryan-150_ami.csv>`_

--------------------------------------
1940s Brazos County Aerial Photographs
--------------------------------------

About
=====

This collections consists of a series of aerial photographs that have been indexed using a highway map from 1980. The images themselves appear to be flat JPGs with no image server.

The primary access point is an image map split into 3 regions. Once you click on a specific region, a new image map appears. Clicking on each image map renders the corresponding jpg in the window.

* **Homepage**: `1940s Brazos County Aerial Photographs <https://library.tamu.edu/collections/maps/brazos-maps.php>`_
* **Curator**: Unclear

Current Stack
=============

* No digital asset management system
* JPEGs are flat files on a library server with the subdomain `webassets <https://webassets.library.tamu.edu/public/files/exhibits/Maps-GIS/Brazos%20Co%20Aerials/40_clb5_78b.jpg>`_
* An annotated bitmap image split into thirds links the satellite views to the corresponding region
* There is no metadata

Migration Plans
===============

* Archipelago for Digital Asset Management
* Exhibit Updated to Pull from Archipelago
* Exhibit will Include a Newly Updated Map but will use Leaflet similar to Woellhof
* ADO Model: Map

Before Migration
================

* Image Assets need a descriptive metadata record
* The record needs to have georeferencing information
* Rights can be NKC or something like that unless we no for sure it should be NC
* Images have dates.  Can get that easily with Computer Vision
* Can also use Identifier Data in Upper right for Title
* Since no metadata record, easiest to start with a blank AMI set in special collections

-----------------------------------------------------------
Amazing, Fantastic, Weird: Science Fiction Studies in Texas
-----------------------------------------------------------

About
=====

This is a collection of program and proceedings from the exhibit opening of: One Hundred Years Hence: Science Fiction and Fantasy at Texas A & M. It consists of PDFs, Powerpoints, etc. This is a complex collection that I need to learn more about. It doesn’t fit easily into a IIIF framework.

* **Homepage**: `<https://oaktrust.library.tamu.edu/handle/1969.1/92159>`_
* **Curator**: Jeremy Brett

Current Stack
=============

* DSPACE

Migration Plans
===============

* Archipelago for Digital Asset Management
* ADO Model: Book

Before Migration
================

* Convert Items (PPTX) to Web Accessible Formats

---------------------------
A.M.C. Yell Book Collection
---------------------------

About
=====

The Agricultural and Mechanical College of Texas Yell Book Online Collection consists of bound Yell Books dating from 1904-1905 through 1931-1932. Included in the booklets are yells and songs that reflect the unique experience of cadets during this period, and the businesses that supported the printing of the booklets. Most of the booklets in this collection were owned by former students, so names, doodles, and in some cases homemade yells can be seen on the covers and within the booklets’ pages.

This is served with the Internet Archive Bookreader Application thus some assumptions are made about stack.

* **Homepage**: https://library.tamu.edu/collections/digital-library/yell_books.php
* Page turning via Internet Archive Bookreader
* Search inside

Current Stack
=============

* Internet Archive Bookreader
* Pages are Bundled
* Text is Alto

Migration Plans
===============

* Archipelago for Digital Asset Management
* ADO Model: Book or CWS with Page so we can programatically add text

Before Migration
================

* Convert Alto to HOCR

--------------------------
Austin's 1830 Map of Texas
--------------------------

About
=====

This first edition of Stephen F. Austin’s 1830 Map of Texas is often described as “the first meaningful map of Texas” and was the first to accurately depict the rivers in Texas and illustrate many of the early settlements including Brazoria, Gonzales, Harrisburg, Matagorda, Victoria and Waco Village.

This map was published in eight editions through 1845 and is the first map of Texas printed in the United States. The map was produced as part of a land grant agreement with the Mexican government but it was also intended to be a showcase for new settlers to Texas. Therefore, it was made to be as open and as inviting as possible.

The map is split into 7 parts and each part is presented independently from the other parts.

There is a Georeferenced data package that is served over HTTP from OAKTrust and thus blocked. This should minimally be switched to HTTPS.

* **Homepage**: https://spotlight.library.tamu.edu/spotlight/austin-map

Current Stack
=============

* DSPACE
* Spotlight
* OAKTrust for Georeferenced Dataset


Migration Plans
===============

* Archipelago for Digital Asset Management
* ADO Model: Map

Before Migration
================

* Figure out what to do with georeferenced dataset.  Can we leverage work done there already?

-------------------------------------------------
The Berger-Cloonan Collection of Decorated Papers
-------------------------------------------------

About
=====

The Berger-Cloonan Collection of Decorated Papers contains more than 20,000 items representing five centuries of paper production and decoration from across the globe and is one of the most extensive collections of its kind. Among its many strengths are eighteenth-century Dutch gilt papers, thousands of unique marbled and paste papers, Japanese Chiyogami and Katazome, historic watermarks, and scores of papermakers’ sample books.

The collection was built by Dr. Sidney E. Berger and Dr. Michèle V. Cloonan in support of their research and teaching interests, and was acquired by Texas A&M University Libraries in 2016. This digital collection contains non-copyrighted papers in the Berger-Cloonan Collection. It is offered here as a starting point for students and researchers who wish to become acquainted with the collection. Digitization of the collection is ongoing, and high-resolution scans of papers will be uploaded as they become available.

Each work is served as a single canvas with manifests.

There are no context pages and only an index.

* Homepage: https://library.tamu.edu/discovery/discovery-context/berger-cloonan?direction=ASC

Current Stack
=============

* SAGE
* Fedora
* Some items are restricted

Migration Plans
===============

* Archipelago
* Ado: Image
* Restricted Items also come to the same collection
* Instructions need to be added on how to access those

---------------------------------------------------
Charting Texas: A History of the State Through Maps
---------------------------------------------------

About
=====

This exhibition features maps and books, documenting several centuries of exploration and political competition for one specific area of North America — Texas. With advancements in geographic knowledge, surveying techniques, and printing technology, one can begin to see Texas taking its now familiar form from the earliest depictions in the 16th Century.

The collection consists of 57 items that are mostly maps.

* **Homepage**: https://spotlight.library.tamu.edu/spotlight/charting-texas

Current Stack
=============

* Spotlight
* Fedora

Migration Plans
===============

* Archipelago
* ADO Types: Map, Image, Book, Manuscript (Hand written Text?)
* Update exhibit to pull from Archipelago

Before Migration
================

* Update metadata to properly identify ADO types

----------------------------
Cherokee Freedmen Collection
----------------------------

This collection consists of written testimonies, letters, and affidavits related to over 30 applications of African Americans and their families that were denied enrollment as Cherokee Freedmen. The hearings were mostly conducted at Fort Gibson or Muskogee, Oklahoma by the United States Department of the Interior’s Commission to the Five Civilized Tribes (a.k.a. the Dawes Commission). Images of the original envelopes are included for most of the documents, which are dated from 1901 to 1907.

* **Homepage**: https://spotlight.library.tamu.edu/spotlight/cherokee-freedmen

Current Stack
=============

* Spotlight
* Fedora

Migration Plans
===============

* Archipelago
* ADO Types: Book
* Update exhibit to pull from Archipelago

Before Migration
================

* N/A

-------------------------
Coleccion Los Palabristas
-------------------------

Contains a collection of 650plus radio interviews with writers and artists from Mexico, South, and Central America, and Spain.

* **Homepage**: http://proxy.library.tamu.edu/login?url=https://avalon.library.tamu.edu/collections/xs55mc14f

Current Stack
=============

* Avalon
* Fedora

Migration Plans
===============

* Keep in Avalon
* Would like to bring to Archipelago as a remote resource but need to figure out restricted content

Before Migration
================

* N/A

---------------------------
College of Medicine Rosters
---------------------------

Made available online through a partnership between the College of Medicine and the University Libraries, these are a set
of photos of class rosters from the college of medicine.

Current Stack
=============

* Sage
* Fedora

Migration Plans
===============

* Migrate to Archipelago
* Should include OCR
* ADO type: Book? Image with Text? Does not need to be CWS as only 1 page

Before Migration
================

* Nothing, tesseract will work fine

---------------------------------------------------------------------
College of Veterinary Medicine & Biomedical Sciences Image Collection
---------------------------------------------------------------------

Digital collection that documents the history of the College of Veterinary Medicine and Biomedical Sciences.

Include 1491 photographs.

* **Homepage**: https://library.tamu.edu/discovery/discovery-context/cvm-images?direction=ASC

Current Stack
=============

* Sage
* Fedora

Migration Plans
===============

* Migrate to Archipelago
* ADO type: Image

Before Migration
================

* Nothing

---------------------------------------
Committee on South Asian Women Bulletin
---------------------------------------

This is a colleciton of PDFs from OAKTrust being served into Spotlight as issues.

* https://spotlight.library.tamu.edu/spotlight/committee-on-south-asian-women-bulletin

Current Stack
=============

* Spotlight (presentation)
* OAKTrust (Asset Management)
* IRIIIFService and base64 delegates for Image Serving of PDFs
* Github Pages for wrapping base64 delegates in IIIF manifests

Migration Plans
===============

* Migrate to Archipelago
* ADO type: Book or CWS Book
* Needs OCR (currently missing)
* Put back in Spotlight with new manifests for provenance purposes

Before Migration
================

* Compare tesseract output with new Impulse solution using DGX Spark

---------------------------
Cushing Exhibition Catalogs
---------------------------

Materials associated with physical exhibitions from Cushing Memorial Library.

Current Stack
=============

* OAKTrust

Migration Plans
===============

* Migrate to Archipelago
* ADO type: Book or CWS Book
* Needs OCR (currently missing)

Before Migration
================

* Do we need to split into JPGs or JP2s for OCR?

------------------------------------
Cushing Historical Images Collection
------------------------------------

Old Flickr images that were done 2 decades ago.  Over 22000 images.  Some have metadata, some do not, some have some AI generated
metadata.

Current Stack
=============

* OAKTrust

Migration Plans
===============

* Migrate to Archipelago
* ADO type: Image

Before Migration
================

* Figure out if this meets minimal standards for metadata according to our Archipelago docs.