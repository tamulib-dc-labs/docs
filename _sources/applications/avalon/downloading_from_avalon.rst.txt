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

1. Download `pyavalon <https://github.com/tamulib-dc-labs/pyavalon>`_.

2. In the terminal, type :code:`get_file_ids_from_a_collection -c "{collection id}" -i {pre or prod} --download -f {file output directory} -o {output.csv}`

-----------------------------
Downloading Large Collections
-----------------------------

Sometimes, a collection will be so large, any attempt to download it will result in an error. To work around this issue, you must download only part of the collection at a time.

In the terminal type:

:code:`pyavalon get_file_ids_from_a_collection -c "{collection id}" -i prod --download -u {Your_Username} -f output-folder --get_range --start 1 --end 1`

It is advised you go page by page to avoid crashes. To do this, make sure the start and end of the range are the same.


---------------------------------------------
Downloading Large Collections With Less Steps
---------------------------------------------

To make a collection download without having to run pyavalon dozens of times, you can use code to automatically repeat pyavalon.

Use the following code: 

.. code-block:: python

    from time import sleep
    import subprocess
    import argparse

    parser = argparse.ArgumentParser(prog="Batch Avalon")
    parser.add_argument("--collection", "-c", help="Specify Collection")
    parser.add_argument("--instance", "-i", help="Pre or Prod")
    parser.add_argument("--file", "-f", help="folder where audio/video files will be saved")
    parser.add_argument("--start", "-s")
    parser.add_argument("--end", "-e")
    parser.add_argument("--output", "-o", help="output csv filename")
    args = parser.parse_args()

    current = int(args.start)
    end = int(args.end)

    while current <= end:
        print(f"Downloading Page {current}")
        command = [
            "pyavalon",
            "get_file_ids_from_a_collection",
            "-c", 
            args.collection,
            "-i", 
            args.instance,
            "--download",
            "-u",
            "cbarr",
            "-f",
            args.file,
            "--get_range",
            "--start",
            str(current),
            "--end",
            str(current),
            "-o",
            f"temp_{current}.csv"
        ]
        subprocess.run(command)
        current += 1
        print("Taking a quick nap!")
        sleep(10)

This will result in downloading the entire collection to a folder. Furthermore, an output.csv will be created for each page that has been downloaded.