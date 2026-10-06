Creating an Ingress in Rancher
==============================

This guide shows how to expose a path on a hostname through a Kubernetes
Ingress in Rancher. The example routes the bare root of
``https://exhibits.library.tamu.edu/`` to the ``exhibits`` service, which
serves the landing page (``index.html``).


How it works
------------

An Ingress is a set of routing rules. Each rule maps a **host** and **path**
to a **service** and **port** inside the cluster. Our clusters use the
**Traefik** ingress controller, so every Ingress sets
``ingressClassName: traefik``.

You can have several Ingresses for the same host. Traefik merges their rules,
so a new path can go in its own Ingress without editing an existing one. For
example, ``/aggieland-through-time`` is handled by the ``exhibits`` Ingress,
and ``/`` is handled by the ``exhibits-root`` Ingress below.


The example Ingress
-------------------

.. literalinclude:: exhibits-root-ingress.yaml
   :language: yaml
   :caption: exhibits-root-ingress.yaml

Key fields:

``metadata.name``
   A name that is unique within the namespace, such as ``exhibits-root``.

``metadata.namespace``
   The namespace where the target service lives, here ``archipelago``. An
   Ingress can only route to services in its own namespace.

``spec.rules[].host``
   The public hostname. DNS for this name must already point at the cluster's
   load balancer.

``path`` and ``pathType``
   ``path: /`` with ``pathType: Exact`` matches **only** the bare root URL.
   The ``exhibits`` web server answers ``/`` with ``index.html``.

``backend.service``
   The Kubernetes service name and port that receive the traffic.

``tls``
   Enables HTTPS for the host. With no ``secretName``, Traefik uses the
   cluster's default certificate.

.. note::

   Choosing between ``Exact`` and ``Prefix``:

   * ``Exact``: ``/`` matches only ``/``. Any other path on the host still
     needs its own rule.
   * ``Prefix``: ``/`` matches **every** path on the host. That is convenient
     when the whole host goes to one service, but it will silently capture
     any path you meant to route elsewhere later.

.. warning::

   If ``index.html`` loads CSS, JavaScript, or images from paths that no rule
   matches (for example ``/assets/...``), those requests will return 404.
   Add rules for those paths, or switch to ``pathType: Prefix``.


Creating it in Rancher
----------------------

Using the Ingress form
~~~~~~~~~~~~~~~~~~~~~~

#. In Rancher, open the cluster and go to
   **Service Discovery → Ingresses**.
#. Click **Create**.
#. Click **Edit as YAML**, paste the YAML above, and click **Create**.

Using Import YAML
~~~~~~~~~~~~~~~~~

#. Click the **Import YAML** button (⬆) in the top bar of the cluster view.
#. Set the default namespace to ``archipelago``.
#. Paste the YAML and click **Import**.

Using kubectl
~~~~~~~~~~~~~

If you have a kubeconfig for the cluster:

.. code-block:: console

   $ kubectl apply -f exhibits-root-ingress.yaml


Verifying
---------

Check that the Ingress exists:

.. code-block:: console

   $ kubectl -n archipelago get ingress exhibits-root

Then request the root URL. You should get a ``200`` response:

.. code-block:: console

   $ curl -I https://exhibits.library.tamu.edu/

Also confirm that existing paths still work:

.. code-block:: console

   $ curl -I https://exhibits.library.tamu.edu/aggieland-through-time


Tip: copying an existing Ingress
--------------------------------

When you start from an Ingress exported from Rancher, delete the fields
Kubernetes generates before reusing it:

* ``metadata.managedFields``
* ``metadata.resourceVersion``
* ``metadata.uid``
* ``metadata.creationTimestamp``
* ``metadata.generation``
* the ``kubectl.kubernetes.io/last-applied-configuration`` annotation
* the entire ``status`` block
