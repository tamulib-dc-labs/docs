================================
Aggieland Through Time Analytics
================================

The interactive map on *Aggieland Through Time* (``/map/``) reports clicks on
building markers and marker clusters to Google Analytics 4. This page lists
the events the map sends, their parameters, and the custom dimensions and
metrics registered in GA4 to report on them.

--------
Overview
--------

* **Property:** ``G-CJRKTHT0N0`` (this is just for testing and will be moved to main)
* **Tagging:** ``gtag.js`` is loaded directly by the site's ``<GoogleAnalytics>``
  component in ``content/_app.mdx``. Google Tag Manager is **not** used, so no
  GTM tags or triggers are needed.
* **Source:** ``app/components/MapWithDateSlider.client.tsx``, in the
  ``trackMapEvent()`` helper and the marker sync effect.

Each click is reported in two ways:

#. A GA4 event sent with ``gtag("event", ...)``.
#. A browser ``CustomEvent`` dispatched on ``window``. It carries the
   complete, untruncated data for other scripts on the page to use.

------
Events
------

``map_marker_click``
~~~~~~~~~~~~~~~~~~~~

Sent when a visitor clicks a single building marker. This also happens when
the visitor clicks a marker after markers are ungrouped, or after zooming far
enough in that clustering turns off.

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Parameter
     - Type
     - Description
   * - ``building_id``
     - string
     - Feature ID of the marker, e.g. ``allen-building-point-1``.
   * - ``building_title``
     - string
     - Building name from the IIIF manifest, e.g. ``Allen Building``.
   * - ``building_href``
     - string
     - Path to the building's work page, e.g. ``/works/allen-building.html``.
   * - ``map_zoom``
     - number
     - Leaflet zoom level when the visitor clicked.
   * - ``start_year``
     - number
     - Start year on the date slider when the visitor clicked.
   * - ``end_year``
     - number
     - End year on the date slider when the visitor clicked.

``map_cluster_click``
~~~~~~~~~~~~~~~~~~~~~

Sent when a visitor clicks a numbered cluster of markers. The map then zooms
in on the cluster or spreads it out. ``map_zoom`` is the zoom level *before*
that happens.

.. list-table::
   :header-rows: 1
   :widths: 20 12 68

   * - Parameter
     - Type
     - Description
   * - ``cluster_size``
     - number
     - Number of buildings in the cluster.
   * - ``cluster_titles``
     - string
     - Building names in the cluster, separated by semicolons. Values longer
       than 100 characters are cut off and end with ``…``.
   * - ``cluster_lat``
     - number
     - Latitude of the cluster's center, rounded to 5 decimal places.
   * - ``cluster_lng``
     - number
     - Longitude of the cluster's center, rounded to 5 decimal places.
   * - ``map_zoom``
     - number
     - Leaflet zoom level when the visitor clicked.
   * - ``start_year``
     - number
     - Start year on the date slider when the visitor clicked.
   * - ``end_year``
     - number
     - End year on the date slider when the visitor clicked.

.. note::

   GA4 rejects event parameter values longer than 100 characters. The map
   shortens every string parameter to 100 characters before sending it. For
   the complete list of buildings in a cluster, use the browser event
   described in `Browser events`_.

Custom definitions in GA4
-------------------------

GA4 does not show event parameters in standard reports or Explorations until
they are registered as custom definitions. These are registered on the
property.

Custom dimensions
~~~~~~~~~~~~~~~~~

All of these use **Event** scope.

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Dimension name
     - Event parameter
     - Used by
   * - Building title
     - ``building_title``
     - ``map_marker_click``
   * - Building ID
     - ``building_id``
     - ``map_marker_click``
   * - Building URL
     - ``building_href``
     - ``map_marker_click``
   * - Cluster buildings
     - ``cluster_titles``
     - ``map_cluster_click``
   * - Map start year
     - ``start_year``
     - both events
   * - Map end year
     - ``end_year``
     - both events
   * - Map zoom
     - ``map_zoom``
     - both events

Custom metrics
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 25 20 30

   * - Metric name
     - Event parameter
     - Unit
     - Used by
   * - Cluster size
     - ``cluster_size``
     - Standard
     - ``map_cluster_click``

``cluster_size`` is a metric rather than a dimension so that GA4 can sum it,
average it, and compare it.

Parameters that are not registered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``cluster_lat`` and ``cluster_lng`` are sent but not registered. Raw
coordinates are of little use in GA4 reports, and registering them would use
up dimension slots (a standard property allows 50 event-scoped custom
dimensions). They can still be seen in DebugView and in a BigQuery export.

Registering a custom definition
-------------------------------

#. Open the property in `Google Analytics <https://analytics.google.com>`_.
#. Click **Admin** (the gear icon, bottom left).
#. Under **Data display**, click **Custom definitions**.
#. Choose the **Custom dimensions** or **Custom metrics** tab, then click
   **Create custom dimension** or **Create custom metric**.
#. Enter the name, scope (**Event**), and event parameter from the tables
   above. For a metric, set the unit of measurement to **Standard**.
#. Click **Save**.

.. important::

   Custom definitions are **not retroactive**. They fill in only for events
   received after the definition is created. Standard reports can take
   24–48 hours to show new data.

Checking events
---------------

**DebugView.** Install the `Google Analytics Debugger
<https://chromewebstore.google.com/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna>`_
Chrome extension and turn it on. Then open **Admin → DebugView** in GA4 and
click markers and clusters on the live map. Events show up within seconds,
with their parameters.

**Browser console.** To watch what the map sends without GA, paste this into
the browser console on the map page:

.. code-block:: javascript

   window.addEventListener("canopy-map:marker-click", (e) => console.log(e.detail));
   window.addEventListener("canopy-map:cluster-click", (e) => console.log(e.detail));

.. warning::

   The local dev server loads the same GA property. Clicks made while testing
   locally are recorded alongside production traffic.

Example reports
---------------

Build these in **Explore → Free-form**.

**Most-clicked buildings**
   Filter: *Event name* exactly matches ``map_marker_click``.
   Rows: *Building title*. Values: *Event count*.

**Cluster usage by zoom level**
   Filter: *Event name* exactly matches ``map_cluster_click``.
   Rows: *Map zoom*. Values: *Event count*, *Cluster size* (average).

**Which eras visitors browse**
   Filter: *Event name* exactly matches ``map_marker_click``.
   Rows: *Map start year*, *Map end year*. Values: *Event count*.

Browser events
--------------

Besides the GA4 events, the map dispatches ``CustomEvent`` objects on
``window``. Their ``detail`` holds the complete data with nothing cut off.

``canopy-map:marker-click``
   .. code-block:: json

      {
        "marker": {
          "id": "allen-building-point-1",
          "title": "Allen Building",
          "href": "/works/allen-building.html",
          "lat": 30.5975,
          "lng": -96.3526,
          "dateBuilt": 1997,
          "dateRazed": null,
          "standing": true
        },
        "zoom": 13,
        "startYear": 1876,
        "endYear": 2025
      }

``canopy-map:cluster-click``
   .. code-block:: json

      {
        "count": 176,
        "markers": [ { "id": "...", "title": "...", "...": "..." } ],
        "center": { "lat": 30.6146, "lng": -96.3419 },
        "bounds": "-96.3668,30.5904,-96.3278,30.6370",
        "zoom": 13,
        "startYear": 1876,
        "endYear": 2025
      }

``markers`` lists every building in the cluster, in the same shape as
``marker`` above. ``bounds`` is ``west,south,east,north``. ``dateRazed`` is
``null`` for buildings that are still standing.