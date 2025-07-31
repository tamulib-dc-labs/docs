===========================
Crosswalking: Avalon to PDF
===========================

When making pdfs of transcripts of Avalon media, use this to create the metadata that goes in the header of the pdf.

1. Create a json using the code avalon.py

2. For each media object you will need the following metadata fields. Those fields will be added to the pdf using a csv file.

+-------------------+-----------------------------------+
| JSON field        | Corresponding Column in csv file  |
+===================+===================================+
| title             | Title                             |
+-------------------+-----------------------------------+
| main_contributors | Main Contributors                 |
+-------------------+-----------------------------------+
| contributor       | Contributors                      |
+-------------------+-----------------------------------+
|                   | Link to resource                  |
+-------------------+-----------------------------------+
| published_by      | Publisher                         |
+-------------------+-----------------------------------+
| genre             | Subjects                          |
+-------------------+-----------------------------------+
| subject           | Subjects                          |
+-------------------+-----------------------------------+
| terms_of_use      | Rights information                |
+-------------------+-----------------------------------+

* Note that the Subjects column will merge two different fields in the json.
* "Main contributors" is occasionally called "creators" in Avalon documentation/formating.
* Link to resource is the ARK.