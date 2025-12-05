Batch Importing SAFs Using the DSpace Command Line
==================================================

This section describes how to batch-import Simple Archive Format (SAF) packages
into DSpace using the command-line importer. The importer processes a directory
of prepared SAFs and deposits each item into the specified collection.

Prerequisites
-------------

Before running a batch import, ensure that:

- You have access to Rancher and the proper clustion (dev, pre, prod).
- You have shell access to the DSpace workload (dspace-cli-saf-import).
- Your user account has permissions to submit to the target collection.
- Your SAF packages follow the required DSpace directory structure.
- You know the UUID of the collection you are importing into.

Basic Command Structure
-----------------------

The DSpace CLI import tool is typically invoked as follows:

.. code-block:: bash

   /dspace/bin/dspace import \
       -a \
       -e "mark.baggett@tamu.edu" \
       -c COLLECTION-UUID \
       -s PATH-TO-SAF-DIRECTORY \
       -m PATH-TO-METADATA-REPORT-FILE.txt

Parameter Breakdown
-------------------

``-a``
   Add items (as opposed to replacing or deleting).

``-e``
   Email address of the DSpace user who will be recorded as the submitter.

``-c``
   UUID of the target collection.

``-s``
   Path to the directory that contains your SAF packages.

``-m``
   Path to the metadata results log that will be generated after the import.
   This file keeps a record of imported item handles and any errors.

Example
-------

The following example imports a directory of SAF packages (``batch_3_with_rights``)
into a collection with UUID ``57726e26-c609-4d10-a717-4f5292bc7c24`` while logging
the results to ``batch_3_import_prod_yo.txt``:

.. code-block:: bash

   /dspace/bin/dspace import \
       -a \
       -e "mark.baggett@tamu.edu" \
       -c 57726e26-c609-4d10-a717-4f5292bc7c24 \
       -s batch_3_with_rights \
       -m batch_3_import_prod_yo.txt

After running the command, review the output log to confirm the handles assigned
to each imported item and check for any warnings or errors.

