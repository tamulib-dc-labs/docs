=======================
Solving Open Oni Issues
=======================

----------------------------------------------
Solr Fails to Spin down and Spin Up Graciously
----------------------------------------------

Sometimes, users will report that search is broken in Open Oni.  When this happens, it's almost always due to the Solr
pod failing to gracefully terminate and restart.  When the new pod is scheduled elsewhere, it encounters a
:code:`write.lock` error and refuses to start.  To understand the problem better, see the Arguments and WorkingDir of
the exec in Rancher:

.. image:: ../_static/images/oni-exec.png
    :alt: Open Oni Exec

To fix:

1. Shell into the Solr pod
2. :code:`rm openoni/data/index/write.lock`
3. Redeploy the pod.