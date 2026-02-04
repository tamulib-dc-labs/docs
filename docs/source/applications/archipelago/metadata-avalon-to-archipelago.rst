=============================================
Crosswalking Metadata from SAF to Archipelago
=============================================

This is how to convert each metadata field in the `Metadata Guidelines <https://oaktrust.library.tamu.edu/server/api/core/bitstreams/efa9caf8-76bf-44f3-a07f-15a5bd68dc2f/content>`_ from Avalon to out-of-the-box Archipelago metadata fields.

For more information on metadata conversions across more repositories, look at the documentation on `Crosswalking <https://tamulib-dc-labs.github.io/docs/applications/archipelago/crosswalking.html>`_.

.. note::

    All fields labeled proposed are not addressed in Metadata Guidelines.


+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Mandatory     | Metadata field name         | Avalon                      | Archipelago                          | 
+===============+=============================+=============================+======================================+
| Yes           | Title                       | Title                       | label                                | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Content Type                | Genre                       | type                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Digital Publisher           | Publisher                   | publisher                            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Rights/Access               | Terms of Use                | rights, rights_statements            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Reformatting                | Genre                       | digital_origin                       | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Yes           | Filename                    | File, Label, Caption File,  | image, audio, video, document,       |
|               |                             | Caption Label, Transcript   | transcript, captions,                |
|               |                             | File, Transcript Label      | upload_associated_warcs              |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Subject                     | Subject,                    | subjects_local,                      | 
|               |                             | Geographic Subject,         | subjects_local_personal_names,       |
|               |                             | Temporal Subject            | subjects_loc.{X}.label,              |
|               |                             |                             | subjects_lcnaf_personal.{X}.label,   |
|               |                             |                             | subjects_lcnaf_corporate.{X}.label,  |
|               |                             |                             | subjects_lcnaf_geographic.{X}.label, |
|               |                             |                             | subjects_lcgft_terms.{X}.label       |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Creator                     | Creator                     | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Date Published              | Date Issued                 | date_published                       | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Date Created                | Date Issued                 | date_created,                        |
|               |                             |                             | date_created_edtf                    |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Summary/Abstract            | Abstract                    | description                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Language                    | Language                    | language                             | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Institution/Department      | Contributor, Note type,     | creator_lod.{X}.label,               |
|               |                             | Note                        | creator.{X}, note                    |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Standard Digital Identifier | Identifier,                 | website_url                          | 
|               |                             | Identifier Type             |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Local Digital Identifier    | Other Identifier,           | node_uuid                            | 
|               |                             | Other Identifier Type,      |                                      |
|               |                             | Work ID, File ID            |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| If applicable | Edition/Revision Info       | Description                 | description                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Alternative Title           |                             | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Genre                       | Genre                       | subjects_lcgft_terms.{X}.label,      |
|               |                             |                             | subjects_local                       |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Table of Contents           | Table of Contents           | description                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Contributor                 | Contributor                 | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Related Resource            | Series, Related Item Label, | ismemberof, ispartof                 | 
|               |                             | Related Item URL            |                                      | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+ 
| Recommended   | Original Publisher          | Publisher                   | publisher                            | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+ 
| Recommended   | Extent                      | Physical Description        | physical_description_extent          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Recommended   | Sponsor                     | Contributor                 | creator_lod.{X}.label,               |
|               |                             |                             | creator.{X}                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Source Collection           |                             | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Original Resource           |                             | website_url                          | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Notes                       | Note type, Note             | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Original Place of           |                             | description                          | 
|               | Publication, Production     |                             |                                      |
|               | or Manufacture              |                             |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Audience level              |                             | note                                 | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Classification              |                             | description                          |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Optional      | Physical item identifier    | Other Identifier,           | description                          |
|               |                             | Other Identifier Type       |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+
| Proposed      | Local identifier            | Other Identifier,           | local_identifier                     |
|               |                             | Other Identifier Type       |                                      |
+---------------+-----------------------------+-----------------------------+--------------------------------------+

