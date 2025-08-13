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

Let's pretend we want to get all traffic between :code:`2025-08-01` and :code:`2025-08-10`.  We can perform a search on the :code:`time` field like :code:`time:[2025-08-01T00:00:00Z TO 2025-08-10T23:59:59Z]`.
Doing a search only for this string will search traffic across all communities and return :code:`174282` documents.

Eliminating Bots
================

:code:`time:[2025-08-01T00:00:00Z TO 2025-08-10T23:59:59Z] AND isBot:false`

https://rancher.library.tamu.edu/k8s/clusters/c-kd2s7/api/v1/namespaces/oaktrust/services/http:dspace-solr:80/proxy/solr/statistics/select?indent=true&q.op=OR&q=time%3A%5B2025-08-01T00%3A00%3A00Z%20TO%202025-08-10T23%3A59%3A59Z%5D%20AND%20isBot%3Afalse

Getting Item Based Stats
========================

Let's pretend we want to get all traffic
