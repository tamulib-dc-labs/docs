===========================
Importing media into Avalon via API Key
===========================
How to upload transcripts and pdfs of media already hosted on Avalon.

---------------------
Create a input.csv
---------------------
You only need two columns, media_id and caption_file. media_id can be found in the URL for a particular item using the structure :code:`https://avalon-pre.library.tamu.edu/media_objects/{API_TOKEN}`. Note that if you are uploading to Avalon Pre, this will be different from "parent object" that may exist on items uploaded to Avalon Prod.

---------------------
Enter information into :code:`batch_upload_captions.py`. 
---------------------
* For :code:`BASE_URL`, enter the URL for the Avalon server. For TAMU, it will either be :code:`https://avalon-pre.library.tamu.edu` or :code:`https://avalon.library.tamu.edu`.
* For :code:`API_TOKEN`, enter :code:`os.getenv("AVALON_PRE")`. Make sure you have an API key stored as an environmental variable for this to work.
* For :code:`CSV_file`, enter :code:`input.csv`.
* For :code:`CAPTION_FOLDER`, enter the location of the vtts, such as :code:`./vtts`.

---------------------
Run the code
---------------------
Type :code:`python batch_upload_captions.py` into the Terminal.