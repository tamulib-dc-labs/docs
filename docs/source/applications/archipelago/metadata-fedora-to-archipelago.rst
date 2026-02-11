================================================
Crosswalking Metadata from Fedora to Archipelago
================================================

This is how to convert each metadata field in the `Metadata Guidelines <https://oaktrust.library.tamu.edu/server/api/core/bitstreams/efa9caf8-76bf-44f3-a07f-15a5bd68dc2f/content>`_ from Fedora to out-of-the-box Archipelago metadata fields.

For more information on metadata conversions across more repositories, look at the documentation on `Crosswalking <https://tamulib-dc-labs.github.io/docs/applications/archipelago/crosswalking.html>`_.

.. note::

    "Mandatory" refers to whether the field is required according to the Metadata Guidelines. All fields labeled proposed are not addressed in Metadata Guidelines. DCMI type is a proposed way to keep the DCMI after crosswalking, since type in Archipelago uses a different controlled vocabulary.


+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Mandatory     | Metadata field name         | Fedora                      | Archipelago                          | Explanation                                   |
+===============+=============================+=============================+======================================+===============================================+
| Yes           | Title                       | dc:title                    | label                                |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Content Type                | dcterms.type                | note                                 |                                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Digital Publisher           |                             | publisher                            |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Rights/Access               | dc:rights                   | rights, rights_statements            | rights = uri, rights_statements = free text   |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Reformatting                | dc:format                   | digital_origin                       |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Filename                    |                             | image, document,                     | Use the columns that match the type of        |
|               |                             |                             | upload_associated_warcs              | media you are uploading.                      |
|               |                             |                             |                                      |                                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Subject                     | dc:subject,                 | subjects_local,                      | Map all subjects to subjects_local except     |
|               |                             | dcterms:spatial,            | subjects_local_personal_names        | for personal names.                           |
|               |                             | dcterms:temporal            |                                      |                                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Creator                     | dc:creator                  | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}                          | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Date Published              | dcterms:issued              | date_published                       |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Date Created                | dcterms:created             | date_created,                        | Use date_created if you have an exact date.   |
|               |                             |                             | date_created_edtf                    | Use date_created_edtf if you have a range.    |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Summary/Abstract            | dc:description,             | description                          |                                               |
|               |                             | dc:abstract                 |                                      |                                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Language                    | dc:language                 | language                             |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Institution/Department      | dc:contributor, dc:note     | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}, note                    | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Standard Digital Identifier | dc:identifier               | website_url                          | If dc.identifier is not a URL, a new field    | 
|               |                             | dc:URL                      |                                      | may need to be created.                       |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Local Digital Identifier    | dc:identifer                | local_identifier                     |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Edition/Revision Info       | dc.description              | description                          |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Alternative Title           | dcterms:alternative         | note                                 |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Genre                       | dcterms.type                | subjects_local                       | This will a local subject unless DCMI         |
|               |                             |                             |                                      | becomes part of Archipelago                   |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Table of Contents           |                             | description                          |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Contributor                 | dc:contributor              | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}                          | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Related Resource            | dcterms:IsPartOf            | ismemberof                           | ismemberof is for member of Collection        |
|               |                             |                             | ispartof                             | ispartof is for member of CreativeWorkSeries  |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Original Publisher          | dc:publisher                | publisher                            |                                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+ 
| Recommended   | Extent                      | dcterms:extent              | physical_description_extent          |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Sponsor                     | dc:contributor              | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}                          | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Source Collection           |                             | note                                 |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Original Resource           |                             | website_url                          |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Notes                       |                             | note                                 |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Original Place of           | dc:description              | description                          |                                               | 
|               | Publication, Production     |                             |                                      |                                               |
|               | or Manufacture              |                             |                                      |                                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Audience level              |                             | note                                 |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Classification              | dcterms:lcc                 | description                          |                                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Physical item identifier    |                             | description                          |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Proposed      | Citation                    | dc:citation                 | note                                 |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+

