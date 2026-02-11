=============================================
Crosswalking Metadata from SAF to Archipelago
=============================================

This is how to convert each metadata field in the `Metadata Guidelines <https://oaktrust.library.tamu.edu/server/api/core/bitstreams/efa9caf8-76bf-44f3-a07f-15a5bd68dc2f/content>`_ from DSpace to out-of-the-box Archipelago metadata fields.

For more information on metadata conversions across more repositories, look at the documentation on `Crosswalking <https://tamulib-dc-labs.github.io/docs/applications/archipelago/crosswalking.html>`_.

.. note::

    Some OAKTrust fields may include [en] at the end of the metadata field.

.. note::

    "Mandatory" refers to whether the field is required according to the Metadata Guidelines. All fields labeled proposed are not addressed in Metadata Guidelines. DCMI type is a proposed way to keep the DCMI after crosswalking, since type in Archipelago uses a different controlled vocabulary.


+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Mandatory     | Metadata field name         | OAKTrust                    | Archipelago                          | Explanation                                   |
+===============+=============================+=============================+======================================+===============================================+
| Yes           | Title                       | dc.title                    | label                                |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Content Type                | dc.type                     | note                                 |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Digital Publisher           | dc.publisher                | publisher                            |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Rights/Access               | dc.rights                   | rights, rights_statements            | rights = uri, rights_statements = free text   |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Reformatting                | dc.format.medium            | digital_origin                       |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Filename                    | dc.identifier               | image, document,                     | Use the columns that match the type of        |
|               |                             | bundle:Original             | upload_associated_warcs              | media you are uploading.                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Subject                     | dc.subject                  | subjects_local,                      | Map all subjects to subjects_local except     |  
|               |                             |                             | subjects_local_personal_names,       | personal names.                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Creator                     | dc.creator                  | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}                          | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Date Published              | dc.date.issued              | date_published                       |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Date Created                | dc.date.created             | date_created,                        | Use date_created if you have an exact date.   |
|               |                             |                             | date_created_edtf                    | Use date_created_edtf if you have a range.    |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Summary/Abstract            | dc.description              | description                          |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Language                    | dc.language                 | language                             |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Institution/Department      | dc.contributor, dc.note     | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}, note                    | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Standard Digital Identifier | dc.identifier.other         | website_url                          | If dc.identifier is not a URL, a new field    |
|               |                             | dc.identifier.uri           |                                      | may need to be created.                       |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Local Digital Identifier    | dc.identifier, id           | local_identifier                     |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Edition/Revision Info       | dc.description              | description                          |                                               | 
|               |                             | dc.description.provenance   |                                      |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Alternative Title           | dcterms.alternative         | note                                 |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Genre                       | dc.type, dc.subject         | subjects_lcgft_terms.{X}.label,      | subjects_lcgft_terms.{X}.label is for contro- |
|               |                             |                             | subjects_local                       | lled vocab. subjects_local is for local vocab |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Table of Contents           | dcterms.description         | description                          |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Contributor                 | dc.contributor.photographer | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             | dc.contributor.illustrator  | creator.{X}                          | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Related Resource            | dc.relation.ispartof        | ismemberof,                          | ismemberof is for member of Collection        |
|               |                             | dc.relation.uri             | ispartof                             | ispartof is for member of CreativeWorkSeries  | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+ 
| Recommended   | Original Publisher          | dc.publisher                | publisher                            |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+ 
| Recommended   | Extent                      | dc.format.extent            | physical_description_extent          |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Sponsor                     | dc.contributor.sponsor      | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}                          | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Source Collection           |                             | note                                 |                                               |   
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Original Resource           | dc.identifier.uri           | website_url                          |                                               |   
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Notes                       | dc.description              | note                                 |                                               |   
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Original Place of           | dc.description              | description                          |                                               |   
|               | Publication, Production     |                             |                                      |                                               |  
|               | or Manufacture              |                             |                                      |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Audience level              |                             | note                                 |                                               |   
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Classification              | dc.classification.lcc       | description                          |                                               |  
|               |                             | dc.subject.classification   |                                      |                                               |    
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Physical item identifier    | dc.identifer,               | local_identifier                     |                                               |  
|               |                             | dc.identifier.other         |                                      |                                               |   
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Proposed      | Date Accessioned            | dc.date.accessioned         | note                                 |                                               |   
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Proposed      | Date Available              | dc.date.available           | note                                 |                                               |   
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+