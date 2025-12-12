=============================
OAKTrust and DSPACE Statistcs
=============================

-----------------------------
Accessing Statistics via Solr
-----------------------------

DSPACE traffic is written to a solr core called :code:`statistcs`.  Each document looks like:

.. code-block:: json

    {
        "ip":"162.158.174.218",
        "referrer":"https://oaktrust.library.tamu.edu/collections/5375f882-869a-418f-b40e-0191ba379fa3",
        "dns":"162.158.174.218",
        "userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "isBot":false,
        "continent":"NA",
        "countryCode":"US",
        "city":"Dallas",
        "latitude":32.7767,
        "longitude":-96.797,
        "id":"22ab66ce-cfcc-4a8e-ac3f-3ce2238d1da3",
        "type":0,
        "owningItem":["7ed85e6e-21f9-4373-ac88-758ba0d579b2"],
        "owningColl":["5375f882-869a-418f-b40e-0191ba379fa3"],
        "owningComm":["ee1165a9-f6b9-4b93-8471-9e4bbee03d04",
          "e55ccac8-4d31-431f-9320-058cc3a708ab",
          "ed9a1370-076a-4cc0-bf87-25ae04053a36"],
        "time":"2025-08-01T20:58:28.617Z",
        "bundleName":["THUMBNAIL"],
        "statistics_type":"view",
        "uid":"8db5cc7c-1cb6-47c0-8bdd-06b86fac8d42"
    }

Based on the document, you can see a number of strategies for getting data about a community, collection, or specific item.  The section below will cover reproduceable ways of creating reports for this.


Getting Time Based Stats
========================

Let's pretend we want to get all traffic between :code:`2025-08-01` and :code:`2025-08-10` in OAKTrust.  We can perform
a search on the :code:`time` field like :code:`time:[2025-08-01T00:00:00Z TO 2025-08-10T23:59:59Z]`.
Doing a search only for this string will search traffic across all communities and return
:code:`174282` documents as formatted like:

.. code-block:: json

    {
        "ip":"162.158.155.223",
        "referrer":"https://oaktrust.library.tamu.edu/bitstreams/ab61984f-c44a-4b78-bfd9-661a1c6557c4/download",
        "dns":"162.158.155.223",
        "userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
        "isBot":false,
        "continent":"NA",
        "countryCode":"US",
        "city":"Newark",
        "latitude":40.7357,
        "longitude":-74.1724,
        "id":"ab61984f-c44a-4b78-bfd9-661a1c6557c4",
        "type":0,
        "owningItem":["8cdd8f6a-dbb3-4a91-96f5-c8a3c81549b1"],
        "owningColl":["a213b1c3-40ff-49a8-a954-38b802e1aa1f",
          "f1fab458-eb4f-4acd-aba9-9c7b08f26730"],
        "owningComm":["5396a3df-85e9-4aef-ae08-13e1e164e55c",
          "9d351faf-09e6-469f-9a26-24bca6d907f6",
          "af0dfacd-b0f2-4f51-b2dd-e63f17519b4f",
          "ed9a1370-076a-4cc0-bf87-25ae04053a36"],
        "time":"2025-08-01T00:00:50.557Z",
        "bundleName":["ORIGINAL"],
        "statistics_type":"view",
        "uid":"4b4d537c-a48c-4486-9a2d-852de113f330"
    }


Eliminating Bots
================

You can remove bot traffic by expanding your query to include
:code:`time:[2025-08-01T00:00:00Z TO 2025-08-10T23:59:59Z] AND isBot:false`. This reduces documents to :code:`110246`.

If you want to avoid the Solr interface entirely, you can do this like so:

https://rancher.library.tamu.edu/k8s/clusters/c-kd2s7/api/v1/namespaces/oaktrust/services/http:dspace-solr:80/proxy/solr/statistics/select?indent=true&q.op=OR&q=time%3A%5B2025-08-01T00%3A00%3A00Z%20TO%202025-08-10T23%3A59%3A59Z%5D%20AND%20isBot%3Afalse

Getting Item Based Stats
========================

Let's pretend we want to find out which collections have gotten the most traffic in the month of October 2025. By
collections, we mean we want to find the owning collections of the most popular items over the past month.
