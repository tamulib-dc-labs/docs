==========================
DSPACE: Importing Entities
==========================
For this, you will need python, poetry shell, and a code editor.

------------------------
Clone relevant git repository
------------------------
* `To move journals from OJS to OakTrust (ojs-to-oaktrust) <https://github.com/markpbaggett/ojs-to-oaktrust>`_

------------------------
New .yml
------------------------

Go to default-config.yml. The code should look like the following:

.. code-block::  python
    journal_title:
        url: https://{title}-tamu.tdl.org/{title}
        token: "api-key"
        oai_endpoint: https://{title}-tamu.tdl.org/{title}/oai
        output_directory: "output"
        title: "Journal Title"
         default_thumbnail: "https:://{default}/{thumbnail}.{ext}"
         date: "2008-2016"
        description: "Description"
        subjects:
             - Motion pictures -- History
             - Motion pictures
             - Motion pictures, Mexican
             - Motion pictures, Spanish
        alternative: ""


Copy default-config.yml and rename the new copy config.yml.

Then, log into OJS and get an API key. To do this, go to Edit Profile > API key. Copy the key.

Inside config.yml, paste the API key for :code:`token`.

Fill in :code:`journal_title`, :code:`url`, :code:`oai_endpoint`, :code:`title`, :code:`default_thumbnail`, :code:`date`, :code:`description`, :code:`subjects`, and :code:`alternative`.  :code:`default_thumbnail` should be a link to an image. :code:`subjects` should come from Library of Congress subject headings. :code:`alternative` should only be used for an alternative title.

------------------------
Creating .csv file
------------------------

Under :code:`ojs-to-oaktrust`, create a new directory called :code:`output`.

On the command line, write:

.. code-block::  shell
    python src/ojsnake.py -j journal_title

articles.csv, issues.csv, title.csv, and volumes.csv should have saved under :code:`ojs-to-oaktrust/output/journal_title` folder.

------------------------
Creating Simple Archive Format (SAF) Files
------------------------

Run Java in terminal.

.. code-block:: shell
    java -jar ~/Downloads/SAFCreator-0.0.2-SNAPSHOT.one-jar.jar

This should open a dialogue box called DSpace Simple Archive Format Creator.

You need a folder for the SAF output. Because there will be four folders created per journal, it is recommended you first make a folder called oaktrust-batches. 
Then create the folder for output from a single execution of SAF. An easy naming convention is "journal_name-unit". "unit" can be articles, issues, volumes, or title. 
You will do this process four times per journal.

In the dialogue box:

* Select one of the .csv files. The unit of the .csv file should match the unit of the folder you just created for output.
* Select source files directory. This can be any directory that is not involved with this transfer process (such as the :code:`/Desktop`). It doesn't really matter.
* Select SAF output directory. Select the new folder you just created called "journal_name-unit"
* Click "Load specified batch now!"
* Go to Batch Verification across the top and click "Verify Batch."
* Create SAF file (rightmost button under Batch Details).

------------------------
Importing SAF Files
------------------------

Create a zip file. When using a Mac, this must be done through command line or else it will give errors later.

.. code-block:: shell
    zip -r {journal_name}-title.zip {journal_name}-title

Go to * `Oaktrust <https://oaktrust-pre.library.tamu.edu>`_ Log in with Shibboleth. 
On the sidebar, go to Import > Batch Import. When asked for a collection, select "Journals". Upload zip file. 

Note: Sometimes "Import" does not appear as an option in the sidebar, in which case you must wait/reload the page until it appears.

------------------------
Creating Child Unit of Parent Unit
------------------------

This will follow mostly the same process as before. However, once the csv files generate, you will need to go to the websites for the parent unit and copy all characters in the url after the last slash. 
Then go to the child unit's .csv and add that string at the end of each line after the last comma (creating another column). Make sure all children with the same url are from the same parent. 
This will link the child to the parent.
