===========================
Crosswalking: Avalon to ARK
===========================

Use this to create an ARK for an object on Avalon.

1. Create a json using the code avalon.py

2. Go to `this site <https://ezid.cdlib.org>`_

3. For each media object you will need the following metadata fields:

+-------------------+--------------------------+
| JSON field        | Corresponding ARK field  |
+===================+==========================+
| id                | Location (URL)           |
+-------------------+--------------------------+
| main_contributors | Who?                     |
+-------------------+--------------------------+
| title             | What?                    |
+-------------------+--------------------------+
| date_digitized    | When?                    |
+-------------------+--------------------------+

The Location (URL) is made using the id field, but not exclusively the id. It should follow this format:

avalon.library.tamu.edu/media_objects/{'id'}