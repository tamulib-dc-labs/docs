==========================
SAGE: Solr 6 versus Solr 9
==========================

Overview
--------

SAGE historically used Solr 6. Several years ago, attempts were made to upgrade to Solr 9.
In May 2026, this upgrade was finally deployed to production.

Missing Documents
-----------------

.. warning::

   Eleven Solr documents are absent from the Brazos Map collection. This is caused by a bug
   in Fedora Karaf's indexing behavior that prevented those 11 records from being indexed
   into the collection.

To move forward, these missing documents were skipped with the intent to recreate them
manually following the Solr 9 schema (see :ref:`adding-documents`).

Schema Comparison
-----------------

The Solr 9 schema differs from Solr 6 in several important ways:

- Field names changed: ``title_txt_en_split`` → ``title_text_si_en_split``;
  ``spatial_txt_en_split_multi`` → ``spatial_multi_string``
- Facet, text, and string variants of fields are more consistently named (e.g.,
  ``creator_facet``, ``creator_text``)
- ``_text_ws`` and ``_text_`` are explicit full-text copy fields
- ``date_issued`` is now an integer array rather than a string
- ``local_coordinates`` is now an array rather than a scalar string
- Internal Solr fields ``_version_`` and ``score`` are not present in stored documents

Solr 9 Document Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
      "application_type": "fedora",
      "application_type_facet": ["fedora"],
      "collection": ["https://api.library.tamu.edu/fcrepo/rest/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects"],
      "collection_facet": ["https://api.library.tamu.edu/fcrepo/rest/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects"],
      "content_type": ["StillImage"],
      "content_type_facet": ["StillImage"],
      "creator": ["Orr, J. A."],
      "creator_facet": ["Orr, J. A."],
      "_text_ws": ["Orr, J. A.", "StillImage", "Texas A & M University--Maps", "Official city map of the city of College Station, Texas"],
      "_text_": ["Orr, J. A.", "StillImage", "Texas A & M University--Maps", "Official city map of the city of College Station, Texas"],
      "date_issued": [1941],
      "reformatting": ["application/tif", "reformatted digital"],
      "reformatting_facet": ["application/tif", "reformatted digital"],
      "genre": ["StillImage"],
      "genre_facet": ["StillImage"],
      "local_coordinates": ["(W 96°21ʹ23ʺ--W 96°18ʹ42ʺ/N 30°38ʹ04ʺ--N 30°35ʹ45ʺ)"],
      "local_coordinates_string": ["(W 96°21ʹ23ʺ--W 96°18ʹ42ʺ/N 30°38ʹ04ʺ--N 30°35ʹ45ʺ)"],
      "id": "aHR0cHM6Ly9hcGkubGlicmFyeS50YW11LmVkdS9mY3JlcG8vcmVzdC8zYi82Zi9jMy8yNS8zYjZmYzMyNS1mNmNhLTQxZDgtYjkxZS04YzVkYjNiZThjMTMvYnJhem9zLW1hcHNfb2JqZWN0cy84OQ==",
      "local_digital_identifier": ["https://api.library.tamu.edu/fcrepo/rest/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89"],
      "local_digital_identifier_text": ["https://api.library.tamu.edu/fcrepo/rest/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89"],
      "local_digital_identifier_facet": ["https://api.library.tamu.edu/fcrepo/rest/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89"],
      "manifest": "https://api.library.tamu.edu/iiif-service/fedora/presentation/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89",
      "rights_access": ["A copyright review process in November 2020 has determined that this particular item is still in copyright, held by the publisher, the City of College Station, Texas, who graciously shared permission for Texas A&M University Libraries to display this image in this online exhibit. The written permission of any copyright and other rights holders is required for distribution, reproduction, or other use that extends beyond what is authorized by fair use and other statutory exemptions. Responsibility for making an independent legal assessment of an item and securing any necessary permissions ultimately rests with persons desiring to use the item. http://rightsstatements.org/vocab/InC/1.0/"],
      "spatial_multi": ["College Station (Tex.)"],
      "spatial_multi_string": ["College Station (Tex.)"],
      "standard_digital_identifier": ["3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89"],
      "standard_digital_identifier_text": ["3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89"],
      "standard_digital_identifier_facet": ["3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89"],
      "subject": ["Texas A & M University--Maps"],
      "subject_facet": ["Texas A & M University--Maps"],
      "subject_ws": ["Texas A & M University--Maps"],
      "title": "Official city map of the city of College Station, Texas",
      "title_text_si_en_split": "Official city map of the city of College Station, Texas",
      "title_facet": ["Official city map of the city of College Station, Texas"],
      "timestamp": "2026-05-08T20:40:14.725Z"
    }

Solr 6 Document Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
      "id": "aHR0cHM6Ly9hcGkubGlicmFyeS50YW11LmVkdS9mY3JlcG8vcmVzdC8zYi82Zi9jMy8yNS8zYjZmYzMyNS1mNmNhLTQxZDgtYjkxZS04YzVkYjNiZThjMTMvYnJhem9zLW1hcHNfb2JqZWN0cy84OQ==",
      "title": "Official city map of the city of College Station, Texas",
      "title_txt_en_split": "Official city map of the city of College Station, Texas",
      "creator": ["Orr, J. A."],
      "subject": ["Texas A & M University--Maps"],
      "local_digital_identifier": ["https://api.library.tamu.edu/fcrepo/rest/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89"],
      "collection": ["https://api.library.tamu.edu/fcrepo/rest/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects"],
      "manifest": "https://api.library.tamu.edu/iiif-service/fedora/presentation/3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89",
      "application_type": "fedora",
      "content_type": ["StillImage"],
      "rights_access": ["A copyright review process in November 2020 has determined that this particular item is still in copyright, held by the publisher, the City of College Station, Texas, who graciously shared permission for Texas A&M University Libraries to display this image in this online exhibit. The written permission of any copyright and other rights holders is required for distribution, reproduction, or other use that extends beyond what is authorized by fair use and other statutory exemptions. Responsibility for making an independent legal assessment of an item and securing any necessary permissions ultimately rests with persons desiring to use the item. http://rightsstatements.org/vocab/InC/1.0/"],
      "genre": ["StillImage"],
      "spatial_multi": ["College Station (Tex.)"],
      "spatial_txt_en_split_multi": ["College Station (Tex.)"],
      "standard_digital_identifier": ["3b/6f/c3/25/3b6fc325-f6ca-41d8-b91e-8c5db3be8c13/brazos-maps_objects/89"],
      "reformatting": ["application/tif", "reformatted digital"],
      "local_coordinates": "(W 96°21ʹ23ʺ--W 96°18ʹ42ʺ/N 30°38ʹ04ʺ--N 30°35ʹ45ʺ)",
      "date_issued": "1941",
      "_version_": 1840544036712087554,
      "timestamp": "2025-08-15T17:39:35.995Z",
      "score": 8.481773
    }

.. _adding-documents:

Adding Documents via the Solr API
----------------------------------

To manually recreate a missing document, POST it to Solr's JSON update handler. The
``commit=true`` parameter flushes the document to the index immediately; omit it if you
are batching multiple updates and want to commit once at the end.

.. important::

   Replace ``<solr-host>``, ``<port>``, and ``<collection>`` with the values for your
   environment. The ``id`` field must be unique within the collection.

Using ``curl``
~~~~~~~~~~~~~~

.. code-block:: bash

    curl -X POST \
      "http://<solr-host>:<port>/solr/<collection>/update?commit=true" \
      -H "Content-Type: application/json" \
      -d '[
        {
          "id": "<unique-base64-id>",
          "title": "My Document Title",
          "application_type": "fedora",
          "application_type_facet": ["fedora"],
          "content_type": ["StillImage"],
          "content_type_facet": ["StillImage"],
          "timestamp": "2026-05-08T00:00:00.000Z"
        }
      ]'

.. note::

   The body must be a JSON **array** even when adding a single document. Solr's update
   handler accepts one or more documents in a single request.

Using Python (``requests``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import requests

    SOLR_URL = "http://<solr-host>:<port>/solr/<collection>/update"

    document = {
        "id": "<unique-base64-id>",
        "title": "My Document Title",
        "application_type": "fedora",
        "application_type_facet": ["fedora"],
        "content_type": ["StillImage"],
        "content_type_facet": ["StillImage"],
        "timestamp": "2026-05-08T00:00:00.000Z",
    }

    response = requests.post(
        SOLR_URL,
        params={"commit": "true"},
        json=[document],
    )
    response.raise_for_status()
    print(response.json())

Verifying the Document Was Added
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After posting, confirm the document is indexed by querying for its ``id``:

.. code-block:: bash

    curl "http://<solr-host>:<port>/solr/<collection>/select?q=id:<unique-base64-id>&wt=json"

.. note::

   Base64 ``id`` values often contain characters (``+``, ``/``, ``=``) that must be
   URL-encoded when used in a query string. Use ``q=id:"<id>"`` with quotes, or
   percent-encode the value.
