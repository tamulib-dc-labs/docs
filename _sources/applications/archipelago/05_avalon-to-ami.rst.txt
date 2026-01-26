=====================
Migrating from Avalon
=====================

If you want to import a collection on Avalon into Archipelago, first you must download the collection and its metadata using `pyavalon <https://github.com/tamulib-dc-labs/pyavalon>`_.

`Here is a guide on downloading entire collections from Avalon <https://tamulib-dc-labs.github.io/docs/applications/avalon/downloading_from_avalon.html>_`.

-------------------------------
Preparing the csv for migration
-------------------------------

* `Read this page to upload the output directly to Archipelago <https://tamulib-dc-labs.github.io/docs/applications/archipelago/ami-upload.html>`_.

    * Be sure you set :code:`type` to :code:`AudioObject` or :code:`VideoObject`.

* `Read this page if you wish to add linked data before uploading to Archipelago <https://tamulib-dc-labs.github.io/docs/applications/archipelago/creating-ami-csv.html>`_.

-----------------
Linking to Avalon
-----------------

To link between your Archipelago object and the original Avalon object, you will use the :code:`website_url` column. You can acquire the Avalon urls for each digital object by using the :code:`CONCAT` function. For example:

:code:`=CONCAT("https://avalon.library.tamu.edu/media_objects/",[cell containing the work id of the item]")`

--------------------------
How to upload these files?
--------------------------

Because these values are being downloaded to your device, you will use a zip file to upload. Remember that zip files have a maximum size of 512MB, so you will likely need to split your migration into batches.

