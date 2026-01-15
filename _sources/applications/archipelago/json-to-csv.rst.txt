==============================================================
How to convert IIIF manifests into spreadsheets for AMI ingest
==============================================================

This is how to take a directory of IIIF manifests, extract metadata and derivatives, and create a working spreadsheet that can later be converted into an AMI-compatible spreadsheet. This method works with both v2 and v3 IIIF manifests.

--------------------------------------------------
Use this derivative and metadata extraction script
--------------------------------------------------


.. code:: python

    import json
    import csv
    import os
    from collections import defaultdict

    SUFFIX = "/full/full/0/default.jpg"

    # Canonical CSV fields
    METADATA_FIELDS = [
        "dc.source",
        "creator",
        "contributor",
        "subject",
        "rights",
        "format",
        "language",
        "title",
        "type",
        "extent",
        "created",
        "abstract",
        "spatial",
        "Description",
        "Created On",
        "In Scope",
    ]

    # Normalized lookup map (lowercase → canonical)
    FIELD_LOOKUP = {
        "dc.source": "dc.source",
        "creator": "creator",
        "contributor": "contributor",
        "subject": "subject",
        "rights": "rights",
        "format": "format",
        "language": "language",
        "title": "title",
        "type": "type",
        "extent": "extent",
        "created": "created",
        "date": "created",          # common IIIF variant
        "abstract": "abstract",
        "description": "Description",
        "spatial": "spatial",
        "created on": "Created On",
        "in scope": "In Scope",
    }


    def find_matching_strings(data, matches=None):
        if matches is None:
            matches = []

        if isinstance(data, dict):
            for value in data.values():
                find_matching_strings(value, matches)
        elif isinstance(data, list):
            for item in data:
                find_matching_strings(item, matches)
        elif isinstance(data, str):
            if data.endswith(SUFFIX):
                matches.append(data)

        return matches


    def extract_langmap_text(obj):
        """
        Extract text from IIIF language maps:
        { "none": ["text"] }, { "en": ["text"] }, etc.
        """
        if not isinstance(obj, dict):
            return []

        values = []
        for v in obj.values():
            if isinstance(v, list):
                values.extend(v)
            else:
                values.append(v)

        return [str(v).strip() for v in values if v]


    def normalize_label(label_raw):
        """
        Normalize label to canonical METADATA_FIELDS entry.
        """
        if isinstance(label_raw, str):
            label = label_raw.strip()
        elif isinstance(label_raw, dict):
            texts = extract_langmap_text(label_raw)
            label = texts[0] if texts else ""
        else:
            return None

        key = label.lower().strip()
        return FIELD_LOOKUP.get(key)


    def normalize_metadata(metadata):
        """
        Normalize IIIF metadata into:
        { canonical_label: [value1, value2, ...] }
        """
        normalized = defaultdict(list)

        if not isinstance(metadata, list):
            return normalized

        for entry in metadata:
            if not isinstance(entry, dict):
                continue

            canonical_label = normalize_label(entry.get("label"))
            if not canonical_label:
                continue

            value_raw = entry.get("value")

            if isinstance(value_raw, list):
                values = [str(v).strip() for v in value_raw]

            elif isinstance(value_raw, dict):
                values = extract_langmap_text(value_raw)

            elif value_raw is not None:
                values = [str(value_raw).strip()]

            else:
                values = []

            for v in values:
                normalized[canonical_label].append(v)

        return normalized


    def process_directory(json_dir, output_csv):
        rows = []
        max_counts = defaultdict(int)

        for filename in sorted(os.listdir(json_dir)):
            if not filename.lower().endswith(".json"):
                continue

            json_path = os.path.join(json_dir, filename)

            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                continue

            label_raw = data.get("label", "")
            label_value = ""

            if isinstance(label_raw, str):
                label_value = label_raw.strip()
            elif isinstance(label_raw, dict):
                texts = extract_langmap_text(label_raw)
                label_value = texts[0] if texts else ""

            row = {
                "filename": filename,
                "label": label_value
            }


            metadata = normalize_metadata(data.get("metadata", []))

            for field in METADATA_FIELDS:
                values = metadata.get(field, [])

                for i, value in enumerate(values, start=1):
                    col_name = f"{field}_{i}"
                    row[col_name] = value
                    max_counts[field] = max(max_counts[field], i)

            derivatives = find_matching_strings(data)
            row["derivatives"] = ";".join(derivatives)

            rows.append(row)

        # Build CSV header
        header = ["filename", "label"]

        for field in METADATA_FIELDS:
            for i in range(1, max_counts[field] + 1):
                header.append(f"{field}_{i}")

        header.append("derivatives")

        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(header)

            for row in rows:
                writer.writerow([row.get(col, "") for col in header])


    if __name__ == "__main__":
        process_directory("path/to/jsons", "output.csv")

------------------
Intermediate steps
------------------

Open the output spreadsheet in Google Sheets. You will need to make it follow the format of the spreadsheet described `here <https://tamulib-dc-labs.github.io/docs/applications/archipelago/creating-ami-csv.html>`_. Here are the list of things you need to edit/fix/verify:

* Add a :code:`node_uuid` column and generate uuids with `uuidgenerator.net <https://www.uuidgenerator.net/>`_.

* Add a :code:`ismemberof` column. The value for each row should be the node_uuid for the parent collection.

* To add linked data, you will need to divide your creators and contributors into different types of columns. Note that creator and contributor are not distinguished except in the :code:`creator_lod` columms, which ask for a role.

    * Use :code:`creator_lod_{i}_agent_type`, :code:`creator_lod_{i}_name_label`, :code:`creator_lod_{i}_name_uri`, :code:`creator_lod_{i}_role_label`, and :code:`creator_lod_{i}_role_uri` for creators/contributors that have authority files. 
   
    * For local names use, :code:`creator_{i}` fields.

* To add linked data, you will need to divide your subjects into different types of columns.

    * Use :code:`subject_lcnaf_personal_{i}_label` and :code:`subject_lcnaf_personal_{i}_uri` when the subject is a person.

    * Use :code:`subject_lcnaf_corporate_{i}_label` and :code:`subject_lcnaf_corporate_{i}_uri` when the subject is a corporate entity.

    * Use :code:`subject_loc_{i}_label` and :code:`subject_loc_{i}_uri` for other subjects.

    * Use :code:`subjects_local_personal_names_{i}` when the subject is a person and not in LCNAF.

    * Use :code:`subjects_local_{i}` when the subject is not a person and not in LCSH.

* To add linked data, you will need to convert the :code:`spatial` field into geographic LCNAF headings.

    * Use :code:`subject_lcnaf_geographic_{i}_label` and :code:`subject_lcnaf_geographic_{i}_uri` for each spatial term.

* Add a :code:`type` column with the worktype the items are. This is so Archipelago knows what template to use for your digital object.

* Rename certain columns.

    * :code:`rights_1` to :code:`rights`
    
        * Add an adjacent column called :code:`rights_statements`. The values should be the **text** for that rights statement. :code:`rights` should be the url.

    * :code:`format_1` to :code:`digital_origin`

    * :code:`language_1` to :code:`language`

        * To ensure compatibility with Archipelago, make sure the values are the full name(s) of the language(s). For example, use :code:`English` instead of :code:`eng`.

    * :code:`extent_1` to :code:`physical_description_extent`

    * :code:`created_1` to :code:`date_created`

    * :code:`abstract_1` to :code:`description`

    * :code:`derivatives` to :code:`image`

* Delete certain columns

    * :code:`filename`

    * :code:`title_1`

    * :code:`Description_1`

    * :code:`Created_On`

    * :code:`In_Scope`