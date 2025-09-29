=======================
How to Process a Batch
=======================

The Digital Collections Department receives content for OpenONI through the cifs drive. Newspapers are uploaded in batches of several issues at a time. A batch will be structed as an entire folder for the batch, subfolders for each individual issue, and each page will be an image titled 0001.tif, 0002.tif, etc. 

There will also be one metadata spreadsheet per batch **or** one metadata spreadsheet for the entire newspaper collection (all batches).

The job of Digital Collections is to create a metadata spreadsheet from the previous spreadsheet(s) that includes the information needed for OpenONI ingest.

----------------------
Acquire program for batch processing
----------------------

Download `texas-aggie-batch-processing <https://github.com/tamulib-dc-labs/texas_aggie_batch_processing>`_. Texas Aggie is one of the newspapers processed by Digital Collections, but not the only one.

----------------------
Download metadata spreadsheet
----------------------

Go to the cifs drive and download the metadata spreadsheet for the batch you wish to work on. Drag the spreadsheet into the texas-aggie-batch-processing repository.

----------
Edit get_data.py
----------

:code:`get_data.py` will be altered every time you wish to use it.

.. code-block:: python
    import os
    from csv import DictReader, DictWriter
    # Batch Information
    path_to_texas_aggie_files = "/Volumes/digital_project_management/Texas Aggie"
    batch_folder = "Batch 3 Scans"
    final_csv_name = "texas_aggie_batch_data_new_3.csv"
    batch_title = "texas_aggie_batch_3"
    
    all_directories = []
    for path, dirs, files in os.walk(f"{path_to_texas_aggie_files}/{batch_folder}"):
    for dir in dirs:
        all_directories.append(dir)
    
    new_data = []
    with open("texas_aggie_batch_data.csv", 'r') as og_data:
        reader = DictReader(og_data)
        for row in reader:
            date = row.get('Date published')
            if len(date.split('-')) < 3:
                date = f"{date}-01"
            current_id = f"texasaggie_{date}"
            if current_id in all_directories:
                volume = row.get('Enumeration').split(':')[0].split('.')[-1]
                issue = row.get('Enumeration').split(':')[1].split('.')[-1]
                dir_path = f"/Volumes/digital_project_management/Texas Aggie/{batch_folder}/{current_id}/"
                pages = sum(
                    os.path.isfile(os.path.join(dir_path, f)) for f in os.listdir(dir_path)
                )
                item = {
                    "item": f"texasaggie_{date}",
                    "title": f"Texas Aggie. Vol. {volume}, No.{issue}",
                    "description": f"The {date} issue (Vol. {volume}, No. {issue}) of the Texas Aggie.; {pages} pages",
                    "date": date,
                    "volume": volume,
                    "issue": issue,
                    "edition": "1",
                    "pages": pages,
                    "ONI-ChronAm_Batch": batch_title
                }
                new_data.append(item)
                all_directories.remove(current_id)
    with open(final_csv_name, 'w') as new_sheet:
        writer = DictWriter(new_sheet, fieldnames=new_data[0].keys())
        writer.writeheader()
        writer.writerows(new_data)
    
    if len(all_directories) > 0 :
        print("These directories were missing and not added to the batch:")
        for item in all_directories:
            print(f"* {item}\n")

**Checklist of Changes**

* Change the :code:`path_to_texas_aggie_files` to the path to the newspaper you are working on. Get this folder name from the cifs drive. Even though the name "texas_aggie" is included in this variable, it will not affect the code if you are working with a different newspaper.
* Change :code:`batch-folder` to the name of the folder containing the batch you are working on. Get this folder name from the cifs drive.
* Change :code:`final_csv_name` to what you want the output spreadsheet to be called. An easy naming convention is :code:`{newspaper_name}_batch_data_{batch number}`.
* Change :code:`batch_title` to what you want the batch to be named. An easy naming convention is :code:`{newspaper_name}_batch_{batch number}`. This will appear in a column of the output spreadsheet.
* Change :code:`"texas_aggie_batch_data.csv"` to the name of the spreadsheet you downloaded from the cifs drive.

**Changes dependent on structure of data**

You may have to change other parts of the code depending on the structure of the data uploaded to the cifs drive.

* The date column on the original spreadsheet might not be titled "Date published". To make sure the processor pulls the date you want, either change the column name on the spreadsheet or change the code.
* Furthermore, on the original spreadsheet, the dates might not follow the YYYY-MM-DD format. Not only is this format used for naming the folders on cifs, but also this format is **required** for OpenONI. If the spreadsheet does not use this format, use Excel functions to set the dates to the format you want.
* If the folders on cifs do not follow the YYYY-MM-DD naming convention, you will need to edit the code to accomodate the naming convention. 
    * For example, a naming convention consisting of YYYYMMDD01 may require the creation of another column in the original spreadsheet. Name this new column :code:`date2` and use Excel functions to make all values follow the YYYYMMDD convention.
        * Add another line under :code:`date = row.get('Date published')`
        .. code-block:: python
            date = row.get('dc.date')
            date2 = row.get('date2')
        
        * Edit the :code:`dir_path` variable to include the other naming convention.
        .. code-block:: python
            dir_path = f"/Volumes/digital_project_management/Texas Aggie/{batch_folder}/{date2}01"
        
        * If some folders on cifs follow one convention and others follow the other, check to see if a directory exists before pulling from it.
        .. code-block:: python
            dir_path = f"/Volumes/digital_project_management/Texas Aggie/{batch_folder}/{current_id}"
            if os.path.isdir(dir_path):
                dir_path = dir_path
            else:
                dir_path = f"/Volumes/digital_project_management/Texas Aggie/{batch_folder}/{date2}01"

* Change the newspaper name in :code:`current_id` to the newspaper you are working with. :code:`current_id` assumes that the folder names include the name of the newspaper. If the folder names only include a date, remove the name of the newspaper from the formula.
* If the original spreadsheet does not include any data about the volume and issue numbers, comment out those lines and remove mention of the volumes and issues during the :code:`item` section of the code that gathers the data for the rows. 
* If the original spreadsheet does include volume and issue metadata, but the field is not separated by semicolons, replace the :code:`split(;)` with whatever punctuation was actually used.
* If the original spreadsheet does include volume and issue metadata but does not use the column name "Enumeration", either change the code to the column name used in the spreadsheet, or change the spreadsheet column name to "Enumeration".
    * If the volume and issue metadata are in a column with a name that is repeated (such as dc.description), you may want to change the spreadsheet, not the code, to avoid confusion.
    