===========
Using Karaf
===========

Occasionally, you might want to monitor things in Karaf to check that active mq messaging is still working.  
This is useful when doing things like reindexing or updating the triplestore. This section will cover some 
commands we use for various things.

------------------
camel:context-list
------------------

:code:`camel:context-list` is used to list all the active Camel contexts running inside the Karaf container.
It helps you monitor and inspect which Camel contexts are currently deployed, their status 
(Started/Stopped/Suspended), uptime, messages in-flight, and more.

A Camel context is essentially a runtime container for Apache Camel routes. Each context can have its own 
configuration and set of routes.

Examples of When to Use
=======================

Fedora Solr indexing is frought with issues and often things fail quite often.  :code:`camel:context-list`
can help us predict when something might fail. For instance, when the :code:`FcrepoIndexer` context stops growing,
we can guess how long it will take until things need to be restarted.

.. code:: shell

    Context                    Status              Total #       Failed #     Inflight #   Uptime          
    -------                    ------              -------       --------     ----------   ------          
    FcrepoFixity               Started                   0              0              0   36.829 seconds  
    FcrepoIndexer              Started                 281              0              1   34.880 seconds  
    FcrepoLDPathContext        Started                  76              0              3   35.276 seconds  
    FcrepoSerialization        Started                   0              0              0   34.511 seconds  
    FcrepoSolrIndexer          Started                 115              0              4   36.286 seconds  
    FcrepoTriplestoreIndexer   Started                   0              0              0   35.543 seconds  
    camel-1                    Started                   0              0              0   37.419 seconds  

Above, :code:`FcrepoIndexer` has one message in flight, but the total messages has stopped growing and is
stuck at 281.  Even Thought FcrepoSolrIndexer is still growing, it will ultimately stop around 846. At 
this point the pod probably needs to be kicked.

----------------
camel:route-info
----------------

If you want info about a context route, you can run :code:`camel:route-info <context> <id>` or do a wild
card like `camel:route-info FcrepoIndexer *`.  This will return info like:

.. code-block:: shell

    Camel Route FcrepoReindexingRecipients
	Camel Context: FcrepoIndexer
	State: Started
	State: Started


    Statistics
        Exchanges Total: 141
        Exchanges Completed: 141
        Exchanges Failed: 0
        Exchanges Inflight: 0
        Min Processing Time: 2 ms
        Max Processing Time: 64 ms
        Mean Processing Time: 4 ms
        Total Processing Time: 658 ms
        Last Processing Time: 12 ms
        Delta Processing Time: 9 ms
        Start Statistics Date: 2025-06-27 16:32:56
        Reset Statistics Date: 2025-06-27 16:32:56
        First Exchange Date: 2025-06-27 16:33:06
        Last Exchange Date: 2025-06-27 16:33:22
    Camel Route FcrepoReindexingReindex
        Camel Context: FcrepoIndexer
        State: Started
        State: Started


    Statistics
        Exchanges Total: 0
        Exchanges Completed: 0
        Exchanges Failed: 0
        Exchanges Inflight: 0
        Min Processing Time: 0 ms
        Max Processing Time: 0 ms
        Mean Processing Time: -1 ms
        Total Processing Time: 0 ms
        Last Processing Time: -1 ms
        Delta Processing Time: 0 ms
        Start Statistics Date: 2025-06-27 16:32:56
        Reset Statistics Date: 2025-06-27 16:32:56
        First Exchange Date: 1969-12-31 23:59:59
        Last Exchange Date: 1969-12-31 23:59:59
    Camel Route FcrepoReindexingRest
        Camel Context: FcrepoIndexer
        State: Started
        State: Started


    Statistics
        Exchanges Total: 0
        Exchanges Completed: 0
        Exchanges Failed: 0
        Exchanges Inflight: 0
        Min Processing Time: 0 ms
        Max Processing Time: 0 ms
        Mean Processing Time: -1 ms
        Total Processing Time: 0 ms
        Last Processing Time: -1 ms
        Delta Processing Time: 0 ms
        Start Statistics Date: 2025-06-27 16:32:56
        Reset Statistics Date: 2025-06-27 16:32:56
        First Exchange Date: 1969-12-31 23:59:59
        Last Exchange Date: 1969-12-31 23:59:59
    Camel Route FcrepoReindexingTraverse
        Camel Context: FcrepoIndexer
        State: Started
        State: Started


    Statistics
        Exchanges Total: 140
        Exchanges Completed: 140
        Exchanges Failed: 0
        Exchanges Inflight: 1
        Min Processing Time: 77 ms
        Max Processing Time: 990 ms
        Mean Processing Time: 112 ms
        Total Processing Time: 15803 ms
        Last Processing Time: 92 ms
        Delta Processing Time: 1 ms
        Start Statistics Date: 2025-06-27 16:32:56
        Reset Statistics Date: 2025-06-27 16:32:56
        First Exchange Date: 2025-06-27 16:33:07
        Last Exchange Date: 2025-06-27 16:33:22
    Camel Route FcrepoReindexingUsage
        Camel Context: FcrepoIndexer
        State: Started
        State: Started


    Statistics
        Exchanges Total: 0
        Exchanges Completed: 0
        Exchanges Failed: 0
        Exchanges Inflight: 0
        Min Processing Time: 0 ms
        Max Processing Time: 0 ms
        Mean Processing Time: -1 ms
        Total Processing Time: 0 ms
        Last Processing Time: -1 ms
        Delta Processing Time: 0 ms
        Start Statistics Date: 2025-06-27 16:32:56
        Reset Statistics Date: 2025-06-27 16:32:56
        First Exchange Date: 1969-12-31 23:59:59
        Last Exchange Date: 1969-12-31 23:59:59

----------------------
camel:context-inflight
----------------------

You can get a list on inflight exchanges like :code:`camel:context-inflight [options] name [route]`.

If you don't supply a route id, it will give you everything.  For example, :code:`camel:context-inflight FcrepoIndexer`
will give you everything:

.. code-block:: shell

     ExchangeId                                        From Route                 Route                      Node           Elapsed (ms)   Duration (ms)  
    ----------                                        ----------                 -----                      ----           ------------   -------------  
    ID-fedora-7bc74df8f9-ll95s-1751043960041-5-1403   FcrepoReindexingTraverse   FcrepoReindexingTraverse   split1                    0          291059  
    ID-fedora-7bc74df8f9-ll95s-1751043960041-5-1408   FcrepoReindexingTraverse   FcrepoReindexingTraverse   to49                      0          291059

