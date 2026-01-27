==============================
Creating new items through AMI
==============================

---------------------------------
Create an csv compatible with AMI
---------------------------------

Here is the template to upload a spreadsheet to Archipelago.

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1wFw1fSr6OpSeNCX7tZDRjhPIfn_pdr7WgUT217FZQbs/edit?usp=sharing" height="400" width="800" frameborder="0" allowfullscreen></iframe>

Be sure to look at the second sheet (AMI template). Enter your data here.

If there are multiple values for any column, cells will have json strings such as:

:code:`[{"name_uri":"http://id.loc.gov/authorities/names/n2001078880","role_uri":"http://id.loc.gov/vocabulary/relators/cre","agent_type":"personal","name_label":"Hogg, James Stephen, 1851-1906.","role_label":"Creator"},{"name_uri":"https://id.loc.gov/authorities/names/n82158463","role_uri":"http://id.loc.gov/vocabulary/relators/rcp","agent_type":"personal","name_label":"Ross, Lawrence Sullivan, 1838-1898","role_label":"Addressee"}]`

This is an creator_lod example for an item with 2 creators. 

To avoid having to write complex json strings for linked data, `read this page on creating a more human-readable, "flat" csv <https://tamulib-dc-labs.github.io/docs/applications/archipelago/02_flat-csv.html>`_.

------------------
Mandatory fields
------------------

There are three mandatory fields for an AMI upload.

* node_uuid

* type

* label

What is node_uuid?
------------------
This is a temporary identifier used for the processing. You will need to create your own. Go to `uuidgenerator.net <https://www.uuidgenerator.net/>`_ to generate a uuid for each row.


What is type?
-------------
This tells Archipelago what type of item you are working with so it knows what template to use. For each item, you will likely select one from the following: Photograph, Postcard, AudioObject, VideoObject, Book, Manuscript, Map, VisualArtwork. 


What is label?
--------------
Label will usually be the title of the digital object.


-----------------------
Other fields (optional)
-----------------------

What is ismemberof?
-------------------

Before uploading an AMI spreadsheet, you will need to create a collection on Archipelago. Add the Archipelago UUID for the parent item (ie the collection) in this column.

------------------------
Where to get your files?
------------------------

There are two ways to attach files to your AMI upload. 

* zip archive
* link (can be IIIF but does not need to be)

Zip archive
------------

Create a zip archive with all files that will be uploaded in the batch. However, keep in mind:

* Zip files have a limit of 512 MB
* Zip files cannot have subfolders. For example, if you are trying to upload multiple digital objects at once but the files that make up each one follow the same naming pattern of :code:`0001.tif`, :code:`0002.tif`, :code:`0003.tif`, and so on, you will need to rename them to clearly differentiate them.

To attach files in a zip file to a digital object, enter the filename in the relevant column depending on what type of media it is (for example, the :code:`images` column). If you have multiple files for the same item, list them all, but separate them with a semicolon (example: :code:`0001.tif;0002.tif;0003.tif`).

Link
----

You can also link to media that is hosted online. This can be a IIIF link (any derivative that ends with :code:`/full/full/0/default.jpg` will work as will any :code:`.jp2`). Media can also be hosted in other sites. Add all links to the relevant media column in your csv.

If a digital object is made up of multiple files, list them all and separate them with semicolons.


-----------------------------
Now that you have your csv...
-----------------------------

1. Go to :code:`/admin/content`.

2. Click "Start an AMI set".

3. Select "Spreadsheet Importer" for your plugin.

4. Select "Create New ADOs" for Operation. Upload the csv in the dialog box.

5. Select "Direct" for data transformation approach. Select the columns where you added filenames or URLs (example: images, documents, etc.). You can select multiple.

6. When selecting Global ADO mappings, choose "ismemberof". For "Ado label", choose which column includes information that tells Archipelago what kind of media it is (most likely, this will be "type").

7. If you are using a zip file to upload content, upload the zip to the dialog box. If not, leave it blank. Then click to create the AMI set.

8. Once the set has been created, go to the "Process" tab and click "Confirm".