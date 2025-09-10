=============================
Downloading media from Avalon
=============================
Use if you are trying to download video/audio files or if you need to pull down metadata stored on Avalon.

-------------
First method
-------------

This method requires that you have an API key and access to the access.library.tamu.edu server. It is faster than the second method.

1. Use `this code <https://github.com/jameswsullivan/automation/blob/main/Python/fetch-avalon-assets-by-collection-via-ssh.py>`_ 

2. Install ffmpeg, paramiko, and python. (Instructions for download are in the code.)

3. Enter AVALON_API_KEY (your API key) and AVALON_HOST_URL. If pulling from Avalon Prod, it should look like :code:`AVALON_HOST_URL = r'https://avalon.library.tamu.edu'`

4. Enter SSH_HOSTNAME and SSH_PORT: :code:`SSH_HOSTNAME = 'access.library.tamu.edu'` and :code:`SSH_PORT = 22`.

5. Enter SSH_USERNAME and SSH_PASSWORD.

6. Enter AVALON_MOUNT PATH: :code:`AVALON_MOUNT_PATH = '/mnt/avalon_prod'`. This will be different if you are pulling from Avalon Pre.

7. Go to the collection and copy the string after the AVALON_HOST_URL.

8. In a terminal, run the program followed by the string from the AVALON_HOST_URL. For example: :code:`python fetch-avalon-assets-by-collection 123456abcdef`


--------------
Second method
--------------

This method requires that you have an API key.

1. Open mark_get_avalon_files.py. Make sure your API key is connected on Line 14. 

2. Go to the collection and copy the string after https://avalon.library.tamu.edu.

3. Scroll to the bottom of the code, to the last paragraph. Paste the string for the variable :code:`collection`. Under :code:`example`, specify whether it is prod or pre.

4. Create a folder where you would like the files downloaded to. Enter the file path under :code:`example.download_best_files`.

5. If you only want a spreadsheet with metadata taken from Avalon, comment out the lines related to downloading files.

6. Run the program by typing :code:`python mark_get_avalon_files.py` into the terminal.

