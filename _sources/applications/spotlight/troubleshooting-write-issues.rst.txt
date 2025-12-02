============================
Troubleshooting Write Issues
============================

Occasionally, you may encounter situations where certain aspects of a Spotlight exhibit
cannot be modified. This document describes known issues, their causes, and steps
to resolve them.

.. contents::
   :local:
   :depth: 2

-------------------------------
Cannot Update Exhibit Thumbnail
-------------------------------

When configuring the ``Exhibit thumbnail``, Spotlight may fail silently. You may upload
a new image or select an existing one, click **Save**, and the thumbnail simply does not
change.

A common cause of this issue is incorrect filesystem ownership: the user running the
Rails application (e.g., ``app.app``) does not have permission to write to the uploads
directory.

To fix this, ensure that the application user owns the directory:

.. code-block:: bash

   sudo chown -R app:app /home/app/webapp/public/uploads

After correcting the ownership, thumbnail updates should begin working
normally.

-------------------------------------
Verifying Directory Permissions (Unix)
-------------------------------------

If updating thumbnails still fails, verify that directory permissions allow the
application user to write to the upload directory.

.. code-block:: bash

   ls -ld /home/app/webapp/public/uploads
   ls -l  /home/app/webapp/public/uploads

Ensure the directory shows the expected owner and permissions. If the directory is
owned by a numeric UID/GID (e.g., ``121:121``), this often indicates that files were
created by a container or a mismatched deployment user.

You can ensure writable permissions by running:

.. code-block:: bash

   sudo chmod -R u+rwX /home/app/webapp/public/uploads

----------------------------------
Checking Application and Rails Log
----------------------------------

Silent failures often produce useful messages in the Rails production log. Inspect the
log while performing the upload:

.. code-block:: bash

   tail -f /home/app/webapp/log/production.log

or

.. code-block:: bash

   tail -f /home/app/webapp/log/development.log

-------------------------------------------
Confirming the Upload Path in Your Install
-------------------------------------------

The default Spotlight upload path is typically:

``public/uploads``
