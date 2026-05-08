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

Before Migration
================

* Image Assets need a descriptive metadata record
* The record needs to have georeferencing information
* Rights can be NKC or something like that unless we no for sure it should be NC
* Images have dates.  Can get that easily with Computer Vision
* Can also use Identifier Data in Upper right for Title
* Since no metadata record, easiest to start with a blank AMI set in special collections
