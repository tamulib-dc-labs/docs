=============================
How to make a PDF transcript to upload to Avalon.
=============================

This page explains how to generate pdfs for a collection of objects using existing metadata already on Avalon and a folder of .vtts with the transcripts.

1. Download existing metadata by using `pyavalon <https://github.com/tamulib-dc-labs/pyavalon>`_.

2. In the terminal enter :code:`pyavalon get_file_ids_from_a_collection -c "{collection id}" -i {pre or prod}`. 

3. A .csv will generate with metadata for the title, creator, contributor, date, rights information, publisher, subjects, derivative file, a parent work file id, a file id, a file title, and a work title.

4. Create your own :code:`{collection-name}-pdf.csv`. Include the following columns:

+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Column in {collection-name}-pdf.csv   | How to create using output.csv                                                                            |
+=======================================+===========================================================================================================+
| Title                                 | Use work title if that is the only title available. If not use file title.                                |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Main Contributor(s)                   | Use Creator field.                                                                                        |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Constributor(s)                       | Use Contributor field.                                                                                    |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Date of Creation                      | Use Date field.                                                                                           |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Link to resource                      | Use Parent work field in following format: "https://avalon.library.tamu.edu/media_objects/{Parent work}"` |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Publisher                             | Use Publisher field.                                                                                      |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Subject(s)                            | Use Subjects field.                                                                                       |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Rights Information                    | Use Rights information field.                                                                             |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+
| VTT                                   | Use the Parent work and File id fields following format: "{Parent work}_{File id}_access.caption.vtt"     |
+---------------------------------------+-----------------------------------------------------------------------------------------------------------+

5. Use the function pdf-build. Change the :code:`collection_title` and the line below it to have the name of your collection and csv you just created. Make sure you have a folder for your pdfs to save and change the :code:`output_filename` and the vtt location.

6. Run :code:`python pdf-build`. 

7. To upload to Avalon, look at the documentation titled "Importing media into Avalon via API Key". PDFs can only be imported through the API key, never through spreadsheets.