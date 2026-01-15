=======================================
Importing media into Avalon via API Key
=======================================

How to upload transcripts and pdfs of media already hosted on Avalon.

----------------------------
Download relevant repository
----------------------------
`pyavalon <https://github.com/tamulib-dc-labs/pyavalon>`_.

---------------------------------
Download relevant Avalon metadata
---------------------------------

In the terminal, enter :code:`pyavalon get_file_ids_from_a_collection -c "{id of the collection}" -i {pre or prod}`.

This will generate an output.csv with the following columns: "Parent work", "Creator", "Contributor", "File id", "File title", "Work title", "Subject", "Rights", "Identifier", "Publisher", and "derivative".

----------------
Create input.csv 
----------------

Create an input.csv with four columns: id, filename, label, and type. 
 * id should be the same as the File id in the previous output.csv
 * filename should be a filepath. If importing pdfs, the filename must start with /Users.
 * label is the name you want the file to appear with when it's online. It is recommended for the label to be "Captions in English" or "Transcript in English".
 * type can only be caption, transcript, or pdf.

----------------
Push into Avalon
----------------

In the terminal, enter :code:`pyavalon upload-supplemental-files -i {pre or prod} -c "{path to .csv file}"`.
