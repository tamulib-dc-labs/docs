========================================
Fixing Broken Cache from IR IIIF Service
========================================

Historically, we have used the IR IIIF Service to generate IIIF Presentation Manifests.
However, the image URLs it references will eventually expire and begin returning ``404`` errors.

Example: Expired Cantaloupe Image URLs
--------------------------------------

The following Canvas record from *Houston Oil Minutes* illustrates the problem.
Notice the Cantaloupe-generated URLs highlighted below:

.. code-block:: json
    :emphasize-lines: 10, 14, 21

    {
      "@id": "https://api.library.tamu.edu/iiif-service/fedora/canvas/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/houston_oil_company_minutes_objects/2/pages/page_0",
      "@type": "sc:Canvas",
      "label": "Index - 1",
      "width": 3342,
      "height": 5544,
      "images": [
        {
          "@id": "https://api.library.tamu.edu/iiif/2/88c02c4f-cb78-3d8d-a4a5-2463f29a6565",
          "@type": "oa:Annotation",
          "motivation": "sc:painting",
          "resource": {
            "@id": "https://api.library.tamu.edu/iiif/2/88c02c4f-cb78-3d8d-a4a5-2463f29a6565/full/full/0/default.jpg",
            "@type": "dctypes:Image",
            "format": "image/jpeg",
            "width": 3342,
            "height": 5544,
            "service": {
              "@context": "http://iiif.io/api/image/2/context.json",
              "@id": "https://api.library.tamu.edu/iiif/2/88c02c4f-cb78-3d8d-a4a5-2463f29a6565",
              "profile": "https://iiif.io/api/image/1.1/compliance/#level2"
            }
          },
          "on": "https://api.library.tamu.edu/iiif-service/fedora/canvas/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/houston_oil_company_minutes_objects/2/pages/page_0"
        }
      ]
    }

Why This Happens
----------------

These IIIF image URLs are created by our delegates file and are unexpectedly cached in Redis by the IR IIIF Service.
Once this Redis cache expires, the IR IIIF Service returns ``404`` for these image endpoints.

Unfortunately, there is no direct way to re-request a specific expired image URL.
However, you *can* trigger regeneration of the cached values by requesting the **canvas ID** itself.

For example:

.. code-block:: text

    https://api.library.tamu.edu/iiif-service/fedora/canvas/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/houston_oil_company_minutes_objects/2/pages/page_0

Requesting this Canvas forces the IR IIIF Service to rebuild the associated manifest components, including the expired Cantaloupe URLs.

Fixing in Batches
-----------------

You can fix this at scale like:

.. code-block:: python

    import json
    import requests
    import os

    for path, directories, files in os.walk("manifests/houston-oil-minutes"):
        for filename in files:
            if filename.endswith(".json"):
                with open(os.path.join(path, filename), "r") as f:
                    data = json.load(f)
                for sequence in data['sequences']:
                    for canvas in sequence['canvases']:
                        r = requests.get(canvas['@id'])
