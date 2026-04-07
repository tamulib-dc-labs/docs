=================================
Linked data and multivalue fields
=================================

This is a guide that makes linked data easier to work with. This page includes a script used to take a "flattened" csv template and reformat the values so that they are compatible with the Archipelago Multi-Importer (AMI).

-------------------
Why is this needed?
-------------------

The spreadsheet template for Archipelago AMI batch import includes fields that require json strings/objects to be included in a single cell. 

Here is an example of a :code:`subject` field:

:code:`["American Civil War (United States : 1861-1865)", "Migration, Internal--Southern States", "Cherokee Indians--Tribal citizenship", "Oklahoma--Fort Gibson (Indian Territory)", "Oklahoma--Sequoyah District (Indian Territory)"]`

Each heading is surrounded by quotation marks and separated from the next heading with a comma and a space. The entire string is in brackets.

This bracketing becomes even more complicated when using linked data. For example, all of this should go under the :code:`agent_linked_data` field when doing a batch import in a single cell:

:code:`[{"uri": "http://id.loc.gov/authorities/names/n2001078880", "role_uri": "http://id.loc.gov/vocabulary/relators/cre", "value": "Hogg, James Stephen, 1851-1906.", "role": "Creator"},{"uri": "https://id.loc.gov/authorities/names/n82158463", "role_uri": "http://id.loc.gov/vocabulary/relators/rcp", "value": "Ross, Lawrence Sullivan, 1838-1898", "role": "Addressee"}]`

This is two headings, each with 4 properties, and should all go in the same cell. Typing this out may be time-consuming and lead to mistakes, so here is a template flat csv and a script that to convert it into an AMI-compatible spreadsheet.

-----------------------------
What does this csv format do?
-----------------------------

Instead of typing long strings into a single small cell, this "flat" template allows you to spread values across multiple columns for better readability and usability.

Here are a few things to keep in mind:

* To add another value for a simple field, add another column. However, column names are not repeatable, so you will need to label new columns like this: :code:`field_1`, :code:`field_2`, :code:`field_3`, etc.

* If a field is linked data or otherwise complex (such as :code:`identifier` or :code:`date_created_edtf`), you will need to add multiple columns per value. You would label new columns like this: :code:`field_1_value`, :code:`field_1_uri`, :code:`field_2_value`, :code:`field_2_uri`, :code:`field_3_value`, :code:`field_3_uri`, etc. Similarly, the :code:`agent_linked_data` field will require you to add four new columns per value.

* Because they are structured differently, linked data metadata terms will always be in different fields from from their non-linked data counterparts.

* Any creator/contributor field that uses linked data must go in the agent_linked_data field and be assigned a role there.

* This template creates an **intermediate** spreadsheet.

* Do not use this script for fields that only take a single value. Add them directly to the final AMI-compatible spreadsheet.

---------
Input csv
---------

Enter your metadata into this csv.

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1wFw1fSr6OpSeNCX7tZDRjhPIfn_pdr7WgUT217FZQbs/edit?usp=sharing" height="400" width="800" frameborder="0" allowfullscreen></iframe>



----------
Conversion
----------

Once you have the input csv, you can run this script to convert it to a csv compatible with Archipelago AMI batch import.

.. code:: python

    import csv
    import json
    import re

    INPUT_CSV = "flat.csv"
    OUTPUT_CSV = "compressed.csv"

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

    def build_linked_data_array(row, fieldnames, base):
        indexes = find_indexes(fieldnames, f"{base}_", "_value")
        results = []

        for i in indexes:
            value = row.get(f"{base}_{i}_value")
            uri   = row.get(f"{base}_{i}_uri")

            if non_empty(label):
                results.append({
                    "value": value,
                    "uri": uri
                })

        return results

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
            "contributor",
            "agent",
            "agent_linked_data",
            "sponsorship",
            "local_department",

            "subject",
            "geographic_subject",
            "temporal_subject",
            "subject_linked_data",
            "geographic_subject_linked_data",
            "temporal_subject_linked_data",

            "genre_form",
            "genre_form_linked_data",
            "content_type",
            "medium",
            "mimetype",
            "extent",
            "description",
            "note",
            "language",

            "digital_exhibit",
            "collecting_area",
            "identifier",
            "title_alternative",
            "related_record",
            "provenance",
            "original_publication",
            
            "classification",
            "coordinates",
            "rights_holder",
            "access_rights",
            "audience",
            "attribution",

            "date_created_edtf",
            "date_issued_edtf"

        ]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:

            # ---- Creator ----
            creator_indexes = find_indexes(reader.fieldnames, "creator_", "")
            creators = [
                row.get(f"creator_{i}")
                for i in creator_indexes
                if non_empty(row.get(f"creator_{i}"))
            ]

            # ---- Contributor ----
            contributor_indexes = find_indexes(reader.fieldnames, "contributor_", "")
            contributors = [
                row.get(f"contributor_{i}")
                for i in contributor_indexes
                if non_empty(row.get(f"contributor_{i}"))
            ]
            
            # ---- Agent ----
            agent_indexes = find_indexes(reader.fieldnames, "agent_", "_value")
            agents = []

            for i in agent_indexes:
                prefix = f"agent_{i}_"
                fields = {
                    "value": row.get(prefix + "value"),
                    "role": row.get(prefix + "role"),
                    "role_uri": row.get(prefix + "role_uri")
                }

                if any(non_empty(v) for v in fields.values()):
                    agents.append(fields)

            # ---- Agent Linked Data ----
            agent_linked_data_indexes = find_indexes(reader.fieldnames, "agent_linked_data_", "_value")
            agents_linked_data = []

            for i in agent_linked_data_indexes:
                prefix = f"agent_linked_data_{i}_"
                fields = {
                    "value": row.get(prefix + "value"),
                    "uri": row.get(prefix + "uri"),
                    "role": row.get(prefix + "role"),
                    "role_uri": row.get(prefix + "role_uri")
                }

                if any(non_empty(v) for v in fields.values()):
                    agents_linked_data.append(fields)


            # ---- Subjects ----

            subject_indexes = find_indexes(reader.fieldnames, "subject_", "")
            subjects = [
                row.get(f"subject_{i}")
                for i in subject_indexes
                if non_empty(row.get(f"subject_{i}"))
            ]
            geographic_subject_indexes = find_indexes(reader.fieldnames, "geographic_subject_", "")
            geographic_subjects = [
                row.get(f"geographic_subject_{i}")
                for i in geographic_subject_indexes
                if non_empty(row.get(f"geographic_subject_{i}"))
            ]
            temporal_subject_indexes = find_indexes(reader.fieldnames, "temporal_subject_", "")
            temporal_subjects = [
                row.get(f"temporal_subject_{i}")
                for i in temporal_subject_indexes
                if non_empty(row.get(f"temporal_subject_{i}"))
            ]
            
            # ---- Linked Data Subjects ----
            subjects_linked_data = build_linked_data_array(row, reader.fieldnames, "subject_linked_data")
            geographic_subjects_linked_data = build_linked_data_array(row, reader.fieldnames, "geographic_subject_linked_data")
            temporal_subjects_linked_data = build_linked_data_array(row, reader.fieldnames, "temporal_subject_linked_data")

            # ---- Genre/Form ----
            genre_form_indexes = find_indexes(reader.fieldnames, "genre_form_", "")
            genre_forms = [
                row.get(f"genre_form_{i}")
                for i in genre_form_indexes
                if non_empty(row.get(f"genre_form_{i}"))
            ]
            genre_forms_linked_data = build_linked_data_array(row, reader.fieldnames, "genre_form_linked_data")

            # ---- Content Type ----
            content_type_indexes = find_indexes(reader.fieldnames, "content_type_", "")
            content_types = [
                row.get(f"content_type_{i}")
                for i in content_types
                if non_empty(row.get(f"content_type_{i}"))
            ]

            # ---- Medium ----
            medium_indexes = find_indexes(reader.fieldnames, "medium_", "")
            mediums = [
                row.get(f"medium_{i}")
                for i in mediums
                if non_empty(row.get(f"medium_{i}"))
            ]

            # ---- Mimetype ----
            mimetype_indexes = find_indexes(reader.fieldnames, "mimetype_", "")
            mimetypes = [
                row.get(f"mimetype_{i}")
                for i in mimetypes
                if non_empty(row.get(f"mimetype_{i}"))
            ]

            # ---- Extent ----
            extent_indexes = find_indexes(reader.fieldnames, "extent_", "")
            extents = [
                row.get(f"extent_{i}")
                for i in extents
                if non_empty(row.get(f"extent_{i}"))
            ]

            # ---- Description ----
            description_indexes = find_indexes(reader.fieldnames, "description_", "")
            descriptions = [
                row.get(f"description_{i}")
                for i in description_indexes
                if non_empty(row.get(f"description_{i}"))
            ]

            # ---- Note ----
            note_indexes = find_indexes(reader.fieldnames, "note_", "")
            notes = [
                row.get(f"note_{i}")
                for i in note_indexes
                if non_empty(row.get(f"note_{i}"))
            ]

            # ---- Language ----
            language_indexes = find_indexes(reader.fieldnames, "language_", "")
            languages = [
                row.get(f"language_{i}")
                for i in language_indexes
                if non_empty(row.get(f"language_{i}"))
            ]

            # ---- Digital Exhibit ----
            digital_exhibits = build_linked_data_array(row, reader.fieldnames, "digital_exhibit")

            # ---- Collecting Area ----
            collecting_area_indexes = find_indexes(reader.fieldnames, "collecting_area_", "")
            collecting_areas = [
                row.get(f"collecting_area_{i}")
                for i in collecting_areas
                if non_empty(row.get(f"collecting_area_{i}"))
            ]

            # ---- Identifier ----
            identifier_indexes = find_indexes(reader.fieldnames, "identifier_", "_value")
            identifiers = []

            for i in identifier_indexes:
                prefix = f"identifier_{i}_"
                fields = {
                    "value": row.get(prefix + "value"),
                    "authority": row.get(prefix + "authority"),
                }

                if any(non_empty(v) for v in fields.values()):
                    identifiers.append(fields)

            # ---- Title Alternative ----
            title_alternative_indexes = find_indexes(reader.fieldnames, "title_alternative_", "")
            titles_alternative = [
                row.get(f"title_alternative_{i}")
                for i in titles_alternative
                if non_empty(row.get(f"title_alternative_{i}"))
            ]

            # ---- Related Record ----
            related_record_indexes = find_indexes(reader.fieldnames, "related_record_", "")
            related_records = [
                row.get(f"related_record_{i}")
                for i in related_records
                if non_empty(row.get(f"related_record_{i}"))
            ]

            # ---- Provenance ----
            provenance_indexes = find_indexes(reader.fieldnames, "provenance_", "")
            provenances = [
                row.get(f"provenance_{i}")
                for i in provenances
                if non_empty(row.get(f"provenance_{i}"))
            ]

            # ---- Original Publication ----
            original_publication_indexes = find_indexes(reader.fieldnames, "original_publication_", "")
            original_publications = [
                row.get(f"original_publication_{i}")
                for i in original_publications
                if non_empty(row.get(f"original_publication_{i}"))
            ]

            # ---- Classification ----
            classification_indexes = find_indexes(reader.fieldnames, "classification_", "_value")
            classifications = []

            for i in classification_indexes:
                prefix = f"classification_{i}_"
                fields = {
                    "value": row.get(prefix + "value"),
                    "authority": row.get(prefix + "authority"),
                }

                if any(non_empty(v) for v in fields.values()):
                    classifications.append(fields)
            
            # ---- Coordinates ----
            coordinates_indexes = find_indexes(reader.fieldnames, "coordinates_", "")
            coordinates = [
                row.get(f"coordinates_{i}")
                for i in coordinates
                if non_empty(row.get(f"coordinates_{i}"))
            ]

            # ---- Rights Holder ----
            rights_holder_indexes = find_indexes(reader.fieldnames, "rights_holder_", "")
            rights_holders = [
                row.get(f"rights_holder_{i}")
                for i in rights_holders
                if non_empty(row.get(f"rights_holder_{i}"))
            ]

            # ---- Access Rights ----
            access_rights_indexes = find_indexes(reader.fieldnames, "access_rights_", "")
            access_rights = [
                row.get(f"access_rights_{i}")
                for i in access_rights
                if non_empty(row.get(f"access_rights_{i}"))
            ]

            # ---- Audience ----
            audience_indexes = find_indexes(reader.fieldnames, "audience_", "")
            audiences = [
                row.get(f"audience_{i}")
                for i in audiences
                if non_empty(row.get(f"audience_{i}"))
            ]

            # ---- Attribution ----
            attribution_indexes = find_indexes(reader.fieldnames, "attribution_", "")
            attributions = [
                row.get(f"attribution_{i}")
                for i in attributions
                if non_empty(row.get(f"attribution_{i}"))
            ]

            # ---- Date created (EDTF) ----
            raw_date_created = {
                "date_issued_date_to": row.get("date_to"),
                "date_issued_date_free": row.get("date_free"),
                "date_issued_date_from": row.get("date_from"),
                "date_issued_date_type": row.get("date_type")
            }

            # Remove empty values entirely
            date_created = {
                k: v for k, v in raw_date_created.items()
                if non_empty(v)
            }

            if not date_created:
                date_created = None

            # Only keep if at least one value is present
            if not any(non_empty(v) for v in date_created.values()):
                date_created = None

            # ---- Date issued (EDTF) ----
            raw_date_issued = {
                "date_issued_date_to": row.get("date_to"),
                "date_issued_date_free": row.get("date_free"),
                "date_issued_date_from": row.get("date_from"),
                "date_issued_date_type": row.get("date_type")
            }
            
            # Remove empty values entirely
            date_issued = {
                k: v for k, v in raw_date_issued.items()
                if non_empty(v)
            }

            if not date_issued:
                date_issued = None

            # Only keep if at least one value is present
            if not any(non_empty(v) for v in date_issued.values()):
                date_issued = None

            # ---- Write row ----
            writer.writerow({
            
                "creator": json.dumps(creators, ensure_ascii=False),
                "contributor": json.dumps(contributors, ensure_ascii=False),
                "agent": json.dumps(agents, ensure_ascii=False),
                "agent_linked_data": json.dumps(agents_linked_data, ensure_ascii=False),

                "subject": json.dumps(subjects, ensure_ascii=False),
                "geographic_subject": json.dumps(geographic_subjects, ensure_ascii=False),
                "temporal_subject": json.dumps(temporal_subjects, ensure_ascii=False),
                "subject_linked_data": json.dumps(subjects_linked_data, ensure_ascii=False),
                "geographic_subject_linked_data": json.dumps(geographic_subjects_linked_data, ensure_ascii=False),
                "temporal_subject_linked_data": json.dumps(temporal_subjects_linked_data, ensure_ascii=False),

                "genre_form": json.dumps(genre_forms, ensure_ascii=False),
                "genre_form_linked_data": json.dumps(genre_forms_linked_data, ensure_ascii=False), 
                "medium": json.dumps(mediums, ensure_ascii=False),
                "mimetype": json.dumps(mimetypes, ensure_ascii=False),
                "extent": json.dumps(extents, ensure_ascii=False),
                "description": json.dumps(descriptions, ensure_ascii=False),
                "note": json.dumps(notes, ensure_ascii=False),
                "language": json.dumps(languages, ensure_ascii=False),

                "digital_exhibit": json.dumps(digital_exhibits, ensure_ascii=False),
                "collecting_area": json.dumps(collecting_areas, ensure_ascii=False),
                "identifier": json.dumps(identifiers, ensure_ascii=False),
                "title_alternative": json.dumps(titles_alternative, ensure_ascii=False),
                "related_record": json.dumps(related_records, ensure_ascii=False),
                "provenance": json.dumps(provenances, ensure_ascii=False),
                "original_publication": json.dumps(original_publications, ensure_ascii=False),
                
                "classification": json.dumps(classifications, ensure_ascii=False),
                "coordinates": json.dumps(coordinates, ensure_ascii=False),
                "rights_holder": json.dumps(rights_holders, ensure_ascii=False),
                "access_rights": json.dumps(access_rights, ensure_ascii=False),
                "audience": json.dumps(audiences, ensure_ascii=False),
                "attribution": json.dumps(attributions, ensure_ascii=False),

                "date_created_edtf": (
                    json.dumps(date_created, ensure_ascii=False)
                    if date_created else ""
                ),
                "date_issued_edtf": (
                    json.dumps(date_issued, ensure_ascii=False)
                    if date_issued else ""
                )
            })

