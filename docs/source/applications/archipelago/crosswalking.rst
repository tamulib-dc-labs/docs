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

+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Element                      | Dublin Core                    | MODS                              | DSpace Field(s)                | Fedora Field(s)        | Avalon Field(s)        | Proposed Archipelago Field    |
+==============================+================================+===================================+================================+========================+========================+===============================+
| Title                        | dc:title                       | mods:titleInfo                    | dc.title                       | dc:title               | Title                  | title                         |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Content Type                 | dc:type                        | mods:typeofResource               | dc.type, dc:type.material      | dcterms.type           | Genre *                | content_type                  |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Digital Publisher            | dc:publisher                   | publisher, mods:note              | dc.publisher *                 | dc:publisher *         | Publisher *            | digital_publisher             |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Rights/Access                | dc:rights                      | mods:accessCondition              | dc.rights, dc.rights.uri       | dc:rights              | Terms of Use           | rights_access                 |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Reformatting                 | dc:format                      | mods:digitalOrigin                | dc.format.digitalOrigin        | dc:format              |                        | reformatting                  |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Filename                     | dc:identifier                  | mods:identifier                   | dc.identifier, bundle:Original |                        | File, Transcript File, |                               |
|                              |                                |                                   |                                |                        | Captions File          |                               |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Subjects                     | dc:subject                     | mods:subject                      | dc.subject, dc.subject.lcsh    | dc:subject             | Subject                | subject                       |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Creator                      | dc:creator                     | mods:name                         | dc.creator                     | dc:creator             | Creator                | creator                       |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Date Published               | dc:date.issued                 | mods:dateIssued                   | dc.date.issued                 | dcterms:issued         | Date Issued            | date_published                |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Date Created                 | dc:date.created                | mods:dateCreated                  | dc.date.created                | dcterms:created        |                        | date_created                  |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Summary/Abstract             | dc:description,                | mods:abstract                     | dc.description *               | dc:description * ,     | Abstract               | summary_abstract              |
|                              | dc:description.abstract        |                                   |                                | dc:abstract            |                        |                               |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Language                     | dc:language                    | mods:languageTerm                 | dc.language.iso                | dc:language            | Language               | language                      |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Institution/Department       | dc:contributor,                | mods:publisher, mods:namePart,    | dc.contributor * ,             | dc:contributor * ,     |                        | institution_department        |
|                              | dc:description                 | mods:note                         | dc.description *               | dc:description *       |                        |                               |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Standard Digital Identifier  | dc:identifier                  | mods:identifier type=""           | dc.identifier.other,           | dc:identifier * ,      |                        | standard_digital_identifier   |
|                              |                                |                                   | dc.identifier.uri              | dc:URL *               |                        |                               |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Local Digital Identifier     | dc:identifier                  | mods:identifier type="local"      | dc.identifier, id              | dc:identifier *        |                        | local_digital_identifier      |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Edition/Revision Information | dc:description                 | mods:edition                      | dc.description *               | dc:description *       |                        | edition_revision              |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Alternative Title            | dc:title.alternative           | mods:titleInfo type="alternative" | dcterms.alternative            | dcterms:alternative    |                        | alternative_title             |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Genre                        | dc:type                        | mods:genre authority=""           | dc.type.genre, dc.subject *    | dcterms.type           | Genre                  | genre                         |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Table of Contents            | dc.description.tableOfContents | mods:tableOfContents              |                                |                        | Table of Contents      | table_of_contents             |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Contributor                  | dc:contributor                 | mods:name                         | dc.contributor.photographer,   | dc:contributor         | Contributor            | contributor                   |
|                              |                                |                                   | dc.contributor.illustrator,    |                        |                        |                               |
|                              |                                |                                   | dc.contributor.editor          |                        |                        |                               |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Related Resource             | dc:relation.isPartOf,          | mods:relatedItem                  | dc.relation.uri * ,            | dcterms:IsPartOf       | Series, Related Item   | related_resource              |
|                              | dc:relation.hasPart            |                                   | dc:relation.ispartofseries,    |                        | Label, Related Item    |                               |
|                              |                                |                                   | dc:relation.isbasedon          |                        | URL                    |                               |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Original Publisher           | dc:publisher                   | mods:publisher, mods:originInfo   | dc.publisher *                 | dc:publisher *         | Publisher *            | original_publisher            |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Extent                       | dc:format.extent               | mods:physicalDescription          | dc.extent                      | dcterms:extent         | Physical Description   | extent                        |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Sponsor                      | dc:contributor,                | mods:name, mods:note              | dc.contributor.sponsor,        | dc:contributor * ,     |                        | sponsor                       |
|                              | dc:description                 |                                   | dc.description.sponsorship     | dc:description *       |                        |                               |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Source Collection            | dc:relation                    | mods:relatedItem                  |                                |                        |                        | source_collection             |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Original Resource            | dc:source                      | mods:relatedItem                  |                                |                        |                        | original_resource             |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Note                         | dc:description                 | note                              | dc.description *               | dc:description *       | Note                   | note                          |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Original Place of            | dc:description                 | mods:placeTerm                    | dc.description *               | dc:description *       |                        | original_place                |
| Publication, Production,     |                                |                                   |                                |                        |                        |                               |
| or Manufacture               |                                |                                   |                                |                        |                        |                               |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Audience Level               | dc:audience                    | mods:targetAudience               |                                |                        |                        | audience_level                |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Classification               | dc:description                 | mods:classification               | dc:classification.lcc,         | dcterms:lcc            |                        | classification                |
|                              |                                |                                   | dc:subject.classification      |                        |                        |                               |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Physical item identifier     | dc:identifier                  | mods:identifier type="local"      |                                |                        |                        | physical_item_identifier      |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Physical item location       | dc:description                 | mods:location                     |                                |                        |                        | physical_item_location        |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Geographic Subject           | dc:subject                     | mods:subject                      | dc.subject *                   | dc:spatial             | Geographic Subject     | geographic_subject            |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
| Temporal Subject             | dc:subject                     | mods:subject                      | dc.subject *                   | dc:temporal            | Temporal Subject       | temporal_subject              |
+------------------------------+--------------------------------+-----------------------------------+--------------------------------+------------------------+------------------------+-------------------------------+
.. note::
    Geographic and Temporal Subjects are not in the Metadata Guidelines. They are in the table because the data already exists for them.

-----------------------
Archipelago-only Fields 
-----------------------

These fields are used by Archipelago and map to elements that are not used elsewhere in the TAMU Libraries repositories. Most of these fields are technical and must be added to existing records. This can be done by the administrator doing the migration. Other fields (such as Linked Data) will not be included in migration at all but may be used for future digital collections.

+-------------------------------+----------------------------------------------+
| Archipelago Field             | Detail                                       |
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
|                               | should be node_uuid for CreativeWorkSeries,  |
|                               | convert internal "Related Resource"          |
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