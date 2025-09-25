=============================
How to make a PDF transcript to upload to Avalon.
=============================

This page explains how to generate pdfs for a collection of objects using existing metadata already on Avalon and a folder of .vtts with the transcripts.

1. Download existing metadata by using `pyavalon <https://github.com/tamulib-dc-labs/pyavalon>`_.

2. In the terminal enter :code:`pyavalon get_file_ids_from_a_collection -c "{collection id}" -i {pre or prod}`. 

3. A .csv will generate with metadata for the title, creator, contributor, date, rights information, publisher, subjects, derivative file, a parent work file id, a file id, a file title, and a work title.

4. Create your own :code:`{collection-name}-pdfs.csv`. Include the following columns:

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1gSdG4xnoWT_RWQCOsYCdpVVmXSixpUW6ufwTPSAN8l0/edit?gid=0#gid=0" height="400" width="1200" frameborder="0" allowfullscreen></iframe>


5. Use the function pdf-build.py. Change the :code:`collection_title` and the line below it to have the name of your collection and csv you just created. Make sure you have a folder for your pdfs to save and change the :code:`output_filename` and the vtt location.

6. Run :code:`python pdf-build.py`. 

7. To upload to Avalon, look at the documentation `Importing media into Avalon via API Key <https://tamulib-dc-labs.github.io/docs/applications/avalon/api-batch-upload.html>`_. PDFs can only be imported through the API key, never through spreadsheets.