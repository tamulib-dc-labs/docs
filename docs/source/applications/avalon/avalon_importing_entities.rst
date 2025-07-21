===============
Importing media into Avalon
===============

--------------------
Creating a Collection
--------------------

1. Log into Avalon. Go to the menu bar at the top. Click "Manage", and from the drop down list, click "Manage Content".

2. Click on the "Create Collection" button at the top right.

------------------
Importing a batch
------------------

1. Click on the "Create An Item" button. Make sure you are under "Manage files" on the menu on the left side of the screen.

2. You will use the Dropbox to import a batch. To import a batch, make sure you have access to :code:`cifs/avalon-pre` or :code:`cifs/avalon-prod`. A new folder should have been automatically generated with the same name as the collection you just created. Create a subfolder within that folder with a label like "Content". Drag and drop all media files you would like to upload into the new subfolder, both audio/video and transcripts.

--------------------
Creating a .xslx spreadsheet
--------------------

To import a batch, you must create a metadata table.

Use `this table <https://tamulib-dc-labs.github.io/docs/applications/avalon/metadata.html>`_ for guidance on metadata fields and column labels. 

* You must include **either** "Bibliographic ID" and "Bibliographic ID Label" columns **or** "Other Identifier Type" and "Other Identifier" columns. If you use "Other Identifier" make sure you put "local" under the "Other Identifier Type" and then the local identifer under "Other Identifier".
* The table should include a column for "File". This should be a filepath relative to the automatically generated folder. If you used the name "Content" for the subfolder, the file path may look like :code:`content/file_name`.
* Adjacent to the right of "File" there should be a column called "Label". This will be a label for each audio/video file.
* You need a "Date Issued" column. Dates should follow YYYY-MM-DD format. If the day is unknown, stop after the month. If the month is unknown, add an "X" after the year (YYYYX). If part of the year is unknown, add an X for the digits you don't know (YYYX). If the entire date is unknown write "unknown/unknown".
* Add title.
* If you have transcripts, they should go under the same row as their corresponding audio/video file. Similar to "File" and "Label" for the A/V file, a transcript will need adjacent "Transcript File" and "Transcript File Label" columns. "Transcript File" should be a filepath such as :code:`content/transcript_file_name`.

--------------------
Uploading through Dropbox
--------------------

1. When the .xlsx spreadsheet is complete, place it under the automatically generated folder for the collection in the :code:`cifs/avalon-pre/collection_name` or :code:`cifs/avalon-prod/collection_name` drive (not under :code:`cifs/avalon_pre/collection_name/content` or :code:`cifs/prod/collection_name/content`).

2. Drag and drop the .xlsx spreadsheet into the cifs drive. It should automatically disappear. Eventually, you will get an automatically generated email saying the metadata table passed the requirements. Later, you will receive a second automatically generated email telling you the metadata on the table passed standards. If your table didn't pass the standards, fix it and upload it to the cifs drive again.

3. Once you get the second email, you can import the batch in Dropbox. Select all materials from :code:`content`. Note that if you are using a older version of Avalon, you cannot upload transcripts yet.

--------------------
Publishing
--------------------

To publish the items you uploaded, go to Manage > Manage Content. Click on your collection, then select "List All Items". Select all items you wish to publish. Then, go to the "Selected Items" option on the menu, and click on the "Publish" button.

--------------------
Updating Access Control
--------------------

To change the access of some items, go to Manage > Manage Content. Click on your collection, then select "List All Items". Select all items you wish to change access for. Then, go to the "Selected Items" option on the menu, and click on the "Update Access Control" button.
