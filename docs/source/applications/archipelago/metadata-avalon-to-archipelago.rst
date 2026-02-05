================================================
Crosswalking Metadata from Avalon to Archipelago
================================================

This is how to convert each metadata field in the `Metadata Guidelines <https://oaktrust.library.tamu.edu/server/api/core/bitstreams/efa9caf8-76bf-44f3-a07f-15a5bd68dc2f/content>`_ from Avalon to out-of-the-box Archipelago metadata fields.

For more information on metadata conversions across more repositories, look at the documentation on `Crosswalking <https://tamulib-dc-labs.github.io/docs/applications/archipelago/crosswalking.html>`_.

.. note:: 

    "Mandatory" refers to whether the field is required according to the Metadata Guidelines.

+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Mandatory     | Metadata field name         | Avalon                      | Archipelago                          | Explanation                                   |
+===============+=============================+=============================+======================================+===============================================+
| Yes           | Title                       | Title                       | label                                |                                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Content Type                | Genre                       | note                                 |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Digital Publisher           | Publisher                   | publisher                            |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Rights/Access               | Terms of Use                | rights, rights_statements            | rights = uri, rights_statements = free text   | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Reformatting                | Genre                       | digital_origin                       |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Yes           | Filename                    | File, Label, Caption File,  | audio, video, transcript, captions   | Use the columns that match the type of        |
|               |                             | Caption Label, Transcript   |                                      | media you are uploading.                      |
|               |                             | File, Transcript Label      |                                      |                                               |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Subject                     | Subject,                    | subjects_local,                      | Map subjects according to the type of         | 
|               |                             | Geographic Subject,         | subjects_local_personal_names,       | subject heading it is (personal, corporate,   |
|               |                             | Temporal Subject            | subjects_loc.{X}.label,              | geographic, genre/form, generic) and whether  |
|               |                             |                             | subjects_lcnaf_personal.{X}.label,   | it is local or not. More fields will be       |
|               |                             |                             | subjects_lcnaf_corporate.{X}.label,  | added as we add more controlled vocabularies  |
|               |                             |                             | subjects_lcnaf_geographic.{X}.label, | to Archipelago. Map all Temporal Subjects     |
|               |                             |                             | subjects_lcgft_terms.{X}.label       | to subjects_local or subjects_loc.{X}.label.  |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Creator                     | Creator                     | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}                          | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Date Published              | Date Issued                 | date_published                       |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Date Created                | Date Issued                 | date_created,                        | Use date_created if you have an exact date.   |
|               |                             |                             | date_created_edtf                    | Use date_created_edtf if you have a range.    |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Summary/Abstract            | Abstract                    | description                          |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Language                    | Language                    | language                             |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Institution/Department      | Contributor, Note type,     | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             | Note                        | creator.{X}, note                    | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Standard Digital Identifier | Identifier,                 | website_url                          | If Identifier is not a URL, a new field may   |
|               |                             | Identifier Type             |                                      | need to be created.                           |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Local Digital Identifier    | Other Identifier,           | local_identifier                     |                                               |  
|               |                             | Other Identifier Type,      |                                      |                                               | 
|               |                             | Work ID, File ID            |                                      |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| If applicable | Edition/Revision Info       | Description                 | description                          |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Alternative Title           |                             | note                                 |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Genre                       | Genre                       | subjects_lcgft_terms.{X}.label,      | subjects_lcgft_terms.{X}.label is for contro- |
|               |                             |                             | subjects_local                       | lled vocab. subjects_local is for local vocab |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Table of Contents           | Table of Contents           | description                          |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Contributor                 | Contributor                 | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}                          | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Related Resource            | Series, Related Item Label, | ismemberof,                          | ismemberof is for member of Collection        | 
|               |                             | Related Item URL            | ispartof                             | ispartof is for member of CreativeWorkSeries  | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+ 
| Recommended   | Original Publisher          | Publisher                   | publisher                            |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+ 
| Recommended   | Extent                      | Physical Description        | physical_description_extent          |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Recommended   | Sponsor                     | Contributor                 | creator_lod.{X}.label,               | creator_lod is for controlled vocab,          |
|               |                             |                             | creator.{X}                          | creator.{X} is for local names                |
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Source Collection           |                             | note                                 |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Original Resource           |                             | website_url                          |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Notes                       | Note type, Note             | note                                 |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Original Place of           |                             | description                          |                                               |  
|               | Publication, Production     |                             |                                      |                                               | 
|               | or Manufacture              |                             |                                      |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Audience level              |                             | note                                 |                                               |  
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Classification              |                             | description                          |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+
| Optional      | Physical item identifier    | Other Identifier,           | local_identifier                     |                                               | 
|               |                             | Other Identifier Type       |                                      |                                               | 
+---------------+-----------------------------+-----------------------------+--------------------------------------+-----------------------------------------------+

