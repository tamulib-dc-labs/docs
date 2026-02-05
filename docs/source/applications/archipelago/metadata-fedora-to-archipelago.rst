=============================================
Crosswalking Metadata from SAF to Archipelago
=============================================

This is how to convert each metadata field in the `Metadata Guidelines <https://oaktrust.library.tamu.edu/server/api/core/bitstreams/efa9caf8-76bf-44f3-a07f-15a5bd68dc2f/content>`_ from Fedora to out-of-the-box Archipelago metadata fields.

For more information on metadata conversions across more repositories, look at the documentation on `Crosswalking <https://tamulib-dc-labs.github.io/docs/applications/archipelago/crosswalking.html>`_.

.. note::

    All fields labeled proposed are not addressed in Metadata Guidelines. DCMI type is a proposed way to keep the DCMI after crosswalking, since type in Archipelago uses a different controlled vocabulary.


+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Mandatory     | Metadata field name         | Fedora                      | Archipelago                          | 
+===============+=============================+=============================+======================================+
| Yes           | Title                       | dc:title                    | label                                | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Content Type                | dcterms.type                | type                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Digital Publisher           |                             | publisher                            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Rights/Access               | dc:rights                   | rights, rights_statements            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Reformatting                | dc:format                   | digital_origin                       | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Filename                    |                             | image, audio, video, document,       |
|               |                             |                             | transcript, captions,                |
|               |                             |                             | upload_associated_warcs              |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Subject                     | dc:subject,                 | subjects_local,                      | 
|               |                             | dcterms:spatial,            | subjects_local_personal_names,       |
|               |                             | dcterms:temporal            | subjects_loc.{X}.label,              |
|               |                             |                             | subjects_lcnaf_personal.{X}.label,   |
|               |                             |                             | subjects_lcnaf_corporate.{X}.label,  |
|               |                             |                             | subjects_lcnaf_geographic.{X}.label, |
|               |                             |                             | subjects_lcgft_terms.{X}.label       |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Creator                     | dc:creator                  | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Date Published              | dcterms:issued              | date_published                       | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Date Created                | dcterms:created             | date_created,                        |
|               |                             |                             | date_created_edtf                    |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Summary/Abstract            | dc:description,             | description                          |
|               |                             | dc:abstract                 |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Language                    | dc:language                 | language                             | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Institution/Department      | dc:contributor, dc:note     | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}, note                    |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Standard Digital Identifier | dc:identifier               | website_url                          | 
|               |                             | dc:URL                      |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Local Digital Identifier    | dc:identifer                | node_uuid                            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Edition/Revision Info       | dc.description              | description                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Alternative Title           | dcterms:alternative         | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Genre                       | dcterms.type                | subjects_lcgft_terms.{X}.label,      |
|               |                             |                             | subjects_local                       |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Table of Contents           |                             | description                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Contributor                 | dc:contributor              | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Related Resource            | dcterms:IsPartOf            | ismemberof, ispartof                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+ 
| Recommended   | Original Publisher          | dc:publisher                | publisher                            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+ 
| Recommended   | Extent                      | dcterms:extent              | physical_description_extent          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Sponsor                     | dc:contributor              | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Source Collection           |                             | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Original Resource           |                             | website_url                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Notes                       |                             | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Original Place of           | dc:description              | description                          | 
|               | Publication, Production     |                             |                                      |
|               | or Manufacture              |                             |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Audience level              |                             | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Classification              | dcterms:lcc                 | description                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Physical item identifier    |                             | description                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Proposed      | Citation                    | dc:citation                 | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Proposed      | DCMI Type                   | dcterms.type                | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+

