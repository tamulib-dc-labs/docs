=================
Creating new ADOs
=================

In Archipelago, there are three ways to upload a new Archipelago Digital Object.

1. Webform (Go to :code:`/node/add`)

2. JSON file (Go to :code:`/node/add-list/super_admin_raw_json`)

3. AMI spreadsheet batch upload

This guide pertains the third of these, batch upload via spreadsheet.

---------------------------------
Create an csv compatible with AMI
---------------------------------

To upload with a spreadsheet, you must create a spreadsheet compatible with Archipelago. Column names vary greatly once Archipelago has been customized to the institution, but below is the template compatible with default Archipelago settings:

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1Ye87dCTkpneR-ELk_nCwPWaFMrofP9qpcEYO-ChUNqc/edit?usp=sharing" height="400" width="800" frameborder="0" allowfullscreen></iframe>

If there are multiple values for any column, cells will have json strings such as:

:code:`[{"uri": "http://id.loc.gov/authorities/names/n2001078880", "role_uri": "http://id.loc.gov/vocabulary/relators/cre", "value": "Hogg, James Stephen, 1851-1906.", "role": "Creator"},{"uri": "https://id.loc.gov/authorities/names/n82158463", "role_uri": "http://id.loc.gov/vocabulary/relators/rcp", "value": "Ross, Lawrence Sullivan, 1838-1898", "role": "Addressee"}]`

This is an :code:`agent_linked_data` example for an item with 2 creators. 

To avoid having to write complex json strings for linked data, `read this page on creating a more human-readable, "flat" csv <https://tamulib-dc-labs.github.io/docs/applications/archipelago/07_linked-data-multivalue.html>`_.

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
This tells Archipelago what type of item you are working with so it knows what template to use. For a full list of TAMU types, read the `documentation on ADO types <https://tamulib-dc-labs.github.io/docs/applications/archipelago/04_ado-types.html>`_.


What is label?
--------------
Label will usually be the title of the digital object.

-------------------------------------------
What about my images/documents/audio/video?
-------------------------------------------

For each row, you will add the files under the corresponding column (images, documents, audio, video, etc). This can be either a filename (if uploading from your computer) or a link (if your image is already hosted elsewhere). If you have multiple files that should go under the same column, separate them with a semicolon.

.. note::
    You must add your files upon import. You can add metadata later through an AMI update. You cannot upload metadata first and add files later unless you upload files individually through the digital object's webform.

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

To attach files in a zip file to a digital object, enter the filename in the relevant column depending on what type of media it is (for example, the :code:`images` column). 

.. note::
    If you are using MacOS, your zip file can only have one level (so you cannot have something like :code:`item-1/0001.tif`).

Link
----

You can also link to media that is hosted online. This can be a IIIF link (any derivative that ends with :code:`/full/full/0/default.jpg` will work as will any :code:`.jp2`). Media can also be hosted in other sites. Add all links to the relevant media column in your csv.

If a digital object is made up of multiple files, list them all and separate them with semicolons.

---------------------
Importing through AMI
---------------------

1. Go to :code:`/admin/content`.

2. Click "Start an AMI set".

3. Select "Spreadsheet Importer" for your plugin.

4. Select "Create New ADOs" for Operation. Upload the csv in the dialog box.

5. Select "Direct" for data transformation approach. Select the columns where you added filenames or URLs (example: images, documents, etc.). You can select multiple.

6. When selecting Global ADO mappings, choose "ismemberof" and/or "ispartof". For "Ado label", choose "label".

7. If you are using a zip file to upload content, upload the zip to the dialog box. If not, leave it blank. Then click to create the AMI set.

8. Once the set has been created, go to the "Process" tab and click "Confirm".