================================
How to do an AMI batch upload in Archipelago
================================

----------------------------------
Create an csv compatible with AMI
----------------------------------

Here is the template for every spreadsheet uploaded into Archipelago.

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1wFw1fSr6OpSeNCX7tZDRjhPIfn_pdr7WgUT217FZQbs/edit?usp=sharing" height="400" width="800" frameborder="0" allowfullscreen></iframe>

Be sure to look at the second sheet (Machine Friendly).

If there are multiple values for any column, cells will have json strings such as:

:code:`[{"name_uri":"http://id.loc.gov/authorities/names/n2001078880","role_uri":"http://id.loc.gov/vocabulary/relators/cre","agent_type":"personal","name_label":"Hogg, James Stephen, 1851-1906.","role_label":"Creator"},{"name_uri":"https://id.loc.gov/authorities/names/n82158463","role_uri":"http://id.loc.gov/vocabulary/relators/rcp","agent_type":"personal","name_label":"Ross, Lawrence Sullivan, 1838-1898","role_label":"Addressee"}]`

This is an creator_lod example for an item with 2 creators. To avoid having to write complex json strings, look at the documentation on making a more human friendly spreadsheet that can be converted into the AMI-compatible format `here <https://tamulib-dc-labs.github.io/docs/applications/archipelago/creating-ami-csv.html>`_.

----------------------------------
Where to get your files?
----------------------------------

There are two ways to attach files to your AMI upload. 

* zip archive
* link (can be IIIF but does not need to be)

Zip archive
------------

Create a zip archive with all images that will be uploaded in the batch. However, keep in mind:

* Zip files have a limit of 500 MB
* Zip files cannot have subfolders. For example, if you are trying to upload multiple items at once but each one follows the same naming pattern of :code:`0001.tif`, :code:`0002.tif`, :code:`0003.tif`, and so on, you will need to rename them to clearly differentiate them.

To attach images in a zip file to an item, enter the filename in the relevant column depending on what type of media it is (for example, the :code:`images` column). If you have multiple files for the same item, list them all, but separate them with a semicolon (example: :code:`0001.tif;0002.tif;0003.tif`).

Link
------------

You can also link to media that is hosted online. This can be a IIIF link (any derivative that ends with :code:`/full/full/0/default.jpg` will work as will any :code:`jp2`s). Media can also be hosted in other sites. Add all links to the relevant media column in your csv.

If there are multiple media files (ie multiple images to make up the object), then separate them with semicolons.

.. note::
    Regardless of whether you use the zip archive or a link, this step can be done using either of the spreadsheets (the AMI-compatible one or the initial human friendly one).


----------------------------------
Now that you have your csv...
----------------------------------

Time to ingest.

1. Go to :code:`/admin/content`.

2. Click "Start an AMI set".

3. Select "Spreadsheet Importer" for your plugin.

4. Select "Create New ADOs" for Operation. Upload the file in the dialog box.

5. Select "Direct" for data transformation approach. Select the columns where you added filenames or URLs (example: images, documents, etc.). You can select multiple.

6. When selecting Global ADO mappings, choose "ismemberof". For "Ado label", choose which column includes information that tells Archipelago what kind of media it is (most likely, this will be "type").

7. If you are using a zip file to upload content, upload the zip to the dialog box. If not, leave it blank. Then click to create the AMI set.

8. Once the set has been created, go to the "Process" tab and click "Confirm".