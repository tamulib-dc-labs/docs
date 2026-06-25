============================
Batches: Loading and Purging
============================

---------------
Batch Structure
---------------

A batch is a directory conforming to the `NDNP (National Digital Newspaper Program) <https://www.loc.gov/ndnp/>`_ specification.
The top-level directory name follows the pattern ``batch_{awardee}_{name}_ver{NNN}``, for example ``batch_txa_aggie_ver009``.

Inside the batch root is a single ``data/`` directory containing a ``batch.xml`` manifest and one subdirectory per
newspaper title (named by LCCN)::

    batch_txa_aggie_ver009/
    └── data/
        ├── batch.xml
        └── sn84009780/
            └── print/
                ├── 1990010101/
                │   ├── 1990010101.xml
                │   ├── 0001.jp2
                │   ├── 0001.pdf
                │   ├── 0001.xml
                │   ├── 0002.jp2
                │   ├── 0002.pdf
                │   ├── 0002.xml
                │   └── ...
                ├── 1990030101/
                │   └── ...
                └── ...

``batch.xml``
=============

The ``batch.xml`` file is an NDNP manifest that enumerates every issue in the batch. Each ``<issue>`` element records the newspaper's LCCN, the issue date, the edition order, and the relative path to that issue's METS/MODS file:

.. code-block:: xml

    <ndnp:batch name="batch_txa_aggie_ver009" awardee="txa" ...>
      <issue lccn="sn84009780" issueDate="1990-01-01" editionOrder="01">
        sn84009780/print/1990010101/1990010101.xml
      </issue>
      ...
    </ndnp:batch>

Issue directories
=================

Each issue lives in a directory named ``YYYYMMDDEE``, where ``YYYYMMDD`` is the publication date and ``EE`` is the zero-padded edition order (e.g., ``1990010101`` = January 1, 1990, edition 1).

The directory contains one METS/MODS XML file (named to match the directory) plus three files per page, numbered sequentially from ``0001``:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - File
     - Description
   * - ``YYYYMMDDEE.xml``
     - Issue-level METS/MODS file containing bibliographic metadata (title, volume, issue number, date) and a file inventory for every page in the issue.
   * - ``NNNN.jp2``
     - JPEG 2000 image of the page.
   * - ``NNNN.pdf``
     - PDF of the page.
   * - ``NNNN.xml``
     - ALTO (Analyzed Layout and Text Object) OCR XML with word-level text and positional coordinates used by open-oni for full-text search.

---------------
Loading a Batch
---------------

Connect to Open Oni's web pod. Run ``kubectl get pods -n newspaper``:

NAME                    READY   STATUS    RESTARTS   AGE
rais-6795576f66-vrt9t   1/1     Running   0          3d16h
solr-8c7cdddc7-gt9w7    1/1     Running   0          3d16h
web-6ffcbdbf5-m95q9     1/1     Running   0          3d16h

Assuming you've already copied your files to the pod, just connect: ``kubectl exec -it web-6ffcbdbf5-m95q9 -n newspaper -- bash``

Now, activate your virtual environment so you can use python:  ``source ENV/bin/activate``

Now load batch like:  ``./manage.py load_batch /opt/openoni/data/batches/batch_txa_aggie_ver009/
chmod -R 777 /var/tmp/django_cache``