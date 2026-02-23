==============================
Convert MARC Binary to TAMU DC
==============================

Currently we have no official tooling for converting MARC binary to DublinCore.  Until we do, you can use a script like
this.  If any part of this needs to be changed, it can be.


.. code-block:: python

    import csv
    import pymarc

    INPUT_FILE = "Feb2-Mark-InstanceUUIDs-932.mrc"
    OUTPUT_FILE = "woellhof.csv"

    DC_HEADERS = [
        "dc.title",
        "dc.identifier",
        "dc.creator",
        "dcterms.extent",
        "dcterms.spatial",
        "dc.coverage",
        "dc.publisher",
        "dcterms.issued",
        "dcterms.type",
        "dc.subject",
        "dc.type",
        "dc.language",
        "dc.rights",
        "dcterms.abstract",
        "dc.description",
        "dcterms.isPartOf",
        "dc.format",
    ]

    LANGUAGE_CODES = {
        "lat": "Latin",
        "eng": "English",
        "ger": "German",
        "fre": "French",
        "dut": "Dutch",
        "ita": "Italian",
        "spa": "Spanish",
        "por": "Portuguese",
        "ara": "Arabic",
        "gre": "Greek",
        "grc": "Greek, Ancient",
        "tur": "Turkish",
    }


    def get_field(record, tag):
        """Safely get a field, returning None if not present."""
        fields = record.get_fields(tag)
        return fields[0] if fields else None


    def get_subfields(field, codes):
        """Get concatenated subfield values for given codes."""
        parts = []
        for code in codes:
            for val in field.get_subfields(code):
                parts.append(val.strip().rstrip(".").strip())
        return " ".join(parts) if parts else ""


    def get_language(record):
        """Extract language from 041 or 008."""
        langs = []
        for f041 in record.get_fields("041"):
            for code in f041.get_subfields("a"):
                code = code.strip()
                langs.append(LANGUAGE_CODES.get(code, code))
        if not langs:
            try:
                f008 = get_field(record, "008")
                code = f008.data[35:38].strip() if f008 else ""
                if code and code != "|||":
                    langs.append(LANGUAGE_CODES.get(code, code))
            except (AttributeError, IndexError):
                pass
        return "||".join(langs)


    def extract_record(record):
        """Extract Dublin Core fields from a single MARC record."""
        row = {}

        # Use 245 $a $b for dc.title
        f245 = get_field(record, "245")
        if f245:
            title_parts = []
            for code in ("a", "b"):
                for v in f245.get_subfields(code):
                    title_parts.append(v.strip().rstrip("/").strip())
            row["dc.title"] = " ".join(title_parts).rstrip(".").strip()
        else:
            row["dc.title"] = ""

        # Get OCLC number from 035 $a for dc.identifier
        identifiers = []
        for f035 in record.get_fields("035"):
            for v in f035.get_subfields("a"):
                identifiers.append(v.strip())
        # Also use the 001
        f001 = get_field(record, "001")
        if f001:
            identifiers.insert(0, f001.data.strip())
        row["dc.identifier"] = "||".join(identifiers)

        # Get dc.creator from 100 $a $d
        f100 = get_field(record, "100")
        if f100:
            creator = get_subfields(f100, ["a", "d"])
            row["dc.creator"] = creator.rstrip(",").strip()
        else:
            row["dc.creator"] = ""

        # Get dcterms.extent values from 300 $a $b $c
        f300 = get_field(record, "300")
        if f300:
            row["dcterms.extent"] = get_subfields(f300, ["a", "b", "c"])
        else:
            row["dcterms.extent"] = ""

        # dcterms.spatial use 651 $a (subject geographic) for values for dcterms.spatial
        spatials = []
        for f651 in record.get_fields("651"):
            place = f651.get_subfields("a")
            if place:
                spatials.append(place[0].strip().rstrip("."))
        row["dcterms.spatial"] = "||".join(spatials)

        # use 255 $c (coordinates/scale) and 034 for dc.coverage values and crosswalking to GeoJSON
        coverage_parts = []
        for f255 in record.get_fields("255"):
            for v in f255.get_subfields("a", "c"):
                coverage_parts.append(v.strip())
        row["dc.coverage"] = " ".join(coverage_parts)

        # Use 264 $b for dc.publisher
        f264 = get_field(record, "264")
        if f264:
            pub = f264.get_subfields("b")
            row["dc.publisher"] = pub[0].strip().rstrip(",").strip("[]") if pub else ""
        else:
            row["dc.publisher"] = ""

        # Use 264 $c for dcterms.issued
        if f264:
            date = f264.get_subfields("c")
            row["dcterms.issued"] = date[0].strip().rstrip(".").strip("[]") if date else ""
        else:
            row["dcterms.issued"] = ""

        # Use 336 $a (content type) for dcterms.type
        types336 = []
        for f336 in record.get_fields("336"):
            for v in f336.get_subfields("a"):
                types336.append(v.strip())
        row["dcterms.type"] = "||".join(types336)

        # Use 651 $a $v $x and 650 $a $x (full subject strings) for dc.subject values
        subjects = []
        for tag in ("600", "610", "650", "651"):
            for field in record.get_fields(tag):
                parts = []
                for sub in field.subfields:
                    # pymarc subfields: list of (code, value) or alternating code/value
                    if hasattr(sub, "code"):
                        if sub.code not in ("0", "1", "2", "4", "5", "6", "8"):
                            parts.append(sub.value.strip().rstrip("."))
                    else:
                        pass
                if parts:
                    subjects.append("--".join(parts))
        # If that fails, fallback
        if not subjects:
            for tag in ("600", "610", "650", "651"):
                for field in record.get_fields(tag):
                    subfield_pairs = list(zip(field.subfields[::2], field.subfields[1::2])) if isinstance(field.subfields[0], str) else []
                    parts = []
                    for code, val in subfield_pairs:
                        if code not in ("0", "1", "2", "4", "5", "6", "8"):
                            parts.append(val.strip().rstrip("."))
                    if parts:
                        subjects.append("--".join(parts))
        row["dc.subject"] = "||".join(subjects)

        # Use 655 $a for genre/form values
        genres = []
        for f655 in record.get_fields("655"):
            for v in f655.get_subfields("a"):
                genres.append(v.strip().rstrip("."))
        row["dc.type"] = "||".join(genres)

        # Get dc.language
        row["dc.language"] = get_language(record)

        # Include this although we will always get dc.rights from the curator
        f540 = get_field(record, "540")
        if f540:
            row["dc.rights"] = get_subfields(f540, ["a"])
        else:
            row["dc.rights"] = ""

        # Use 520 $a for dcterms.abstrat
        abstracts = []
        for f520 in record.get_fields("520"):
            for v in f520.get_subfields("a"):
                abstracts.append(v.strip())
        row["dcterms.abstract"] = "||".join(abstracts)

        # Use 500 $a (general notes), 546 $a (language note) for dc.description fields
        notes = []
        for f500 in record.get_fields("500"):
            for v in f500.get_subfields("a"):
                notes.append(v.strip())
        for f546 in record.get_fields("546"):
            for v in f546.get_subfields("a"):
                notes.append(v.strip())
        row["dc.description"] = "||".join(notes)

        # Use 700 with $t (related work title) or 773 for dcterms.isPartOf (Drop if it makes now sense)
        parts_of = []
        for f700 in record.get_fields("700"):
            titles = f700.get_subfields("t")
            if titles:
                creator_name = f700.get_subfields("a")
                for t in titles:
                    entry = t.strip().rstrip(".")
                    if creator_name:
                        entry = creator_name[0].strip().rstrip(",") + ". " + entry
                    parts_of.append(entry)
        for f773 in record.get_fields("773"):
            for v in f773.get_subfields("t", "a"):
                parts_of.append(v.strip().rstrip("."))
        row["dcterms.isPartOf"] = "||".join(parts_of)

        # Use 338 $a (carrier type) for dc.format
        formats = []
        for f338 in record.get_fields("338"):
            for v in f338.get_subfields("a"):
                formats.append(v.strip())
        row["dc.format"] = "||".join(formats)

        return row


    def main():
        with open(INPUT_FILE, "rb") as fh:
            reader = pymarc.MARCReader(fh)
            records = []
            for record in reader:
                if record is None:
                    continue
                records.append(extract_record(record))

        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(fh, fieldnames=DC_HEADERS)
            writer.writeheader()
            writer.writerows(records)

        print(f"Wrote {len(records)} records to {OUTPUT_FILE}")


    if __name__ == "__main__":
        main()
