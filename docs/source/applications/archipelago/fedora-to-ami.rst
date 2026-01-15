===============================================
Getting AMI-compatible spreadsheets from Fedora
===============================================

If you want to import a collection on Fedora into Archipelago, use the following script:

.. code:: python

    import json
    import requests
    from csv import DictWriter

    csv_data = []
    unique_values = []
    final_data = []

    collection_url = "https://api.library.tamu.edu/iiif-service/fedora/collection/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps"
    collection_response = requests.get(collection_url)
    collection_json = collection_response.json()

    # Safely get manifests
    manifests = collection_json.get('manifests', [])
    if not manifests:
        raise RuntimeError("No manifests found at collection URL")

    for manifest in manifests:
        manifest_response = requests.get(manifest.get('@id'))
        manifest_json = manifest_response.json()

        files = []

        item = {
            'title': manifest_json.get('label', ''),
            'description': manifest_json.get('description', ''),
        }

        # --- Metadata (IIIF v2) ---
        for metadata in manifest_json.get('metadata', []):
            label = metadata.get('label')
            value = metadata.get('value')

            if label is None:
                continue

            # Keep lists as JSON; scalars as-is
            if isinstance(value, list):
                item[label] = json.dumps(value)
            else:
                item[label] = value

            if label not in unique_values:
                unique_values.append(label)

        # --- Files from canvases ---
        for canvas in manifest_json.get('sequences', [])[0].get('canvases', []):
            try:
                files.append(canvas['images'][0]['resource']['@id'])
            except (KeyError, IndexError):
                continue

        item['files'] = json.dumps(files)
        csv_data.append(item)

    # --- Normalize rows so all columns exist ---
    for row in csv_data:
        for label in unique_values:
            if label not in row:
                row[label] = ""
        final_data.append(row)

    if not final_data:
        raise RuntimeError("No data collected — final_data is empty")

    # --- Build CSV headers safely ---
    fieldnames = set()
    for row in final_data:
        fieldnames.update(row.keys())

    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = DictWriter(csvfile, fieldnames=sorted(fieldnames))
        writer.writeheader()
        for row in final_data:
            writer.writerow(row)

The script reads all IIIF manifests in a Fedora collection, extracts the metadata labels and values and puts them in a spreadsheet.

----------------------
Things to keep in mind
----------------------

* :code:`collection_url` should be in this format :code:`https://api.library.tamu.edu/iiif-service/fedora/collection/uuid`.

* This spreadsheet is not automatically compatible with AMI. Some metadata column names need to be changed depending on the labels used in the IIIF manifests.

* Double check the :code:`derivatives` column. Ensure that each canvas is separated by a semicolon. Also, if semicolons are used in the canvas (ie uri is in hexadecimal and end with :code:`;1`, :code:`;2`, :code:`;3`, etc.), this will not work.  

* Create the collection in Archipelago so you can link the parent uuid.

* `Generate your own uuids <https://www.uuidgenerator.net/>`_ for the node_uuid column.

* If you want to add linked data, you will need some intermediate steps.

    * Add columns depending on what values you want to link. Every linked data value will require two columns: a label and a uri.

    * `How to make a flat csv and convert it back into an AMI-compatible csv <https://tamulib-dc-labs.github.io/docs/applications/archipelago/creating-ami-csv.html>`_

* This is the only way to get metadata and derivatives for a Fedora collection if you don't have the IIIF manifests downloaded to your device.