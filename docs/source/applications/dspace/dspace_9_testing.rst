===============================
Features and Tests for DSPACE 9
===============================

-------------
Journal Tests
-------------

Import Journal, Volume, and Issue with Relationships
====================================================

Journal Entities are currently used for several collections in OakTrust.  We need to test import:

1. Import Title with no relationships.
2. Import Volume adding relationships to Title.
3. Import Issue adding relationships to Volume.
4. Import Article adding relationships to Issue.

According to Nick at TDL, sorting of Articles should be better than in 7.

1. Test sort order of articles in an issue.

-------------
Feature Tests
-------------

Feature tests are influnenced by the `feature and tests document <https://docs.google.com/document/d/19oJ0MKoztPneoW9SWUDz8E8PVwW1ltfXyda-MY5sAOc/edit?tab=t.0>`_ we created earlier this summer.

Integration & Metadata Enrichment
=================================

OpenAIRE Data Correction
------------------------

`OpenAIRE Data Correction <https://wiki.lyrasis.org/display/DSDOC8x/OpenAIRE+Integration>`_`: this feature provides a basic integration with the OpenAIRE Content Provider Dashboard via the `Notification Broker <https://catalogue.openaire.eu/service/openaire.broker/overview>`_.  It allows repositories who have subscribed to the OpenAIRE Notification Broker to import JSON data from OpenAIRE in order to enhance or correct the metadata of Items in the repository. (Made possible thanks to the OpenAIRE Call Innovation funded project "Enrich local data via the OpenAIRE Graph” awarded to 4Science.)

**Tests**

1. Test subscription to the OpenAIRE Notification Broker.
2. Import JSON data and confirm metadata corrections appear in the repository.
3. Validate that corrections don’t overwrite local edits unexpectedly.

OpenAIRE Publication Claim
--------------------------

`OpenAIRE Publication Claim <https://wiki.lyrasis.org/display/DSDOC8x/Publication+Claim>`_: OpenAIRE Publication Claim: this feature provides a closer integration between DSpace and the OpenAIRE Publication REST API.  It allows DSpace to import possible publications from OpenAIRE for users having a Researcher Profile in DSpace. (Made possible thanks to the OpenAIRE Call Innovation funded project "Enrich local data via the OpenAIRE Graph” awarded to 4Science.

**Tests**

1. Log in with a Researcher Profile.
2. Trigger publication import from OpenAIRE.
3. Verify correct association of publications to user profile.

OpenAlex Integration (DSpace 9)
-------------------------------

OpenAlex integration: DSpace now supports `importing content (via MyDSpace) <https://wiki.lyrasis.org/display/DSDOC9x/Live+Import+from+external+sources#LiveImportfromexternalsources-OpenAlexIntegration>`_ from OpenAlex.org. The DSpace Publication Claim feature also now supports importing Publications related to a Researcher Profiles, provided that the profile has an OpenAlex ID. (Donated by 4Science and University of Cambridge with additional funding from the Vietsch Foundation)

**Tests**

1. Import content into MyDSpace from OpenAlex.
2. Verify integration of OpenAlex IDs with Researcher Profiles.

DOI Import (Crossref or DataCite)
---------------------------------

Import via DOI searches multiple sources at once (CrossRef, DataCite) (Donated by University of Bamberg)

**Tests**

1. Perform DOI-based import.
2. Confirm metadata from both sources is retrieved and merged correctly.

External Source Lookup (Relationships tab)
------------------------------------------

Lookup via external sources from the Edit Item page (Relationship tab): When editing an Entity, on the "Relationships" tab you can now click the "+Add" button to lookup and import related entities from `supported external sources <https://wiki.lyrasis.org/pages/viewpage.action?pageId=315720684#ImportingItemsviabasicbibliographicformats(Endnote,BibTex,RIS,CSV,etc)andonlineservices(arXiv,PubMed,CrossRef,CiNii,etc)-SupportedExternalSources>`_. (Donated by Atmire)

**Tests**

1. Use “+Add” to find and import related entities.
2. Confirm correct linking and metadata import.

Submission and Item Management
==============================

Duplicate Detection in Submission/Workflow
------------------------------------------

`Basic Duplicate Detection in submission and workflow <https://wiki.lyrasis.org/pages/viewpage.action?pageId=328958055>`_: this feature introduces basic duplicate detection into DSpace submission and workflow, using Solr's ability to search by levenshtein distance (Developed by The Library Code with support of TU Berlin, FHNW and ZHAW.)

**Tests**

1. Submit an Item with metadata close to an existing one.
2. Verify duplicate warning appears.

Primary Bitstream Management
----------------------------

`Improved "Primary Bitstream" management <https://wiki.lyrasis.org/display/DSDOC8x/Set+a+bitstream+as+primary>`_: Submitters can now define if a bitstream is a "primary" bitstream directly on the submission page after a file has been uploaded.  On the Item page, the primary bitstream now has a badge. (Developed by 4Science, funded by the University of California - California Digital Library)

**Tests**

1. Upload multiple files during submission.
2. Mark one as primary and check for badge on Item page.

Withdraw/Reinstate Request
--------------------------

`Request Withdrawal or Reinstatement <https://wiki.lyrasis.org/display/DSDOC8x/Request+Withdrawn+and+Reinstate+of+an+item>`_: Optionally, all logged-in users are able to request that a specific Item be withdrawn or reinstated using the new DSpace `Quality Assurance tool <https://wiki.lyrasis.org/display/DSDOC8x/Quality+Assurance>`_  (Donated by 4Science, partially funded by University of California - California Digital Liberary)

**Tests**

1. Logged-in user requests withdrawal.
2. Admin reviews/approves request.
3. Same test for reinstatement.

Edit Metadata with Authority Control
------------------------------------

Edit Metadata using Authority Control lookup: Users are now able to `edit metadata controlled by vocabularies in item's metadata edit form <https://wiki.lyrasis.org/display/DSDOC8x/Edit+Metadata#EditMetadata-Addoreditauthoritycontrolledmetadatafields>`_ in the same way that is done in submission form. (Donated by Toni Prieto)

**Tests**

1. Edit controlled fields in item metadata form.
2. Verify authority-controlled vocabularies work as expected.

Embargo Badge Display (DSPACE 9)
--------------------------------

Embargo release dates for embargoed files are now displayed on the Item page. The user interface includes a new `"showAccessStatuses" configuration for bitstreams <https://wiki.lyrasis.org/display/DSDOC9x/User+Interface+Configuration#UserInterfaceConfiguration-ItemPageSettings>`_ on the Item page. When enabled, all embargoed files will display a badge (on the Item page) which contains the date the embargo expires. (Donated by Université Laval)

**Tests**

1. Add embargoed file.
2. Check that Item page displays embargo expiry badge.


Search & Navigation
===================

Search Tab on Community/Collection pages
----------------------------------------

Search Tab on Community/Collection pages: All Community and Collection pages now include a "Search" tab. (Donated by Atmire)

**Tests**

1. Verify “Search” tab exists and functions.

Search Facets on Homepage & Collections
---------------------------------------

Search Facets on Homepage, Community/Collection pages: Optionally, search facets/filters can now be displayed on home page and all Community, and Collection pages. (Donated by DSquare Technologies and Atmire)

**Tests**

1. Test filtering on Homepage and Community/Collection pages.

Advanced Search Options
-----------------------

Advanced Search options: Optionally, a new "Advanced Search" filter can be enabled on the Search page to provide advanced search capabilities. (Donated by DSquare Technologies)

**Tests**

1. Enable advanced filters and verify additional options appear.

Geospatial Maps (DSpace 9)
--------------------------

`Support for Geospatial maps, including browsing and searching <https://wiki.lyrasis.org/display/DSDOC9x/User+Interface+Configuration#UserInterfaceConfiguration-Geospatialmapviewersettings>`_. Items or Entities including geospatial data can now (optionally) embed a map of the location on their Item page, and be searchable and browsable via a new geospatial map viewer. (Donated by The Library Code)

**Tests**

1. Upload Item with geospatial metadata.
2. Verify interactive map and geospatial search work.


Notifications and Interoperability
==================================

COAR Notify Protocol
--------------------

`COAR Notify Protocol <https://wiki.lyrasis.org/display/DSDOC8x/COAR+Notify>`_: DSpace now supports the COAR Notify Protocol for sending & receiving Linked Data Notifications (LDN) messages from external systems.  DSpace is able to register external LDN services to send or receive messages from.  This allows users to request review/endorsement from an external service (supporting COAR Notify) during the Item submission process. It also allows these external services to send event notifications into DSpace's `Quality Assurance tool <https://wiki.lyrasis.org/display/DSDOC8x/Quality+Assurance>`_.  (Donated by COAR and 4Science)

**Tests**

1. Register external LDN service.
2. Send review request during submission.
3. Receive inbound notification into QA tool.