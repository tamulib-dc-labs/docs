=============================================
Crosswalking Metadata from SAF to Archipelago
=============================================

This is how to convert each metadata field in the `Metadata Guidelines <https://oaktrust.library.tamu.edu/server/api/core/bitstreams/efa9caf8-76bf-44f3-a07f-15a5bd68dc2f/content>`_ from DSpace to out-of-the-box Archipelago metadata fields.

For more information on metadata conversions across more repositories, look at the documentation on `Crosswalking <https://tamulib-dc-labs.github.io/docs/applications/archipelago/crosswalking.html>`_.

.. note::

    Some OAKTrust fields may include [en] at the end of the metadata field.

.. note::

    All fields labeled proposed are not addressed in Metadata Guidelines. DCMI type is a proposed way to keep the DCMI after crosswalking, since type in Archipelago takes from a different controlled vocabulary.


+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Mandatory     | Metadata field name         | OAKTrust                    | Archipelago                          | 
+===============+=============================+=============================+======================================+
| Yes           | Title                       | dc.title                    | label                                | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Content Type                | dc.type                     | type                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Digital Publisher           | dc.publisher                | publisher                            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Rights/Access               | dc.rights                   | rights, rights_statements            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Reformatting                | dc.format.medium            | digital_origin                       | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Filename                    | dc.identifier               | image, audio, video, document,       |
|               |                             |                             | transcript, captions,                |
|               |                             |                             | upload_associated_warcs              |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Subject                     | dc.subject                  | subjects_local,                      | 
|               |                             |                             | subjects_local_personal_names,       |
|               |                             |                             | subjects_loc.{X}.label,              |
|               |                             |                             | subjects_lcnaf_personal.{X}.label,   |
|               |                             |                             | subjects_lcnaf_corporate.{X}.label,  |
|               |                             |                             | subjects_lcnaf_geographic.{X}.label, |
|               |                             |                             | subjects_lcgft_terms.{X}.label       |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Creator                     | dc.creator                  | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Date Published              | dc.date.issued              | date_published                       | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Date Created                | dc.date.created             | date_created,                        |
|               |                             |                             | date_created_edtf                    |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Summary/Abstract            | dc.description              | description                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Language                    | dc.language                 | language                             | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Institution/Department      | dc.contributor, dc.note     | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}, note                    |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Standard Digital Identifier | dc.identifier.other         | website_url                          | 
|               |                             | dc.identifier.uri           |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Local Digital Identifier    | dc.identifier, id           | node_uuid                            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Edition/Revision Info       | dc.description              | description                          | 
|               |                             | dc.description.provenance   |                                      | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Alternative Title           | dcterms.alternative         | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Genre                       | dc.type, dc.subject         | subjects_lcgft_terms.{X}.label,      |
|               |                             |                             | subjects_local                       |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Table of Contents           | dcterms.description         | description                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Contributor                 | dc.contributor.photographer | creator_lod.{X}.label,               |
|               |                             | dc.contributor.illustrator  | creator.{X}                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Related Resource            | dc.relation.ispartof        | ismemberof, ispartof                 | 
|               |                             | dc.relation.uri             |                                      | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+ 
| Recommended   | Original Publisher          | dc.publisher                | publisher                            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+ 
| Recommended   | Extent                      | dc.format.extent            | physical_description_extent          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Sponsor                     | dc.contributor.sponsor      | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Source Collection           |                             | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Original Resource           | dc.identifier.uri           | website_url                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Notes                       | dc.description              | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Original Place of           | dc.description              | description                          | 
|               | Publication, Production     |                             |                                      |
|               | or Manufacture              |                             |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Audience level              |                             | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Classification              | dc.classification.lcc       | description                          |
|               |                             | dc.subject.classification   |                                      |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Physical item identifier    |                             | description                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Proposed      | Date Accessioned            | dc.date.accessioned         | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Proposed      | Date Available              | dc.date.available           | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Proposed      | Local identifier            | dc.identifer,               | local_identifier                     |
|               |                             | dc.identifier.other         |                                      |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Proposed      | DCMI Type                   | dc.type                     | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+

