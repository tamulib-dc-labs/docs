====================================
Remediating Failed Imports in Avalon
====================================

Everyone makes mistakes—and when importing into Avalon, mistakes often show up as failed rows.
This guide explains how remediation works, highlights common errors, and shows how to fix them.

-----------------
About Remediation
-----------------

When you upload an Avalon batch ingest sheet, Avalon processes each row independently:

- **Valid rows** are ingested successfully.
- **Invalid rows** fail with an error message.

Because successful rows are ingested immediately, you must take care to avoid creating duplicates when retrying.

When a batch partially fails, Avalon sends an email like this:

.. line-block::

    Initial processing of your batch ingest failed. Details are below. Please see the Batch Ingest Package Format for further help.

    To replay this batch, please rename your spreadsheet to e25eb36f-c874-4895-bd60-3613ee97440e_Caitlyn Sheet - Sheet3.csv and reupload it after making desired changes. Only unpublished items can be updated via this method. Retain all rows in the spreadsheet including those that have no changes.

    The following rows of your spreadsheet failed:
    Row     Error
    3       File unknown attribute 'file_' for MediaObject.
    4       File unknown attribute 'file_' for MediaObject.
    5       File unknown attribute 'file_' for MediaObject.

    The following rows of your spreadsheet successfully completed:
    Row     Media Object ID
    6       gh93gz665

To remediate:

1. Correct the failed rows in your spreadsheet.
2. Rename the file exactly as instructed in the error message (:code:`e25eb36f-c874-4895-bd60-3613ee97440e_Caitlyn Sheet - Sheet3.csv`).
3. Re-upload the revised file.

.. note::
   Always keep **all rows**, including successful ones, in the resubmitted sheet.
   Avalon will ignore the already-ingested rows and only update the failed ones.

-------------
Common Errors
-------------

File unknown attribute ``file_`` for MediaObject
===============================================

This error means Avalon encountered a column header it does not recognize.
In the example above, the column was labeled ``File `` (with a trailing space) instead of ``File``.

**How to fix:**

- Check your column headers carefully.
- Ensure they match the required names in the `Batch Ingest Package Format <https://avalonmediasystem.org/>`_.
- Remove extra spaces or typos.
- Remember that some fields (like ``File`` and ``Label``) can appear multiple times if repeatable—but they must be spelled **exactly**.

