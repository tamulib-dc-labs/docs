==========================
Making Transcripts with Whisper
==========================

For this, you will need python, poetry, and a code editor.

------------------------
Clone relevant git repositories.
------------------------

* `To transcribe audio with Whisper (tamu-whisper) <https://github.com/tamulib-dc-labs/tamu-whisper.git>`_
* `To edit captions (whisper-reviewer) <https://github.com/tamulib-dc-labs/whisper-reviewer.git>`_

---------------
Import files.
---------------

Open tamu-whisper. Create a new folder called :code:`all_source_files`.
Using the code editor, open the folder where you keep the audio files you will be working with. 
In the case of VSCode, go to File > Open Folder to import them. Imported files should save to :code:`all_source_files` folder.

-------------
Transcribing
-------------

Each transcription through Whisper will create 2 files: a vtt file with the captions and timestamps and a json file that provides estimates for the accuracy of each word.

Whisper allows for six settings that change the dataset the AI draws from. From smallest to largest, the models are tiny, base, small, medium, turbo, and large.
Turbo is recommended because it provides high quality transcriptions and does not take too long. (For example, turbo will take about 10-15 minutes to transcribe a 30 minute audio file.)

If transcribing many files, it is recommended to create smaller folders (:code:`folder_subdivision`) within :code:`all_source_files` to place a selection of audio files so transcription can be done in batches. 
This is because the transcribing program takes a lot of energy and can take about an hour to transcribe 5 30-minute audio files using turbo.

To transcribe, enter the following in the command line:

.. code-block:: shell

    tamuwhisper transcribe -d all_source_files/folder_subdivision -c "YourLastName, YourFirstName" -m [model]

When this is complete, all jsons and vtts should appear under the :code:`output/` folder in :code:`tamu-whisper`.

---------
Editing vtts
---------

To edit the vtts, first they must be moved to :code:`whisper-reviewer`. In :code:`tamu-whisper`, create a new :code:`.py`` file called :code:`move_files_to_reviewer`. 

.. code-block:: python

    from csv import DictReader
    import os
    import shutil
    import json

    json_file_data = "whisper-reviewer/public/test_for_whisper_transcript_online.json"
    all_data = []

    with open(json_file_data, "r") as my_json:
        audio_file_data = json.load(my_json)

    with open("science_fiction_radio_show_original inventory&metadata.csv", "r") as my_file:
        reader = DictReader(my_file)
        for row in reader:
            if row['Title'] != "":
                all_data.append(
                    {
                        "uin": row['\ufeffUIN'],
                        "title": row['Title']
                    }
                )

    for path, directories, files in os.walk("output"):
        for file in files:
            if "c000507" in file:
                identifier = file.split('_access')[0]
                name = [item["title"] for item in all_data if item['uin'] == identifier][0]
                full_name = f"{name}"
                audio_file_location = ""
                for item in audio_file_data:
                    if identifier in item["url"]:
                        audio_file_location = item['audio']
                        break

                if '.json' in file:
                    with open(json_file_data, 'r') as f:
                        current_data = json.load(f)
                    current_data.append(
                        {
                            "audio": audio_file_location,
                            "url": f"./transcripts/{file}",
                            "name": full_name
                        }
                    )
                    shutil.move(f"{path}/{file}", "whisper-reviewer/public/transcripts")
                    with open(json_file_data, "w") as f:
                        json.dump(current_data, f, indent=4)
                elif '.vtt' in file:
                    shutil.move(f"{path}/{file}", "whisper-reviewer/vtts")


Within this code, you will need to edit all paths to files that begin with "whisper-reviewer" to begin with your username, depending on where you saved it.
For example, the last file path may need to be written as :code:`/Users/yourUsername/Desktop/whisper-reviewer/vtts`.

Open :code:`whisper-reviewer`. There should be folders for :code:`vtts/` and :code:`public/`. Within :code:`public/`, there is a folder :code:`public/transcripts/` and a json file :code:`test_for_whisper_transcript_online.json`.
The json file will be used to build a temporary website that hosts the audio files with synchronized captions, allowing for easier review.

Go back to :code:`tamu-whisper` so you can run the program to move the files. In command line, write:

.. code-block:: shell

    python move_files_to_reviewer.py

All files in the :code:`output/` folder will disappear because they have been moved out of :code:`tamu-whisper` and into :code:`whisper-reviewer`. 
The :code:`test_for_whisper_transcript_online.json` file should have items added. For each .json file moved over, each corresponding audio file will be added to the site.
The code will appear as a series of three data within a bracket: the :code:`"audio"` (link to url for a specific file), :code:`"url"` (path to get to corresponding json file), and :code:`"name"` (title given to audio file). 

In whisper-reviewer, open :code:`vtts/` folder and select a newly changed file. In VSCode, the most recently added files will be green. Edit the file.

--------
Uploading Transcript
--------

Once you are done uploading transcripts, you will need to push it onto github.
Do this series of commands:

.. code-block:: shell

    git checkout -b new_branch_name
    git add vtts/
    git add public/
    git commit -m 'changes you made'
    git push origin new_branch_name


