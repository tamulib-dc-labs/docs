==========================
Making Transcripts with WhisperX 
==========================

1. Enter the following code into the terminal: :code:`pip install whisperx`.

2. In that same respository, add a folder of your source files.

3. Enter the following prompt into the terminal: 

:code:`whisperx {filepath} --model turbo --output_dir output`

You may need more commands depending on what you want from WhisperX.

------------------
Special prompts:
------------------

If the audio is in a language other than English, append the following code to your command prompt:

:code:`--language {Language_Name}`

To add diarization, append the following code: 

:code:`--diarize`

To help diarization, append the following code:

:code:`--min_speakers {Number} --max_speakers {Number}`

Keep in mind that commercials, announcements, and narrators are also considered speakers.

---------------
WhisperX output
---------------

As output, five files will be generated: .json, .srt, .tsv, .txt, and .vtt

To move the json and vtt to `whisper-editor <https://github.com/tamulib-dc-labs/whisper-reviewer>`_, make sure you have the following add-to-json.py downloaded.

.. code:: python
    
    from csv import DictReader
    import os
    import json
    import shutil
    json_file_data = "/Users/{Username}/whisper-reviewer/public/test_for_whisper_transcript_online.json"
    all_data = []
    
    with open(json_file_data, "r") as my_json:
    audio_file_data = json.load(my_json)
    with open("mycsv.csv", "r") as my_file:
    reader = DictReader(my_file)
    for row in reader:
        if row['Title'] != "":
            all_data.append(
                {
                    "uin": row['UIN'],
                    "title": row['Title'],
                    "audio": row['Audio']
                }
            )
    for path, directories, files in os.walk("output"):
        for file in files:
            if ".json" in file:
                identifier = file.split('.json')[0]
                name = [item["title"] for item in all_data if item['uin'] == identifier][0]
                full_name = f"{name} whisperx"
                audio_file_location = [item["audio"] for item in all_data if item['uin'] == identifier][0]
                audio_file_data.append(
                    {
                        "audio": audio_file_location,
                        "url": f"./transcripts/{file}",
                        "name": full_name
                    }
                )
                shutil.move(f"{path}/{file}", "/Users/{Username}/whisper-reviewer/public/transcripts")
                with open(json_file_data, "w") as f:
                    json.dump(audio_file_data, f, indent=4)
            elif '.vtt' in file:
                shutil.move(f"{path}/{file}", "/Users/{Username}/whisper-reviewer/vtts/{output-folder}")

---------------
Automate Transcription 
---------------

Instead of running a command for every item you wish to transcribe with WhisperX, use a script that transcribes all items in a directory.

.. code:: python
    import subprocess
    import os


    def process_dropbox(input_directory, output):
        for path, directories, files in os.walk(input_directory):
            for filename in files:
                if ".sha256" not in filename:
                    subprocess.run([
                        "whisperx",
                        f"{path}/{filename}",
                        "--model",
                        "turbo",
                        "--output_dir",
                        output,
                        "--compute_type",
                        "float32",
                        "--language",
                        "en",
                    ])


    if __name__ == "__main__":
        directories_to_process = (
            "/Users/username/path/to/directory",
        )
        output_directory = "output"
        for input_dir in directories_to_process:
            process_dropbox(input_dir, output_directory)
