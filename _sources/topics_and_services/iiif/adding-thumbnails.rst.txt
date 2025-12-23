=====================================
Adding a Thumbnail to a IIIF Manifest
=====================================

When building exhibits with Spotlight, it may be useful to add a thumbnail to a IIIF manifest if one is missing.

The thumbnail is its own section in the manifest, on the top level. (For example, it should be aligned with
:code:`metadata` and :code:`sequences`.)

The thumbnail will have this format:

.. code-block:: json

    "thumbnail": {
        "@id": "https://api-pre.library.tamu.edu/iiif/2/5e190c52-c05f-38a1-b358-dbce6429b4a0/full/,200/0/default.jpg",
        "@type": "dctypes:Image",
        "label": "thumbnail image",
        "service": {
        "@id": "https://api-pre.library.tamu.edu/iiif/2/5e190c52-c05f-38a1-b358-dbce6429b4a0",
        "@context": "http://iiif.io/api/image/2/context.json",
        "profile": "http://iiif.io/api/image/2/level2.json",
        "label": "IIIF Image Service"
        }
    }

Note that :code:`@id` under :code:`service` should be nearly identical to :code:`@id` one level under
:code:`thumbnail`, except without the sizing, rotation, scale, and cropping features and the :code:`.jpg` extension.

You can acquire this :code:`@id` by going to the first canvas under :code:`sequences`.

:code:`,200` is a good size for the Spotlight search results.

--------------------
Adding Thumbnails to a directory of manifests
--------------------

Here is a script that adds a thumbnail section to each json in a directory of IIIF manifests.

.. code-block:: python

    import json
    from pathlib import Path

    MANIFEST_DIR = Path("manifest")
    THUMBNAIL_SUFFIX = "/full/,200/0/default.jpg"


    def is_manifest(data):
        return (
            data.get("@type") == "sc:Manifest"
            or "sequences" in data
        )


    def find_first_canvas(manifest):
        try:
            return manifest["sequences"][0]["canvases"][0]
        except (KeyError, IndexError, TypeError):
            return None


    def extract_image_service(canvas):
        """
        Look for an Image API service on the first canvas,
        regardless of where it lives.
        """
        candidates = []

        # Typical v2 location
        for img in canvas.get("images", []):
            res = img.get("resource", {})
            service = res.get("service")

            if isinstance(service, dict) and "@id" in service:
                candidates.append(service["@id"])

            elif isinstance(service, list):
                for s in service:
                    if "@id" in s:
                        candidates.append(s["@id"])

        return candidates[0] if candidates else None


    def add_thumbnail(manifest):
        canvas = find_first_canvas(manifest)
        if not canvas:
            print("  ⚠️  No canvas found")
            return False

        service_id = extract_image_service(canvas)
        if not service_id:
            print("  ⚠️  No image service found on canvas")
            return False

        manifest["thumbnail"] = {
            "@id": f"{service_id}{THUMBNAIL_SUFFIX}",
            "@type": "dctypes:Image",
            "label": "thumbnail image",
            "service": {
                "@id": service_id,
                "@context": "http://iiif.io/api/image/2/context.json",
                "profile": "http://iiif.io/api/image/2/level2.json",
                "label": "IIIF Image Service"
            }
        }

        return True


    def main():
        json_files = sorted(MANIFEST_DIR.glob("*.json"))
        print(f"Found {len(json_files)} JSON files")

        for path in json_files:
            print(f"\nProcessing {path.name}")

            with path.open(encoding="utf-8") as f:
                data = json.load(f)

            if not is_manifest(data):
                print("  ❌ Not recognized as a manifest — skipped")
                continue

            if add_thumbnail(data):
                with path.open("w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                print("  ✅ Thumbnail added")
            else:
                print("  ❌ Thumbnail not added")

        print("\nDone.")


    if __name__ == "__main__":
        main()