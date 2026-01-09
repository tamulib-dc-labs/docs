================================
How to make a flat csv compatible with AMI batch import
================================

The spreadsheet template for Archipelago AMI batch import includes fields that require json strings/objects to be included in a single cell. For example all of this should go under the creator_lod field when doing a batch import in a single cell:

:code:`[{"name_uri":"http://id.loc.gov/authorities/names/n2001078880","role_uri":"http://id.loc.gov/vocabulary/relators/cre","agent_type":"personal","name_label":"Hogg, James Stephen, 1851-1906.","role_label":"Creator"},{"name_uri":"https://id.loc.gov/authorities/names/n82158463","role_uri":"http://id.loc.gov/vocabulary/relators/rcp","agent_type":"personal","name_label":"Ross, Lawrence Sullivan, 1838-1898","role_label":"Addressee"}]`

This is two items, each with 5 properties, all under the same field. Typing this out may be time-consuming and lead to mistakes, so here is a script that converts a spreadsheet that is easier to work with to the spreadsheet required for AMI imports.

----------------------------------
Input csv
----------------------------------

Enter your metadata into this csv.

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1wFw1fSr6OpSeNCX7tZDRjhPIfn_pdr7WgUT217FZQbs/edit?usp=sharing" height="400" width="800" frameborder="0" allowfullscreen></iframe>


Be sure to look at the first sheet (Human Friendly).

Add more columns if there need to be more metadata values per field (such as if you need to add more local subjects). However, the creator_lod fields need to be added in sets of 5 (agent_type, name_label, name_uri, role_label, and role_uri). All other fields with _uri and _label appear in pairs.


----------------------------------
Conversion
----------------------------------

Once you have the input csv, you can run this script to convert it to a csv compatible with Archipelago AMI batch import.

.. code:: python

    import csv
    import json
    import re

    INPUT_CSV = "input.csv"
    OUTPUT_CSV = "intermediate.csv"

    # --------------------
    # Helpers
    # --------------------

    def non_empty(val):
        return val is not None and str(val).strip() != ""

    def find_indexes(fieldnames, prefix, suffix):
        """
        Finds all numeric indexes for columns like:
        prefix{i}suffix
        """
        pattern = re.compile(rf"^{re.escape(prefix)}(\d+){re.escape(suffix)}$")
        indexes = set()

        for name in fieldnames:
            match = pattern.match(name)
            if match:
                indexes.add(int(match.group(1)))

        return sorted(indexes)

    def build_lcnaf_array(row, fieldnames, base):
        indexes = find_indexes(fieldnames, f"{base}_", "_label")
        results = []

        for i in indexes:
            label = row.get(f"{base}_{i}_label")
            uri   = row.get(f"{base}_{i}_uri")

            if non_empty(label):
                results.append({
                    "label": label,
                    "uri": uri
                })

        return results

    def build_date_created_edtf(row):
        date_obj = {}

        for key in ["date_type", "date_from", "date_to", "date_free"]:
            val = row.get(key)
            if non_empty(val):
                date_obj[key] = val.strip()

        return json.dumps(date_obj, ensure_ascii=False) if date_obj else "{}"

    # --------------------
    # Main
    # --------------------

    with open(INPUT_CSV, newline="", encoding="utf-8") as infile, \
        open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)

        # Normalize headers
        reader.fieldnames = [h.strip() for h in reader.fieldnames]

        fieldnames = [
            "node_uuid"
            "label",
            "type",
            "description",

            "creator",
            "creator_lod",

            "subject_loc",
            "subject_lcnaf_personal_names",
            "subject_lcnaf_corporate_names",
            "subject_lcnaf_geographic_names",
            "subject_lcgft_terms",
            "subject_wikidata",

            "subjects_local",
            "subjects_local_personal_names",

            "date_created",
            "date_created_edtf",

            "language",
            "ismemberof",
            "owner",
            "rights",
            "rights_statements",
            "resource_type",
            "digital_origin",
            "rights_statement_label",
            "rights_statement_uri",
            "physical_description_extent",
            "images"
        ]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:

            # ---- Creators ----
            creator_indexes = find_indexes(reader.fieldnames, "creator_", "")
            creators = [
                row.get(f"creator_{i}")
                for i in creator_indexes
                if non_empty(row.get(f"creator_{i}"))
            ]

            # ---- Creator LOD ----
            lod_indexes = find_indexes(reader.fieldnames, "creator_lod_", "_name_label")
            creator_lod = []

            for i in lod_indexes:
                prefix = f"creator_lod_{i}_"
                fields = {
                    "agent_type": row.get(prefix + "agent_type"),
                    "name_label": row.get(prefix + "name_label"),
                    "name_uri": row.get(prefix + "name_uri"),
                    "role_label": row.get(prefix + "role_label"),
                    "role_uri": row.get(prefix + "role_uri")
                }

                if any(non_empty(v) for v in fields.values()):
                    creator_lod.append(fields)

            # ---- Subject LOC ----
            loc_indexes = find_indexes(reader.fieldnames, "subject_loc_", "_label")
            subject_loc = []

            for i in loc_indexes:
                label = row.get(f"subject_loc_{i}_label")
                uri   = row.get(f"subject_loc_{i}_uri")

                if non_empty(label):
                    subject_loc.append({
                        "label": label,
                        "uri": uri
                    })

            # ---- LCNAF ----
            lcnaf_personal   = build_lcnaf_array(row, reader.fieldnames, "subject_lcnaf_personal")
            lcnaf_corporate  = build_lcnaf_array(row, reader.fieldnames, "subject_lcnaf_corporate")
            lcnaf_geographic = build_lcnaf_array(row, reader.fieldnames, "subject_lcnaf_geographic")

            # ---- LCGFT ----
            lcgft_indexes = find_indexes(reader.fieldnames, "subject_lcgft_terms_", "_label")
            subject_lcgft = []

            for i in lcgft_indexes:
                label = row.get(f"subject_lcgft_terms_{i}_label")
                uri   = row.get(f"subject_lcgft_terms_{i}_uri")

                if non_empty(label):
                    subject_lcgft.append({
                        "label": label,
                        "uri": uri
                    })
            # ---- Wikidata ----
            wikidata = build_lcnaf_array(row, reader.fieldnames, "subject_wikidata")

            # ---- Subjects local ----
            local_indexes = find_indexes(reader.fieldnames, "subjects_local_", "")
            subjects_local = [
                row.get(f"subjects_local_{i}")
                for i in local_indexes
                if non_empty(row.get(f"subjects_local_{i}"))
            ]

            # ---- Subjects local personal names ----
            local_personal_indexes = find_indexes(
                reader.fieldnames,
                "subjects_local_personal_names_",
                ""
            )

            subjects_local_personal = [
                row.get(f"subjects_local_personal_names_{i}")
                for i in local_personal_indexes
                if non_empty(row.get(f"subjects_local_personal_names_{i}"))
            ]

            # ---- Dates ----
            date_created_edtf = build_date_created_edtf(row)

            # ---- Write row ----
            writer.writerow({
                "node_uuid": row.get("node_uuid"),
                "label": row.get("label"),
                "type": row.get("type"),
                "description": row.get("description"),

                "creator": json.dumps(creators, ensure_ascii=False),
                "creator_lod": json.dumps(creator_lod, ensure_ascii=False),

                "subject_loc": json.dumps(subject_loc, ensure_ascii=False),
                "subject_lcnaf_personal_names": json.dumps(lcnaf_personal, ensure_ascii=False),
                "subject_lcnaf_corporate_names": json.dumps(lcnaf_corporate, ensure_ascii=False),
                "subject_lcnaf_geographic_names": json.dumps(lcnaf_geographic, ensure_ascii=False),
                "subject_lcgft_terms": json.dumps(subject_lcgft, ensure_ascii=False),
                "subject_wikidata": json.dumps(wikidata, ensure_ascii=False),

                "subjects_local": json.dumps(subjects_local, ensure_ascii=False),
                "subjects_local_personal_names": json.dumps(subjects_local_personal, ensure_ascii=False),

                "date_created": row.get("date_created"),
                "date_created_edtf": date_created_edtf,

                "language": row.get("language"),
                "ismemberof": row.get("ismemberof"),
                "owner": row.get("owner"),
                "rights": row.get("rights"),
                "rights_statements": row.get("rights_statements"),
                "resource_type": row.get("resource_type"),
                "digital_origin": row.get("digital_origin"),
                "rights_statement_label": row.get("rights_statement_label"),
                "rights_statement_uri": row.get("rights_statement_uri"),
                "physical_description_extent": row.get("physical_description_extent"),
                "images": row.get("images")
        })





