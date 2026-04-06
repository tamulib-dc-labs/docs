=====================
Modifying the Webform
=====================

AMI spreadsheet imports allow the admin to set whatever metadata fields they want, but this is not reflected in the default webform. If the admin wants to include a custom metadata field in an ADO upload using the webform, they can't.

This also raises issues when editing existing ADOs. There are three ways to edit an existing ADO:

* AMI batch update

* JSON edit

* Edit Descriptive Metadata webform

The webform is the most user-friendly option. However, if the ADO has metadata not in the default webform, the admin is unable to edit those fields. 

--------------------
How to start editing
--------------------

1. Go to :code:`/admin/structure/webform`.

2. From the list, locate the webform you wish to edit. Click "Build" at the right hand of the table.

3. You should now see a list of all fields included in that webform.

4. Click on "Source" to edit the webform as a yaml.