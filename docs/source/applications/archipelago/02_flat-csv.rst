=================================
Using an intermediate, "flat" csv
=================================

The spreadsheet template for Archipelago AMI batch import includes fields that require json strings/objects to be included in a single cell. 

Here is an example of a subjects_local field:

:code:`["American Civil War (United States : 1861-1865)", "Migration, Internal--Southern States", "Cherokee Indians--Tribal citizenship", "Oklahoma--Fort Gibson (Indian Territory)", "Oklahoma--Sequoyah District (Indian Territory)"]`.

Each heading is surrounded by quotation marks and separated from the next heading with a comma and a space. The entire string is in brackets.

This bracketing becomes even more complicated when using linked data. For example, all of this should go under the creator_lod field when doing a batch import in a single cell:

:code:`[{"name_uri":"http://id.loc.gov/authorities/names/n2001078880","role_uri":"http://id.loc.gov/vocabulary/relators/cre","agent_type":"personal","name_label":"Hogg, James Stephen, 1851-1906.","role_label":"Creator"},{"name_uri":"https://id.loc.gov/authorities/names/n82158463","role_uri":"http://id.loc.gov/vocabulary/relators/rcp","agent_type":"personal","name_label":"Ross, Lawrence Sullivan, 1838-1898","role_label":"Addressee"}]`

This is two headings, each with 5 properties, and should all go in the same cell. Typing this out may be time-consuming and lead to mistakes, so here is a template flat csv and a script that to convert it into an AMI-compatible spreadsheet.

-----------------------------
What does this csv format do?
-----------------------------

Instead of typing long strings into a single small cell, this "flat" template allows you to spread values across multiple columns for better readability and usability. 

This is similar to an Avalon spreadsheet upload, where you can add as many columns as needed, except a few things differ.

* Creators and subjects will be separated between local and linked data. In Avalon, all creators/subjects are treated the same.

* Creators and contributors are both classified as "creators". You can differentiate between them using a role property. In Avalon, creators and contributors are differentiated by being placed in columns labeled "Creator" or "Contributor".

    * The role property is only usable if you is using linked data for the creator. Local creators do not have a role property.

* Every linked data value requires at least two columns, not one. To add an extra subject on Avalon, a single column needs to be created. To add an extra subject here, two columns must be created, one for the label and the other for the uri.

* Most linked data fields will require two columns per entry except creator/contributor fields, which require five: personal/corporate, label, uri, role, and role uri.

* Local creators, local subjects, and local subjects - personal names can be added with a single column that contains the label. This is similar to Avalon.

* Avalon column names are repeatable. Here, the columns require a number so the script knows which label to match with which uri.

    * For example, LCSH subjects follow this format: :code:`subject_loc_{i}_label` and :code:`subject_loc_{i}_uri` where :code:`i` represents a number. :code:`i` **must** match for a label and uri pair.

* An Avalon spreadsheet is the final product that is uploaded. This template creates an **intermediate** spreadsheet that must be converted into an AMI-compatible spreadsheet.

Not all Archipelago values require multiple "parts" to be strung together. This spreadsheet template is only used for adding the following repeatable fields:

* LCNAF creators

* LCSH subject headings

* LCNAF subjects (personal)

* LCNAF subjects (corporate)

* LCNAF geographic subjects

* LCGFT terms

* Local creators

* Local subjects

* Local subjects - personal names

* Wikidata

Other fields, like description or date_created should be added directly to the final AMI-compatible spreadsheet.

---------
Input csv
---------

Enter your metadata into this csv.

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1wFw1fSr6OpSeNCX7tZDRjhPIfn_pdr7WgUT217FZQbs/edit?usp=sharing" height="400" width="800" frameborder="0" allowfullscreen></iframe>


Be sure to look at the first sheet (Flat).

Add more columns if there need to be more metadata values per field. Remember that:

* LCNAF creator fields are added in sets of 5.

* LCSH subject headings, LCNAF subjects (personal), LCNAF subjects (corporate), LCNAF geographic subjects, LCGFT terms, and Wikidata fields are added in sets of 2.

* Local creators, local subjects, and local subjects - personal names are added individually.

----------------------------------
What do these column headers mean?
----------------------------------

* If Column label starts with

    * this is the type of metadata field it is

* :code:`creator_lod_{i}_name_`

    * LCNAF creator  

* :code:`subject_loc_{i}_`

    * LCSH subject heading 

* :code:`subject_lcnaf_personal_{i}_`

    * LCNAF subject (personal) 

* :code:`subject_lcnaf_corporate_{i}_`

    * LCNAF subject (corporate) 

* :code:`subject_lcnaf_geographic_{i}_`

    * LCNAF geographic subject

* :code:`subject_lcgft_terms_{i}_`

    * LCGFT (genre/form) term 

* :code:`creator_{i}`

    * Local creator

* :code:`subjects_local_{i}`

    * Local subject

* :code:`subjects_local_personal_names_{i}`

    * Local subject - personal name

* :code:`subjects_wikidata_{i}_`

    * Wikidata



----------
Conversion
----------

Once you have the input csv, you can run this script to convert it to a csv compatible with Archipelago AMI batch import.

.. code:: python

    import csv
    import json
    import re

    INPUT_CSV = "input_flat.csv"
    OUTPUT_CSV = "output.csv"

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

            "creator",
            "creator_lod",

            "subject_loc",
            "subject_lcnaf_personal_names",
            "subject_lcnaf_corporate_names",
            "subject_lcnaf_geographic_names",
            "subject_lcgft_terms",
            "subject_wikidata",

            "subjects_local",
            "subjects_local_personal_names"
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
            
                "creator": json.dumps(creators, ensure_ascii=False),
                "creator_lod": json.dumps(creator_lod, ensure_ascii=False),

                "subject_loc": json.dumps(subject_loc, ensure_ascii=False),
                "subject_lcnaf_personal_names": json.dumps(lcnaf_personal, ensure_ascii=False),
                "subject_lcnaf_corporate_names": json.dumps(lcnaf_corporate, ensure_ascii=False),
                "subject_lcnaf_geographic_names": json.dumps(lcnaf_geographic, ensure_ascii=False),
                "subject_lcgft_terms": json.dumps(subject_lcgft, ensure_ascii=False),
                "subject_wikidata": json.dumps(wikidata, ensure_ascii=False),

                "subjects_local": json.dumps(subjects_local, ensure_ascii=False),
                "subjects_local_personal_names": json.dumps(subjects_local_personal, ensure_ascii=False)
            })


--------------------------
Putting your csvs together
--------------------------

Now that you have your output.csv, you can copy and paste these columns into your AMI-compatible spreadsheet.
