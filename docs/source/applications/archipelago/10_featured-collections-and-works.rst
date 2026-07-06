=====================================
Featured Collections and Featured Works
=====================================

The TAMU Digital Collections front page displays two curated sections:
**Featured Collections** and **Featured Works**. These views surface hand-picked
content to site visitors by curators. Both sections are driven by Drupal's core
``promote`` field, a Search API Solr view, and a small amount of custom
theme code.

-----------
How It Works
-----------

The overall flow for both sections is identical:

1. An editor checks a **"Featured on front page"** checkbox on a node edit form.
2. The checkbox saves ``1`` to the node's core ``promote`` field.
3. A Search API Solr view filters for ``promote = 1`` and renders matching
   nodes as cards.
4. The view block is placed on the front page and restricted to ``<front>``
   via block visibility settings.

-------------------
The Promote Checkbox
-------------------

Drupal's ``promote`` field exists on all node types but is hidden by default
in Archipelago. The TAMU theme exposes it through two
``hook_form_FORM_ID_alter`` implementations in
``web/themes/custom/tamu_theme/tamu_theme.theme``.

**For Digital Object Collections:**

.. code-block:: php

   function tamu_theme_form_node_digital_object_collection_edit_form_alter(
       &$form, FormStateInterface $form_state, $form_id)

**For Digital Objects:**

.. code-block:: php

   function tamu_theme_form_node_digital_object_edit_form_alter(
       &$form, FormStateInterface $form_state, $form_id)

Both hooks add a checkbox to the **Advanced** sidebar of the node edit form
and attach a shared submit handler:

.. code-block:: php

   function tamu_theme_promote_node_submit($form, FormStateInterface $form_state) {
     $node = $form_state->getFormObject()->getEntity();
     $node->set('promote', (int) $form_state->getValue('tamu_promote'));
     $node->save();
   }

.. note::

   After checking or unchecking the box and saving, the Search API Solr
   index must pick up the change. This usually happens within a few minutes
   via cron. To force it immediately go to
   **Configuration → Search API → [your index] → Queue all items → Index now**.

-----------
Solr Index
-----------

The ``promote`` field must be present in the Search API index for the view
filters to work.

1. Go to **Configuration → Search API → [index] → Fields**.
2. Confirm ``Promoted to front page`` is listed (machine name ``promote``,
   type ``Integer``).
3. If it is missing, click **Add fields**, find it under *Content*, add it,
   save, and re-index.

.. warning::

   You may see the message *"Your config-set contains manually added
   customizations."* after adding this field. This is harmless — it simply
   means the Solr config was modified through the UI rather than regenerated
   from scratch. The field will continue to work correctly.

----
Views
----

Featured Collections
~~~~~~~~~~~~~~~~~~~~

* **View machine name:** ``solr_search_collections``
* **Display:** a dedicated Block display within the collections view
* **Filter:** ``Content type = Digital Object Collection`` AND ``promote = 1``
* **Row style:** Content rendered in the ``digital_object_with_thumbnail_for_grid``
  display mode
* **Block visibility:** restricted to ``<front>``

Featured Works
~~~~~~~~~~~~~~

* **View machine name:** ``duplicate_of_collections``
* **Display:** Block display
* **Filter:** ``Content type = Digital Object`` AND ``promote = 1``
* **Row style:** Content rendered in the ``digital_object_with_thumbnail_for_grid``
  display mode
* **Block visibility:** restricted to ``<front>``

.. note::

   The ``custom_frontpage`` view (path ``/node``) also filters on
   ``promote = 1``. To prevent promoted Digital Objects from rendering there
   in full-node mode, that view has a filter excluding the ``digital_object``
   content type. If you see a promoted item appearing in an unexpected place,
   check that view's filter criteria.

--------------------------
Card / Masonry Rendering
--------------------------

Both sections share the same card and masonry layout used by the collection
membership grid.

Display mode
~~~~~~~~~~~~

The ``digital_object_with_thumbnail_for_grid`` display mode renders each
node using:

* **DS layout:** ``ds-1col``
* **Theme template:**
  ``web/themes/custom/tamu_theme/templates/node/ds-1col--node-digital-object-with-thumbnail-for-grid.html.twig``

  This template outputs a ``.tamu-card`` wrapper with a thumbnail image
  region and a title/body region. The thumbnail is produced by the
  Strawberry Field formatter, which calls the
  **tamu_custom_simple_card_thumbnail** metadata display Twig template
  (stored in Archipelago's metadata display system, not in the theme file
  system).

Thumbnail template
~~~~~~~~~~~~~~~~~~

Location (in Archipelago's metadata display UI, not on disk):

  **tamu_custom_simple_card_thumbnail**

This template builds a IIIF Image API URL from the node's JSON data and
renders a plain ``<img>`` tag. The image size is controlled by the
``iiif_size`` variable at the top of that template (e.g. ``pct:25`` for
25 % of the full image width).

Masonry CSS
~~~~~~~~~~~

The masonry layout is applied by
``web/themes/custom/tamu_theme/css/cards.css``.

The view's unformatted list template must wrap each row in a plain ``<div>``
for the CSS columns layout to work correctly in Firefox:

* **Featured Collections template:**
  ``templates/views/views-view-unformatted--solr-search-collections.html.twig``
* **Featured Works template:**
  ``templates/views/views-view-unformatted--duplicate-of-collections.html.twig``

Both templates have the same structure:

.. code-block:: twig

   <div class="tamu-cards-grid w-100">
     {% for row in rows %}
       <div>{{ row.content }}</div>
     {% endfor %}
   </div>

The ``tamu-cards-grid`` class triggers the CSS columns grid. Without the
inner ``<div>`` wrapper, Firefox renders all cards in a single row instead
of columns.

------------------
Adding a Featured Item
------------------

Collections
~~~~~~~~~~~

1. Edit the **Digital Object Collection** node.
2. In the **Advanced** sidebar, check **Featured on front page**.
3. Save.
4. Wait for Solr to re-index (or force it manually).
5. The collection will appear in the **Featured Collections** block on the
   front page.

Digital Objects (Works)
~~~~~~~~~~~~~~~~~~~~~~~

1. Edit the **Digital Object** node.
2. In the **Advanced** sidebar, check **Featured on front page**.
3. Save.
4. Wait for Solr to re-index (or force it manually).
5. The item will appear in the **Featured Works** block on the front page.

-----------------------
Removing a Featured Item
-----------------------

Uncheck **Featured on front page** on the node edit form and save.
The item will disappear from the front page after the next Solr index cycle.

---------------------
Relevant File Locations
---------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - File
     - Purpose
   * - ``tamu_theme/tamu_theme.theme``
     - Promote checkbox hooks and submit handler
   * - ``tamu_theme/css/cards.css``
     - Masonry grid and card image styles
   * - ``tamu_theme/templates/node/ds-1col--node-digital-object-with-thumbnail-for-grid.html.twig``
     - Card HTML structure
   * - ``tamu_theme/templates/views/views-view-unformatted--solr-search-collections.html.twig``
     - Featured Collections masonry wrapper
   * - ``tamu_theme/templates/views/views-view-unformatted--duplicate-of-collections.html.twig``
     - Featured Works masonry wrapper
   * - Archipelago metadata display: ``tamu_custom_simple_card_thumbnail``
     - IIIF thumbnail URL builder (managed in Drupal UI)
