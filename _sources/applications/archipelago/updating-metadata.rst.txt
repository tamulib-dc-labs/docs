================================
How to bulk update metadata
================================

----------------------------------
Download the existing metadata
----------------------------------

First, you need to know the metadata you already have and the :code:`node_uuid`s of each item you wish to update. The easiest way to get this information is by downloading the metadata as a csv.

1. Go to :code:`/admin/content`.

2. Select all items you wish to update.

3. Scroll to the bottom of the page. Make sure you select "Export Archipelago Digital Objects to CSV content item". Then click "Apply to selected items".

----------------------------------
Edit the metadata
----------------------------------

Change the metadata you want in the spreadsheet.

Delete any columns you are not changing. However you must keep:

* Any columns where the data was changed.

* :code:`node_uuid`

* :code:`label`

* :code:`type`

----------------------------------
Uploading the spreadsheet with changes
----------------------------------

1. Go to :code:`/admin/content`.

2. Click "Start an AMI set".

3. Select "Spreadsheet Importer" for your plugin.

4. Select "Update Existing ADOs" for Operation. Upload the csv in the dialog box.

5. Select "Direct" for data transformation approach. Select the columns where you added filenames or URLs (example: images, documents, etc.). You can select multiple. 

    a. If you are not changing any files, do not select anything.

6. When selecting Global ADO mappings, choose "ismemberof". For "Ado label", choose which column includes information that tells Archipelago what kind of media it is (most likely, this will be "type").

    a. If you are not changing any parent-child relationships, **do not select anything**.

    b. Under ADO mappings, ADO UUID, select :code:`node_uuid`.

7. Click to create the AMI set.

8. Once the set has been created, go to the "Process" tab and make sure you have the option checked that will not alter your existing files. Click "Confirm".