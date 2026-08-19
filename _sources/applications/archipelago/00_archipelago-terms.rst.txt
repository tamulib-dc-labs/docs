===========
Terminology
===========

Archipelago Digital Object (ADO) - any digital object or digital object collection on Archipelago.

Archipelago Multi-Importer (AMI) - the module used to batch ingest ADOs into Archipelago using a spreadsheet.

Embargo - a restriction that hides an ADO's viewers and files from some or all visitors while leaving its metadata public. Archipelago drives this from a key in the object's JSON, not from an access control list.

IP embargo - an embargo that is lifted for visitors whose IP address falls inside a configured range, used at TAMU to make objects viewable on campus only. See :doc:`11_ip-embargo`.

Element/Metadata element - a metadata concept (ie “subject”, “creator”).

Field/Metadata field - the specific term used for a metadata concept in a repository (ie “dc.subject”, “dc.creator”).

JSON - a file format (.json) used for storing information. All Archipelago metadata is stored in JSON files.

Strawberry field - a descriptive metadata field comprised of many individual Archipelago fields put together. In order to add a field to the larger Strawberry Field, that metadata field and value must first go into the JSON.

TWIG - the template engine used to extract metadata from JSONs and display it on the Archipelago site.

Type/ADO Type/Worktype - a mandatory, Archipelago-specific metadata field that tells Archipelago which view mode to use for a specific kind of ADO. For example, "Book" or "VideoObject".

View mode/Display mode - a template used by Archipelago to display specific media. For example, "Digital Object Full View" or "Digital Object with Audio Player"

