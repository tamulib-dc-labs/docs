==========================
DSPACE: Importing Entities
==========================

How to do batch imports in OAKTrust

------------------------
Clone relevant git repository
------------------------

Download `ojs-to-oaktrust <https://github.com/markpbaggett/ojs-to-oaktrust>`_

------------------------
Create .csv file
------------------------

Create a csv file with metadata. You may receive one already made by someone else.

Example csv:

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1QMv0_PxooY3H9_pQotWBztOftrJAgidfa7CQOGYpf6E/edit?usp=sharing" height="400" width="1200" frameborder="0" allowfullscreen></iframe>


* If you are importing a title, volumes, or issues, do not use the bundle:ORIGINAL column. This is only used to attach specific files for individual articles or other digital items.
* bundle:THUMBNAIL can be a filepath or a link on the web.
* Only use one of the following (or none): relation.isJournalIssueofPublication, relation.isJournalVolumeofIssue, relation.isJournalofVolume. This is how you link back to the parent.

------------------------
Creating Simple Archive Format (SAF) Files
------------------------

Run Java in terminal by entering this code: :code:`java -jar ~/Downloads/SAFCreator-0.0.2-SNAPSHOT.one-jar.jar`

This should open a dialogue box called DSpace Simple Archive Format Creator.

You need a folder for the SAF output. Because there will be multiple folders created per journal, it is recommended you first make a folder called oaktrust-batches. 
Then create the folder for output from a single execution of SAF. An easy naming convention is "journal_name-unit". "unit" can be articles, issues, volumes, or title. 
You will do this process at least four times per journal. You may need to do it more (divide articles into smaller batches) if the journal has a lot of articles.

In the dialogue box:

* Select one of the .csv files. The unit of the .csv file should match the unit of the folder you just created for output.
* Select source files directory. The bundle:ORIGINAL and bundle:THUMBNAIL filepaths are relative to the source files directory.
* Select SAF output directory. Select the folder you just created under "oaktrust-batches".
* Click "Load specified batch now!"
* Go to Batch Verification across the top and click "Verify Batch."
* Create SAF file (rightmost button under Batch Details).

------------------------
Importing SAF Files
------------------------

Create a zip file. When using a Mac, this must be done through command line or else it will give errors later.

Create a zip file in terminal using this format: :code:`zip -r {folder}.zip {folder}`

Go to * `Oaktrust <https://oaktrust-pre.library.tamu.edu>`_ Create a collection for the journal. On the sidebar, go to Import > Batch Import. Select the collection you just created and upload the zip file. 

Note: Sometimes "Import" does not appear as an option in the sidebar, in which case you must wait/reload the page until it appears.

------------------------
Creating Child Unit of Parent Unit
------------------------

This will follow the same process. However, you will need to go to the site for the parent unit and put the end of the url into one of the relation columns. 
This will link the child to the parent.