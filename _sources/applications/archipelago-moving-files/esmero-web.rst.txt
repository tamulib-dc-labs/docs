==========================
Migrating Using Esmero Web
==========================

You can upload items so they are hosted on :code:`https://digitalcollections.library.tamu.edu/sites/default/files` when you try to bring them into Archipelago via AMI set. 

----------------------------------
Uploading files from your computer
----------------------------------

Clone the `kubectl-recurse-copy <https://github.com/tamulib-dc-labs/kubectl-recurse-copy>`_ repository on Github.

Create a folder in the repository. Move all files you hope to upload there.

Run the following code

:code:`uv run cp.py [path/to/folder_with_files] [pod key] /var/www/html/web/sites/default/files -n archipelago`

------------------------------
Deleting files from esmero web
------------------------------

Esmero Web has a limit on space, so files that are already uploaded can be deleted.

Go to Rancher Prod, then to prod-apps-cluster, then to Workloads. Click esmero-web, the three dots on the side, then Execute Shell. 

Once inside the shell, type :code:`cd /var/www/html/web/sites/default/files`.

Remove selected files.

------------------------
Example filepath for csv
------------------------

:code:`https://digitalcollections.library.tamu.edu/sites/default/files/filename.jp2`