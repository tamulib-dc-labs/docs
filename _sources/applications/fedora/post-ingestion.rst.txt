===============
Reindexing Solr
===============

-----
About
-----

Sometimes, Solr needs to be reindexed.  Depending on the health of the server this could be after MAGPIE ingests
something or when you need to reindex everything after changing ldpath.  This document attempts to explain those
processes.

-----------
Post Ingest
-----------

After MagPie runs, you may need to make Fedora index the documents in Solr.

Since we have moved to Rancher from Chef, Solr documents do not always get written automatically  to fcrepo’s Solr
instance. The same goes for the triple store. As a result, you must trigger it by shelling into fcrepo and posting
an HTTP request against the Fedora Reindexing Service.

-------
Running
-------

Connect to the :code:`fedora` pod or wherever fedora is running via shell.  You can do this in Rancher or via
kubectl.

Once inside the container (pod), you can get useful information about the service via cURL:

.. code-block:: shell

    curl http://localhost:9080/reindexing


To reindex, you need to make a POST to the defined re-indexing endpoint, and it will begin to traverse the Fedora
repository at that point, sending “re-indexing” hints to the specified services (there are no default services
defined). Currently, there is no way to target specific Fedora resources with this method.

.. code-block:: shell

    curl -X POST http://localhost:9080/reindexing/ -H "Content-Type: application/json" -d '["broker:queue:solr.reindex","broker:queue:triplestore.reindex"]'

Note, running the command above should reindex Solr and Fuseki.  You can remove the Fuseki command if unneeded.

.. code-block:: shell

    curl -X POST http://localhost:9080/reindexing/ -H "Content-Type: application/json" -d '["broker:queue:solr.reindex"]'

-------------------------------------
Redeploying and Removing Health Check
-------------------------------------

Before you do this, you may need to remove the healthcheck and redeploy pods. 

The settings for the healthcheck should look something like this:

.. image:: ../../_static/images/health-check.png

You can access this page from :code:`Workloads -> Pod Name (fedora) -> Config -> Health Check`

----------
Monitoring
----------

After running the reindex, you can then watch the logs to make sure every thing is running well like so:

.. code-block:: shell

    # karaf log:
    tail -f /usr/local/karaf/data/log/karaf.log
    ls -al /usr/local/karaf/data/log/

If nothing happens, you need to redploy or remove the health check.  I recommend first trying a redeploy of 
:code:`fedora` and :code:`fedora-solr`.  If that doesn't work, remove the health check.

It is still unclear exactly what needs to happen for this to work. We have also seen where adding the liveliness
check back seems to make things start working again.
