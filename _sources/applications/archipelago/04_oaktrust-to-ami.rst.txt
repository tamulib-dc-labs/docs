=======================
Migrating from OAKTrust
=======================

If you want to import a collection on OAKTrust into Archipelago, first you must download the collection and its metadata.

Go to OAKTrust > Export > Metadata and OAKTrust > Export > Batch Export (ZIP).

You will get a csv and a zip.

-------------------------------
Preparing the csv for migration
-------------------------------

* `Read this page to upload the output directly to Archipelago <https://tamulib-dc-labs.github.io/docs/applications/archipelago/01_ami-upload.html>`_.

* `Read this page if you wish to add linked data before uploading to Archipelago <https://tamulib-dc-labs.github.io/docs/applications/archipelago/02_flat-csv.html>`_.

----------------------
How to get your files?
----------------------

The field :code:`dc.description.provenance[en]` includes the filenames of all files associated with a specific digital object, among other information. You will need to extract the filename from this long string. 

To do this, you must find a pattern in the file naming structures. For example, the filenames might all start with "CMLJWC". Since you want the jp2 files, you can use the following regex pattern :code:`(r"(CMLJWC[^,\s]*?\.jp2)")`.

Create a new spreadsheet (input.csv) with a single column, :code:`dc.description.provenance[en]`. Rename it to "long_string" and run this code:

.. code:: python

    import csv
    import re

    INPUT_CSV = "input.csv"
    OUTPUT_CSV = "output.csv"

    SOURCE_COLUMN = "dc.description.provenance[en]"
    NEW_COLUMN = "image"

    # Regex: starts with CMLAGC, ends with .jp2
    pattern = re.compile(r"(CMLJWC[^,\s]*?\.jp2)")

    with open(INPUT_CSV, newline="", encoding="utf-8") as infile, \
        open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + [NEW_COLUMN]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            text = row.get(SOURCE_COLUMN, "")

            match = pattern.search(text)
            row[NEW_COLUMN] = match.group(1) if match else ""

            writer.writerow(row)

Replace :code:`dc.description.provenance[en]` on your original spreadsheet with the values of :code:`image` from the output.csv.

--------------------------
How to upload these files?
--------------------------

Because these values are being downloaded to your device, you will use a zip file to upload. Remember that zip files have a maximum size of 512MB, so you will likely need to split your migration into batches.

The files downloaded from OAKTrust utilize a lot of directories, but you only want the jp2s that you want to upload. Here is a script to take all jp2s from a folder and add them to a new folder.

.. code:: python
    
    import os
    import shutil

    SOURCE_DIR = "downloaded-collection"
    DEST_DIR = "downloaded-collection-jp2s-only"

    os.makedirs(DEST_DIR, exist_ok=True)

    for root, dirs, files in os.walk(SOURCE_DIR):
        for filename in files:
            if "jp2" in filename.lower() and "jpg" not in filename.lower():
                src_path = os.path.join(root, filename)

                # Handle duplicate filenames
                dest_path = os.path.join(DEST_DIR, filename)
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(dest_path):
                    dest_path = os.path.join(
                        DEST_DIR, f"{base}_{counter}{ext}"
                    )
                    counter += 1

                shutil.copy2(src_path, dest_path)

    print("Done.")

Your new folder will include all items in alphabetical order. However, it is likely the csv you downloaded (and the resulting :code:`image` column) are not sorted alphabetically. Use the sort function on Google Sheets to sort the entire spreadsheet by the values in the image column. This will make splitting your files into batches easier.

When making a zip with these files, make sure you select the files you want and right click to compress them. Do not compress the folder or else there may be an error when you try to ingest them.
