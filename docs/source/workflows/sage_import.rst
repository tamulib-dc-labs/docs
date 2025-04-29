===========
SAGE Import
===========

`Placeholder instructions <https://tamulib.atlassian.net/wiki/spaces/DIDP/pages/989921286/Creating+a+SAGE+Collection+from+Scratch>`_

---------------------------------------
How to Use the Solr API via the Browser
---------------------------------------

In order to build a collection in SAGE, you must first start with a SOLR query that will give you all the works that
belong to a collection in Fedora. Because our Solr index follows our Fedora models closely, this isn't always easy to
guess, so you often times need to experiment with a few requests to determine the string to add to your READER in SAGE.

Our Solr instances aren't publicly available, so you have two choices:

1. Find a pod in Rancher with :code:`curl` installed and make a request via the Solr API or
2. Make a proxy request via Rancher to Solr in your browser.

In order to do number 2, the pod in Rancher must have an additional port forwarded to :code:`80`, :code:`8080`, or
:code:`443`. You can tell if this is enabled by accessing the :code:`Services` tab in the pod. If this has been done,
the :code:`Target` tab will have an anchor.

Assuming an additional port has been added to the pod, you should be able to do a request like this:

https://rancher-devpre.library.tamu.edu/k8s/clusters/c-8vksj/api/v1/namespaces/fcrepo4/services/http:fedora-solr:80/proxy/fcrepo-solr/fedora-core/select?indent=on&q=hasParent:%22https://api-pre.library.tamu.edu/fcrepo/rest/bb/97/f2/3e/bb97f23e-803a-4bd6-8406-06802623554c/cherokee_freedmen_objects%22&wt=json&&rows=10000

This will require authenticating to Rancher first as you'll be proxying your request through it.
