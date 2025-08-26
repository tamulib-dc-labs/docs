===========================
Importing media into Avalon via API Key
===========================
How to upload transcripts and pdfs of media already hosted on Avalon.

---------------------
Use the following code - :code:`batch_upload_captions.py`
---------------------
.. code-block:: python
    import csv
    import requests
    import os
    # --- CONFIG ---
    BASE_URL = "https://avalon.example.edu"   # your Avalon server
    API_TOKEN = "API Token"      # replace with real token
    CSV_FILE = "input.csv"       # mapping file
    CAPTION_FOLDER = "./vtts"    # folder with .vtt files
    # --- HEADERS ---
    headers = {
        "Authorization": f"Token token={API_TOKEN}"
    }
    # --- PROCESS CSV ---
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            media_id = row["media_id"]
            caption_file = row["caption_file"]

            file_path = os.path.join(CAPTION_FOLDER, caption_file)
            if not os.path.exists(file_path):
                print(f"File not found: {file_path}")
                continue

            with open(file_path, 'rb') as f:
                files = {
                    'file': (caption_file, f, 'text/vtt')
                }
                response = requests.post(
                    f"{BASE_URL}/media_objects/{media_id}/supplemental_files",
                    headers=headers,
                    files=files
                )

            if response.status_code == 200:
                print(f"Uploaded {caption_file} to {media_id}")
            else:
                print(f"Failed for {media_id}: {response.status_code} {response.text}")

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