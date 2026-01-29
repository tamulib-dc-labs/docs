Batch Import into DSpace Using SAFCreator
=========================================

This document describes the step-by-step process for performing a batch import
into DSpace using **SAFCreator**, a tool developed by Texas A&M Libraries.
The workflow covers installing prerequisites, creating a SAF (Simple Archive Format)
package, importing items into DSpace, and adding thumbnails after ingestion.

Prerequisites
-------------

Before starting, ensure you have:

- Access to the target DSpace instance (e.g., OAKTrust)
- Metadata prepared in CSV format
- Content files organized in folders
- Administrative access (if required) to install software

Installing SAFCreator
---------------------

SAFCreator is a Java-based application used to generate SAF packages for batch import.

1. Download SAFCreator
^^^^^^^^^^^^^^^^^^^^^^

- Download the SAFCreator JAR file from GitHub:
  
  ::
  
     https://github.com/jcreel/SAFCreator

2. Verify Java Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

SAFCreator requires Java to be installed.

- Open a command prompt or terminal and run:

  .. code-block:: bash

     java -version

- If Java is installed, the version information will be displayed.
- If you see an error such as ``java: command not found``, Java is not installed.

3. Install Java (If Needed)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Download Java from the official site:

  ::
  
     https://www.java.com/en/download/manual.jsp

- Follow the installation instructions for your operating system.

.. note::

   If you are using a Texas A&M managed system, administrative access is required
   to install Java. Follow the instructions at the link below to obtain admin access:

   ::
   
      https://service.tamu.edu/TDClient/36/Portal/KB/ArticleDet?ID=774

Launching SAFCreator
--------------------

Once Java is installed, you can launch SAFCreator.

You may double-click the JAR file to launch the application.

Alternatively,
1. Open a command prompt in the directory containing the SAFCreator JAR file.
2. Run the following command:

   .. code-block:: bash

      java -jar -Dfile.encoding=UTF-8 SAFCreator-0.0.2-SNAPSHOT.one-jar.jar

Configuring the SAF Batch
-------------------------

After launching SAFCreator, you will be prompted to fill in three fields:

1. **Path to the metadata CSV file**
2. **Source Directory**
3. **Destination Directory**
   
.. image:: ../../_static/images/dspace_batch_import/safcreator.png
    :alt: SAFCreator

Source Directory
^^^^^^^^^^^^^^^^

The source directory contains the digital files associated with the batch.

- Files are typically retrieved from:
  
  - DPM (Digital Project Management) OneDrive, or
  - OKATrust Google Drive

If the files are stored in Google Drive:

1. Download the folder
2. Unzip it locally
3. Use the unzipped folder as the source directory

Loading the Batch
^^^^^^^^^^^^^^^^^

1. Select the CSV metadata file.
2. Select the source directory containing the content files.
3. Select the destination directory where the SAF output will be written.
4. Click **Load Specified Batch Now**.

.. image:: ../../_static/images/dspace_batch_import/safcreator_2.png
    :alt: Load specified batch

Verifying the Batch
-------------------

Once the batch is loaded:

1. Click **Batch Verification**
2. Select **VERIFY BATCH**
3. Review the verification results
4. Fix any reported errors before proceeding

.. image:: ../../_static/images/dspace_batch_import/safcreator_1.png
    :alt: Verify Batch

Writing SAF Data
----------------

After successful verification:

1. The **Write SAF Data Now** button will become enabled.
2. Click the button to export the SAF package to the destination directory.
3. Navigate to the destination directory.
4. Zip the contents of the SAF output directory.

.. image:: ../../_static/images/dspace_batch_import/safcreator_3.png
    :alt: SAFCreator Write

.. image:: ../../_static/images/dspace_batch_import/safcreator_4.png
    :alt: SAFCreator Finish Screen

.. image:: ../../_static/images/dspace_batch_import/compress_zip.png
    :alt: Compress files

Importing the SAF Package into DSpace
-------------------------------------

1. Log in to OAKTrust (DSpace).
2. Navigate to **Batch Import (ZIP)**.
3. Select the target collection for the items.
4. Upload the zipped SAF package.

.. important::

   Ensure **Validate Only** is **unchecked**.
   If checked, DSpace will only validate the batch and will not import the items.

5. Click **Proceed** to start the batch import process.

.. image:: ../../_static/images/dspace_batch_import/dspace_1.png
    :alt: SAFCreator

Reviewing Import Results
------------------------

After the process completes:

1. Click **Retrieve the Process Output**
2. Review the logs for:
   
   - Errors
   - Warnings
   - Failed items

Address any issues as needed.

Adding Thumbnails After Import
------------------------------

After items are successfully imported, thumbnails can be generated using a DSpace process.

1. Navigate to the **Process** tab in OAKTrust DSpace.
2. Create a new process.
3. Select the script: **Filter Media**

.. image:: ../../_static/images/dspace_batch_import/dspace_2.png
    :alt: SAFCreator

Process Parameters
^^^^^^^^^^^^^^^^^^

Add the following parameters:

- ``-i`` (identifier):  
  The value should be the **handle** of the collection or item.
- ``-force``:  
  Forces regeneration of thumbnails.

.. image:: ../../_static/images/dspace_batch_import/dspace_3.png
    :alt: SAFCreator

.. image:: ../../_static/images/dspace_batch_import/dspace_4.png
    :alt: SAFCreator

Starting the Process
^^^^^^^^^^^^^^^^^^^^

1. Review the parameters.
2. Start the process.
3. Monitor the process status for completion.

Once finished, thumbnails should be visible on the imported items.

.. image:: ../../_static/images/dspace_batch_import/dspace_5.png
    :alt: SAFCreator

---
