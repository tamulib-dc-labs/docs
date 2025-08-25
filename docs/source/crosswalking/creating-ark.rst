===========================
Creating ARKs with TAMU ID Minter
===========================

Use this to create an ARK for an object. ARKs are created with `this site <https://ezid.cdlib.org>`_

Create an input.csv. For each media object you will need the following metadata fields:

+-------------------+--------------------------+
| .csv metadata     | Corresponding ARK field  |
+===================+==========================+
| id/url            | Location (URL)           |
+-------------------+--------------------------+
| creator           | Who                      |
+-------------------+--------------------------+
| title             | What                     |
+-------------------+--------------------------+
| date of creation  | When                     |
+-------------------+--------------------------+


When working with items in Avalon that don't yet have a url, the Location (URL) is made using the id field, but not exclusively the id. It should follow this format:

avalon.library.tamu.edu/media_objects/{'id'}

If an item already has a url (such as one on Fedora), use that for the url (the where).

Use `tamu-id-minter <https://github.com/tamulib-dc-labs/tamu-id-minter>`_ to create the ARKs.

In the terminal enter :code:`tamu_mint create_arks -i input.csv`.

-------------------
Editing the Status of an ARK
-------------------

ARKs can be public for items that are already online or they can be reserved for items that will later be made public. To change the status of an ARK:

Make sure input.csv includes a column labeled "ark".

In the terminal enter :code:`tamu_mint switch_statuses -s {public, reserved, or unavailable} -i input.csv`.