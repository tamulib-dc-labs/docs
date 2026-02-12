===========================================================
Crosswalking from DSpace, Fedora, and Avalon to Archipelago
===========================================================

Definitions:

* Element/Metadata element - a metadata concept (ie “subject”, “creator”).

* Field/Metadata field - the specific term used for a metadata concept in a repository (ie “dc.subject”, “dc.creator”). These are usually the names of columns in metadata spreadsheets.

All elements in the `Metadata Guidelines <https://oaktrust.library.tamu.edu/server/api/core/bitstreams/efa9caf8-76bf-44f3-a07f-15a5bd68dc2f/content>`_ are in the first table below. Each row contains the fields used for that element in DSpace, Fedora, and Avalon. The final column proposes a field to use in Archipelago spreadsheets. The element name will be the heading displayed in the descriptive metadata.

During migration, the administrator may need to evaluate certain columns to identify the correct element. For example, a dc.publisher could refer to a digital publisher or an original publisher. Fields that require this consideration are marked with an asterisk. 

Some elements in this table have no metadata fields associated with them. Other elements may not have a complete list of all associated metadata fields. As more metadata fields are identified in existing metadata records over the migration process, they will be added to this table.

This is a table used for crosswalking existing collections. There may be future collections that require new metadata elements and fields. In that case, new fields will be added to accommodate those collections.

--------------
TAMU Elements:
--------------

+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Element                      | DSpace Field(s)                | Fedora Field(s)        | Avalon Field(s)        | Proposed Archipelago Field    |
+==============================+================================+========================+========================+===============================+
| Title                        | dc.title                       | dc:title               | Title                  | title                         |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Content Type                 | dc.type                        | dcterms.type           | Genre *                | content_type                  |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Digital Publisher            | dc.publisher *                 | dc:publisher *         | Publisher *            | digital_publisher             |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Rights/Access                | dc.rights, dc.rights.uri       | dc:rights              | Terms of Use           | rights_access                 |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Reformatting                 | dc.format.digitalOrigin        | dc:format              |                        | reformatting                  |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Filename                     | dc.identifier, bundle:Original |                        | File, Transcript File, |                               |
|                              |                                |                        | Captions File          |                               |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Subjects                     | dc.subject                     | dc:subject             | Subject                | subject                       |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Geographic Subject           | dc.subject                     | dc:spatial             | Geographic Subject     | geographic_subject            |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Temporal Subject             | dc.subject                     | dc:temporal            | Temporal Subject       | temporal_subject              |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Creator                      | dc.creator                     | dc:creator             | Creator                | creator                       |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Date Published               | dc.date.issued                 | dcterms:issued         | Date Issued            | date_published                |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Date Created                 | dc.date.created                | dcterms:created        |                        | date_created                  |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Summary/Abstract             | dc.description *               | dc:description * ,     | Abstract               | summary_abstract              |
|                              |                                | dc:abstract            |                        |                               |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Language                     | dc.language.iso                | dc:language            | Language               | language                      |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Institution/Department       | dc.contributor * ,             | dc:contributor * ,     |                        | institution/department        |
|                              | dc.description *               | dc:description *       |                        |                               |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Standard Digital Identifier  | dc.identifier.other,           | dc:identifier * ,      |                        | standard_digital_identifier   |
|                              | dc.identifier.uri              | dc:URL *               |                        |                               |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Local Digital Identifier     | dc.identifier, id              | dc:identifier *        |                        | local_digital_identifier      |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Edition/Revision Information | dc.description *               | dc:description         |                        | edition_revision              |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Alternative Title            | dcterms.alternative            | dcterms:alternative    |                        | alternative_title             |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Genre                        | dc.type.genre, dc.subject *    | dcterms.type           | Genre                  | genre                         |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Table of Contents            |                                |                        | Table of Contents      | table_of_contents             |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Contributor                  | dc.contributor.photographer,   | dc:contributor         | Contributor            | contributor                   |
|                              | dc.contributor.illustrator,    |                        |                        |                               |
|                              | dc.contributor.editor          |                        |                        |                               |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Related Resource             | dc.relation.uri * ,            | dcterms:IsPartOf       | Series, Related Item   | related_resource              |
|                              | dc:relation.ispartofseries,    |                        | Label, Related Item    |                               |
|                              | dc:relation.isbasedon          |                        | URL                    |                               |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Original Publisher           | dc.publisher *                 | dc:publisher *         | Publisher *            | original_publisher            |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Extent                       | dc.extent, dc.format.extent    | dcterms:extent         | Physical Description   | extent                        |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Sponsor                      | dc.contributor.sponsor,        | dc:contributor * ,     |                        | sponsor                       |
|                              | dc.description.sponsorship     | dc:description         |                        |                               |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Source Collection            |                                |                        |                        | source_collection             |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Original Resource            |                                |                        |                        | original_resource             |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Note                         | dc.description *               | dc:description *       | Note                   | note                          |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Original Place of            | dc.description *               | dc:description *       |                        | original_place                |
| Publication, Production,     |                                |                        |                        |                               |
| or Manufacture               |                                |                        |                        |                               |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Audience Level               |                                |                        |                        | audience_level                |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Classification               | dc.classification.lcc,         | dcterms:lcc            |                        | classification                |
|                              | dc.subject.classification      |                        |                        |                               |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Physical item identifier     |                                |                        |                        | physical_item_identifier      |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Physical item location       |                                |                        |                        | physical_item_location        |
+------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+

.. note::
    Geographic and Temporal Subjects are not in the Metadata Guidelines. They are in the table because the data already exists for them.

-----------------------
Archipelago-only Fields 
-----------------------

These fields are used by Archipelago and map to elements that are not used elsewhere in the TAMU Libraries repositories. Most of these fields are technical and must be added to existing records. This can be done by the administrator doing the migration. Other fields (such as Linked Data) will not be included in migration at all but may be used for future digital collections.

+-------------------------------+----------------------------------------------+
| Proposed Archipelago Field    | Detail                                       |
+===============================+==============================================+
| Type                          | Not the same as dc.type                      |
+-------------------------------+----------------------------------------------+
| node_uuid                     | Internal Archipelago identifier              |
+-------------------------------+----------------------------------------------+
| ismemberof                    | Use for child objects of Collections, should |
|                               | be node_uuid for Collection, convert         |
|                               | internal "Related Resource" url to this      |
+-------------------------------+----------------------------------------------+
| ispartof                      | Use for child objects of CreativeWorkSeries, |
|                               | Should nbe node_uuid for CreativeWorkSeries, |
|                               | Convert internal "Related Resource"          |
|                               | url to this                                  |
+-------------------------------+----------------------------------------------+
| sequence_id                   | Use to order child objects of                |
|                               | CreativeWorkSeries                           |
+-------------------------------+----------------------------------------------+
| owner                         | Respository that owns the material           |
+-------------------------------+----------------------------------------------+
| Image                         | Link or filepath to image                    |
+-------------------------------+----------------------------------------------+
| Document                      | Link or filepath to document                 |
+-------------------------------+----------------------------------------------+
| Audio                         | Link or filepath to audio                    |
+-------------------------------+----------------------------------------------+
| Transcript                    | Link or filepath to transcript files         |
+-------------------------------+----------------------------------------------+
| Video                         | Link or filepath to video                    |
+-------------------------------+----------------------------------------------+
| Captions                      | Link or filepath to caption files            |
+-------------------------------+----------------------------------------------+
| upload_associated_warcs       | Link or filepath to warc                     |
+-------------------------------+----------------------------------------------+
| Linked data                   | Upload uri with label                        |
+-------------------------------+----------------------------------------------+
| Geolocated data               | Upload coordinates with label                |
+-------------------------------+----------------------------------------------+

---------------------------------
Where can I see the entire table?
---------------------------------

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1wFw1fSr6OpSeNCX7tZDRjhPIfn_pdr7WgUT217FZQbs/edit?usp=sharing" height="400" width="800" frameborder="0" allowfullscreen></iframe>

Be sure to look at the third sheet, Crosswalking, to see a table of all the Metadata field names included in the `Metadata Guidelines <https://oaktrust.library.tamu.edu/server/api/core/bitstreams/efa9caf8-76bf-44f3-a07f-15a5bd68dc2f/content>`_ and how each field maps to OAKTrust, Fedora, Avalon, and Archipelago. 
