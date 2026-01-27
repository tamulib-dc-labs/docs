=====================
Migrating from Avalon
=====================

If you want to import a collection on Avalon into Archipelago, first you must download the collection and its metadata using `pyavalon <https://github.com/tamulib-dc-labs/pyavalon>`_.

`Here is a guide on downloading entire collections from Avalon <https://tamulib-dc-labs.github.io/docs/applications/avalon/downloading_from_avalon.html>_`.

-------------------------------
Preparing the csv for migration
-------------------------------

* `Read this page to upload the output directly to Archipelago <https://tamulib-dc-labs.github.io/docs/applications/archipelago/01_ami-upload.html>`_.

    * Be sure you set :code:`type` to :code:`AudioObject` or :code:`VideoObject`.

* `Read this page if you wish to add linked data before uploading to Archipelago <https://tamulib-dc-labs.github.io/docs/applications/archipelago/02_flat-csv.html>`_.

-----------------
Linking to Avalon
-----------------

To link between your Archipelago object and the original Avalon object, you will use the :code:`website_url` column. You can acquire the Avalon urls for each digital object by using the :code:`CONCAT` function. For example:

:code:`=CONCAT("https://avalon.library.tamu.edu/media_objects/",[cell containing the work id of the item]")`

--------------------------
How to upload these files?
--------------------------

Because these values are being downloaded to your device, you will use a zip file to upload. Remember that zip files have a maximum size of 512MB, so you will likely need to split your migration into batches.

---------------------------
Adding Transcripts/Captions
---------------------------

You can add transcripts and captions to an item by using the "transcripts" and "captions" columns on the template. However, after you create the AMI set but before you process it, go to the "Edit" tab. Scroll down to the "Edit Config and associated data" box.

It should look like this:

.. code:: json

    "AudioObject": {
            "metadata": "direct",
            "metadata_config": {
                "template": "11"
            },
            "bundle": "digital_object:field_descriptive_metadata",
            "files": []
        }

Or like this: 

.. code:: json

    "VideoObject": {
            "metadata": "direct",
            "metadata_config": {
                "template": "11"
            },
            "bundle": "digital_object:field_descriptive_metadata",
            "files": []
        }

Replace the empty :code:`files[]` with the following:

.. code:: json

    "files": [
    {
      "source": "audio",
      "type": "original"
    },
    {
      "source": "transcript",
      "type": "transcript",
      "mimetype": "text/vtt",
      "label": "English transcript"
    }
  ]

Or with this:

.. code:: json

    "files": [
    {
      "source": "video",
      "type": "original"
    },
    {
      "source": "captions",
      "type": "caption",
      "mimetype": "text/vtt",
      "label": "English captions"
    }
  ]

This lets Archipelago connect the transcript to audio or caption to video. 

.. note::

    AudioObject must be a mp3. If you upload mp4s, Archipelago thinks you have a video, even though you set the type as AudioObject. Your "video" won't show up in the audio player, but it appears under the Download dropdown menu. If you change the object type to VideoObject, the file will show up in the video player, but it will not be in sync with the transcript.