========================================
Generating Service Files and Derivatives
========================================

The images we serve to users in our various repositories are all handled by an image server called Cantaloupe.
Cantaloupe takes a file from DSpace or Fedora and generates a tiled image and a thumbnail from the base asset stored in
the repository. These processes are resource intensive and can greatly affect the experience of our users. This process
is especially affected by the quality, size, and type of file. For that reason, we serve high quality lossy files from
our preservation files based on current best practices and research.

Note worthy documents used in this decision making include:

* `High Throughput JPEG 2000 (HTJ2K): Algorithm, Performance and Potential <https://www.htj2k.com/wp-content/uploads/white-paper.pdf>`_
* `Generating lossy access JP2s from lossless preservation masters <https://bitsgalore.org/2022/03/30/generating-lossy-access-jp2s-from-lossless-preservation-masters.html>`_
* `Evaluating HTJ2K as a Drop-In Replacement for JPEG2000 with IIIF <https://journal.code4lib.org/articles/17596>`_
* `Technical Requirements for Digitized Page Images Submitted to HathiTrust <https://www.hathitrust.org/member-libraries/resources-for-librarians/contributor-toolkit/technical-requirements-page-images/>`_

-----------------------------
Preferences for Service Files
-----------------------------

HTJ2K
=====

While we don’t use this format yet since Cantaloupe 5.0.6 cannot process these, we acknowledge that this is the best
format for performance and service file use. We will closely watch developments with HTJ2K and Cantaloupe and adopt
accordingly when support is more widely available.

Lossy JP2
=========

Much research has been done showing that lossy JP2 is best in quality, performance, and speed.  Thus we create lossy
JP2s with grok or kakadu for service files.

JPG
===

High quality JPGs are acceptable but less desirable than lossy JP2s.

---------------------
Generating Lossy JP2s
---------------------

Lossy JP2s can be generated from a directory of images using `an in-house written program <https://github.com/markpbaggett/quick_convert>`_
like so:

.. code-block:: shell

    markcovert path -t jp2 -p path/to/files -o /path/to/output/destination

This application wraps many command line utilities and is capable of creating a large number of qualities and formats.
When creating lossy JP2s, it effectively does this for each file:

.. code-block:: shell

    kdu_compress -i input.tiff -o output.jp2 Creversible='yes' Qfactor=90 ORGgen_plt=yes Corder=RPCL Cprecincts="{256,256}" Cblk="{64,64}" Clevels=8

--------------------
Files for HathiTrust
--------------------

We do not send TIFFs to HathiTrust either.  Instead, we follow their requested practices and send JP2s according to
their standard.  Also, we use grok for this to align with their processes and we copy existing data from the
preservation files using exiftool and check the preservation files with jhove.  Using modern grok and python, that
equates to doing:

.. code-block:: python

    import os
    import subprocess
    from tqdm import tqdm
    tifs_path = "/Volumes/digital_project_management/Ranchers Roundup/1988/TIFF"
    jp2s_path = f'{tifs_path.split("/TIFF")[0]}/JP2s'
    jhove_path = f'{tifs_path.split("/TIFF")[0]}/JHOVE'
    jp2s_path = os.path.expanduser(jp2s_path)
    jhove_path = os.path.expanduser(jhove_path)
    os.makedirs(jp2s_path, exist_ok=True)
    os.makedirs(jhove_path, exist_ok=True)
    for path, dirs, files in os.walk(tifs_path):
        for file in tqdm(files):
            command = [
                "grk_compress",
                "-i", f"{tifs_path}/{file}",
                "-o", f"{jp2s_path}/{file.replace('tif', 'jp2')}",
                "-n", "5",
                "-p", "RLCP",
                "--sop",
                "--eph",
                "-M", "62",
                "-I",
                "-q", "32"
            ]
            subprocess.run(command)
            exif_command = [
                "exiftool",
                "-tagsfromfile",
                "@",
                "-srcfile",
                f"{jp2s_path}/{file.replace('tif', 'jp2')}",
                f"{tifs_path}/{file}",
                "-XMP:format=",
                "-ImageHistory=Technical metadata values were copied (via exiftool) from the original TIFF to this derivative JP2.",
                "-EXIF:ColorSpace=",
                "-overwrite_original"
            ]
            subprocess.run(exif_command)
            jhove_command = [
                "jhove",
                "-h",
                "xml",
                f"{jp2s_path}/{file.replace('tif', 'jp2')}"
            ]
            with open(f"{jhove_path}/{file.replace('tif', 'xml')}", "w") as output_file:
                subprocess.run(jhove_command, stdout=output_file)

---------------------------------
Generating Thumbnails with Pillow
---------------------------------

If uploading a collection to DSPACE, you will often want thumbnails so that you don't have to run an additional process.
Arguably, this should be added to the same utility above, but if you want another approach where you just get thumbnails
for certain files for a particular project, Pillow might be useful.

For instance, say we had a directory of PDFs that also had image files and we wanted to generate a thumbnail from the first
page of the PDF.  Something like this might be useful:

.. code-block:: python

    from csv import DictWriter, DictReader
    from PIL import Image
    import os

    year = "1988"
    with open(f"charity_{year}.csv", 'r') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            pdf = row['filename'].split('/')[-1]
            directory = row['filename'].split('/')[0]
            page = pdf.split('_')[-1].split('-')[0]
            zfilled = page.zfill(4)
            thumbnail_path =  f"/Volumes/digital_project_management/Ranchers Roundup/{year}/thumbs/"
            jp2_path = f"/Volumes/digital_project_management/Ranchers Roundup/{year}/JP2s/"
            os.makedirs(thumbnail_path, exist_ok=True)
            with Image.open(f"{jp2_path}{zfilled}.jp2") as img:
                img.thumbnail((200, 200))
                img.save(f"{thumbnail_path}{zfilled}.jpg")

