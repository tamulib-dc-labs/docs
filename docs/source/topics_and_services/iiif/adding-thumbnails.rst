================================================
Adding a Thumbnail to a IIIF Manifest
================================================

When building exhibits with Spotlight, it may be useful to add a thumbnail to a IIIF manifest. The thumbnail is its own section in the manifest, on the top level. (For example, it should be aligned with :code:`metadata` and :code:`sequences`.)

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

Note that :code:`@id` under :code:`service` should be nearly identical to :code:`@id` one level under :code:`thumbnail`, except without the sizing, rotation, scale, and cropping features and the :code:`.jpg` extension.

You can acquire this :code:`@id` by going to the first canvas under :code:`sequences`.

:code:`,200` is a good size for the Spotlight search results.