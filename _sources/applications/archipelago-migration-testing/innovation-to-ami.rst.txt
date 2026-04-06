===============================
Migrating Using Innovation Site
===============================

You can upload items so they are hosted on :code:`library.tamu.edu/innovation` when you try to bring them into Archipelago via AMI set. 

----------------------------------
Uploading files from your computer
----------------------------------

In the terminal go to 

:code:`ssh netid@access.library.tamu.edu`

Then go to the destination for your files.

:code:`/mnt/web_php_pre/innovation/your_folder`

On another terminal, go to the folder with the files you want to move. Once you are in that directory, move the jpgs and JPGs first.

:code:`scp *.JPG netid@access.library.tamu.edu:/mnt/web_php_pre/innovation/your_folder`

:code:`scp *.jpg netid@access.library.tamu.edu:/mnt/web_php_pre/innovation/your_folder`

If you have tiffs, convert them to jp2s. Then move them to the innovation folder.

:code:`scp *.jp2 netid@access.library.tamu.edu:/mnt/web_php_pre/innovation/your_folder`

--------------------------
Uploading Bookreader files
--------------------------

In the terminal go to 

:code:`ssh netid@access.library.tamu.edu`

Then go to the destination for your files.

:code:`/mnt/web_php_pre/innovation/your_folder`

On another terminal, go to the folder with yearbook files.

:code:`ssh netid@access.library.tamu.edu`

:code:`/mnt/aggie_yearbooks`

Select a yearbook and go to that directory.

:code:`cd yb19XX`

Copy the jp2 zip file to your innovation folder.

:code:`cp yb19XX_jp2.zip /mnt/web_php_pre/innovation/your_folder`

Back in the first terminal (the innovation folder):

:code:`unzip yb19XX_jp2.zip`

:code:`cd yb19XX_jp2`

:code:`find . -type f`

This will print all the files in the directory. To get them in an Archipelago-friendly format, copy this list to a text editor and reformat it so the files are URLs and separated by semicolons.
