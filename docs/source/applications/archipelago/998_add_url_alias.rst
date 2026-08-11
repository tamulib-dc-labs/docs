========================
Add URL alias for a Node
========================

In Archipelago, we sometimes need a prettier link for a node. This should only be done for collections, and the
System path must be based on the node id, not the uuid (which Archipelago also treats as an alias).

-----
Steps
-----

* Visit :code:`/admin/config/search/path/add`
* In **System path**, enter the node's path, e.g. :code:`/node/123`
* In **URL alias**, enter the desired friendly path, e.g. :code:`/collections/my-collection`
* Save