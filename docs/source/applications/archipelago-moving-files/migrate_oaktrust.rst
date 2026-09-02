==============================
Migrating OAKTrust Collections
==============================

Download existing OAKTrust metadata for a collection using Metadata Export function.

Clone `oaktrust_to_archipelago <https://github.com/tamulib-dc-labs/oaktrust_to_archipelago>`_ repository.

Move metadata export csv to your oaktrust_to_archipelago repository. Run the following code:

:code:`uv run oaktrust_to_archipelago.py input.csv`

You should receive an output csv with links to each file. 

* This output requires lots of metadata cleanup before you can upload it into Archipelago. Do not directly upload unreveiwed outputs from this to Archipelago.

* Make sure you are not uploading tifs into Archipelago. If an OAKTrust collection contains tifs, you will need to download the files and then convert to jp2s.

* If you have an item made up of many files, it is recommended to upload this as a Digital Object Collection, so you will want to make every file its own separate ADO. Therefore, in the spreadsheet, each page should get its own row. You will need to create this, since this function by default places all files for a given item in the same row.

* Check oaktrust_to_archipelago repository for more specific instructions regarding changing the bundle to get a different set of files.