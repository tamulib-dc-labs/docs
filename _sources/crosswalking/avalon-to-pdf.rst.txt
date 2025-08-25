===========================
Crosswalking: Avalon to PDF
===========================

When making pdfs of transcripts of Avalon media, use this to create the metadata that goes in the header of the pdf.

1. Use the script :code:`mark_get_avalon_files.py` to bring down metadata on Avalon. You may need to change some lines of :code:`def write_csv` depending on the structure of that collection's metadata on Avalon. For example, if multiple audio/video files are under the same digital object in Avalon, you will use "label" instead of "title".

2. For each media object you will need the following metadata fields. Those fields will be added to the pdf using a csv file.

+-------------------+-----------------------------------+
| JSON field        | Corresponding Column in csv file  |
+===================+===================================+
| title             | Title                             |
+-------------------+-----------------------------------+
| label             | Title                             |
+-------------------+-----------------------------------+
| main_contributors | Main Contributors                 |
+-------------------+-----------------------------------+
| contributor       | Contributors                      |
+-------------------+-----------------------------------+
| date_issued       | Date of Creation                  |
+-------------------+-----------------------------------+
|                   | Link to resource                  |
+-------------------+-----------------------------------+
| publisher         | Publisher                         |
+-------------------+-----------------------------------+
| genre             | Subjects                          |
+-------------------+-----------------------------------+
| subject           | Subjects                          |
+-------------------+-----------------------------------+
| temporal_subject  | Subjects                          |
+-------------------+-----------------------------------+
| geographic_subject| Subjects                          |
+-------------------+-----------------------------------+
| topical_subject   | Subjects                          |
+-------------------+-----------------------------------+
| terms_of_use      | Rights information                |
+-------------------+-----------------------------------+

* Note that the Subjects column will merge five different fields in the json.
* "Main contributors" is occasionally called "creators" in Avalon documentation/formating.
* Link to resource is the ARK, which cannot be acquired from this process.
