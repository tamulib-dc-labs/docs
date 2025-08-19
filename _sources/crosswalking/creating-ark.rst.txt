===========================
Creating ARKs
===========================

Use this to create an ARK for an object. ARKs are created with `this site <https://ezid.cdlib.org>`_

Create a .csv. For each media object you will need the following metadata fields:

+-------------------+--------------------------+
| .csv metadata     | Corresponding ARK field  |
+===================+==========================+
| id/url            | Location (URL)           |
+-------------------+--------------------------+
| creator           | Who?                     |
+-------------------+--------------------------+
| title             | What?                    |
+-------------------+--------------------------+
| date of creation  | When?                    |
+-------------------+--------------------------+


When working with items in Avalon that don't yet have a url, the Location (URL) is made using the id field, but not exclusively the id. It should follow this format:

avalon.library.tamu.edu/media_objects/{'id'}

If an item already has a url (such as one on Fedora), use that for the url (the where).

Use the script ark-creator.py. Change the input_csv to the .csv you created with the who, what, and when.