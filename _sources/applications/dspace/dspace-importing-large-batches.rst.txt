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
- You have scp'd or rsync'd your files to the server via access.library.tamu.edu.

Copying a SAF Import to the Access Server
-----------------------------------------

The access server is what the Libraries uses as its jump / mount point for most running containers.

To get write access to the server, you must `submit a help desk request <https://helpdesk.library.tamu.edu/default_kace.php>`_
and choose *Submit a Computer or Software Problem*.  If you don't do this, you can't get your files to the remote server.

Once you have write access, you can save your files to :code:`access.library.tamu.edu:/mnt/nfstmp/oaktrust-saf-import`.

Most people create their own areas on the server to hold files.  For instance, I use :code:`/mnt/nfstmp/oaktrust-saf-import/mark_imports`.

You need to be sure that you on the access server and the default user on the container running in Rancher can read, write,
and execute. If you don't do this, your import will fail.  To make this easiest you can just use **777** on your files.

Now that you have background information, you can follow these steps:

========================
1. Create your file area
========================

.. code-block:: bash

    # Connect to Server
    ssh netid@access.library.tamu.edu
    # Make a Directory at the Mount Point
    mkdir /mnt/nfstmp/oaktrust-saf-import/mark_imports
    # Make sure you can write
    chmod 777 -R /mnt/nfstmp/oaktrust-saf-import/mark_imports

===========================
2. Copy Files to the Server
===========================

.. code-block:: bash

    scp -r my-saf-import-on-my-computer netid@access.library.tamu.edu:/mnt/nfstmp/oaktrust-saf-import/mark_imports

===========================
3. Double Check Permissions
===========================

.. code-block:: bash

    chmod 777 -R /mnt/nfstmp/oaktrust-saf-import/mark_imports/my-saf-import-on-my-computer

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

