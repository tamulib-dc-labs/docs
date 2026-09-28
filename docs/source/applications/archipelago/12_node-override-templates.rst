==============================================
Overriding a Single Page with a Node Template
==============================================

Some static pages on TAMU Digital Collections, such as **About Our Digital
Collections** or **Statement of Use**, are written directly in Twig rather than
in the Drupal WYSIWYG editor. This gives us full control over the markup, lets
us reuse the theme's hero, card, and section styles, and keeps page content
under version control in the
`tamu-archipelago-theme <https://github.com/tamulib-dc-labs/tamu-archipelago-theme>`_
repository.

This page explains how the override works and how to add one for a new page.

------------
How It Works
------------

When Drupal renders a node, it builds a list of *template suggestions* and uses
the most specific template file it can find in the active theme. Drupal core
provides several suggestions on its own, and the TAMU theme adds one more in
``web/themes/custom/tamu_theme/tamu_theme.theme``:

.. code-block:: php

   /**
    * Add node ID to theme suggestions so node--TYPE--NID.html.twig templates work.
    */
   function tamu_theme_theme_suggestions_node_alter(array &$suggestions, array $variables) {
     $node = $variables['elements']['#node'];
     $suggestions[] = 'node__' . $node->bundle() . '__' . $node->id();
   }

This hook runs for **every** node, so no additional PHP is needed when you add a
new page. You only need to add a template file with the right name.

For a Basic page with node ID ``121197`` viewed in the ``full`` view mode,
Drupal looks for templates in roughly this order, from most to least specific:

.. code-block:: text

   node--page--121197.html.twig     <- added by tamu_theme
   node--121197--full.html.twig
   node--121197.html.twig
   node--page--full.html.twig
   node--page.html.twig             <- generic Basic page template
   node--full.html.twig
   node.html.twig

If no node-specific template exists, the page falls back to
``node--page.html.twig``, which renders the node's title in a hero and the
WYSIWYG ``body`` field underneath.

---------------
Naming the File
---------------

Template names follow this pattern:

.. code-block:: text

   node--<bundle>--<node id>.html.twig

* ``<bundle>`` is the content type's machine name with underscores replaced by
  hyphens. For Basic pages this is ``page``. A ``digital_object`` would be
  ``digital-object``.
* ``<node id>`` is the numeric node ID, **not** the UUID.
* The extension must be ``.html.twig``. A file named ``.twig.html`` will be
  silently ignored.

Existing examples in ``templates/node/``:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - File
     - Page
   * - ``node--page--28534.html.twig``
     - About Our Digital Collections
   * - ``node--page--121197.html.twig``
     - Statement of Use

-----------------
Adding a New Page
-----------------

1. **Create the node.** Go to ``/node/add/page``, give it a title, and save
   it. The body can be left empty since the template will supply the content.
   Make sure it is published.

2. **Find the node ID.** Hover over or click the **Edit** tab. The URL will be
   ``/node/<nid>/edit``. Use this number, not the UUID.

3. **Create the template.** In the theme repository, copy an existing override
   as a starting point:

   .. code-block:: bash

      cp templates/node/node--page--121197.html.twig templates/node/node--page--<nid>.html.twig

4. **Write the content.** Edit the new file. See `Page Structure`_ below for the
   building blocks available.

5. **Deploy the theme** to ``web/themes/custom/tamu_theme`` the same way as any
   other theme change.

6. **Clear the cache.** Drupal caches the template registry, so a new template
   will not be picked up until caches are rebuilt:

   .. code-block:: bash

      drush cr

7. **Optionally add a URL alias** so the page has a friendly path. See
   :doc:`998_add_url_alias`.

--------------
Page Structure
--------------

Override templates use the same wrapper and classes so every static page looks
consistent. The styles live in ``css/collection-hero.css`` and ``css/slim.css``
and are loaded on every page, so no library needs to be attached.

.. code-block:: html+jinja

   <article{{ attributes }}>

     {# ── Hero ── #}
     <div class="tamu-collection-hero" style="background-image: url('<IIIF image URL>'); background-size: cover; background-position: center;">
       <div class="tamu-collection-hero__overlay">
         <div class="container">
           <h1 class="tamu-collection-hero__title">Page Title</h1>
         </div>
       </div>
     </div>

     {# ── Body ── #}
     <div class="container tamu-about-body">
       {{ title_suffix }}

       <div class="tamu-about-body__intro">
         <h2>Short summary heading</h2>
         <p>Introductory paragraph.</p>
       </div>

       <section class="tamu-about-body__section">
         <h2>Section Heading</h2>
         <h3>Subheading</h3>
         <p>Body text.</p>
       </section>

       <hr class="tamu-about-body__divider">

       <section class="tamu-about-body__section">
         ...
       </section>
     </div>

   </article>

Available building blocks:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Class
     - Use
   * - ``tamu-collection-hero``
     - Full-width banner image with the page title. Any IIIF Image API URL
       works as the background.
   * - ``tamu-about-body``
     - Outer container for the page body.
   * - ``tamu-about-body__intro``
     - Large lead-in heading and paragraph at the top of the page.
   * - ``tamu-about-body__section``
     - A content section. Styles its ``h2``, ``h3``, ``p``, and ``a`` elements.
   * - ``tamu-about-body__divider``
     - Maroon rule placed between sections.
   * - ``tamu-about-body__cite``
     - Maroon-bordered callout box, used for citation examples and contact
       details.
   * - ``tamu-cards-grid`` / ``tamu-card``
     - Grid of linked image cards, used for collection highlights. See
       ``node--page--28534.html.twig`` for an example.

A few tips:

* Keep ``{{ attributes }}`` on the ``<article>`` and ``{{ title_suffix }}`` in
  the body. Drupal uses them for contextual links and other admin tools.
* Escape ampersands in text as ``&amp;``.
* Theme images can be referenced as
  ``/themes/custom/tamu_theme/images/<file>``.

-------------------
Things to Watch For
-------------------

**The template ignores the node's body field.** Once an override exists,
editing the page in Drupal changes nothing except the title in admin listings.
All content changes must be made in the template and deployed.

**The template applies to every view mode.** The
``node--<bundle>--<nid>`` suggestion does not include the view mode, so if the
node ever appears as a teaser or card in a view, the full page template will
render there too. If that becomes a problem, wrap the template in
``{% if view_mode == 'full' %}`` or name the file
``node--<nid>--full.html.twig`` instead.

**The bundle must match.** If the template has no effect, confirm the node's
content type. A ``node--page--<nid>`` template will never match a node that is
not a Basic page.

**Confirming which template is used.** Turn on Twig debugging at
``/admin/config/development/settings`` (Drupal 10.1+), clear caches, and view
the page source. HTML comments list every suggestion Drupal considered and mark
the file it chose with ``x``. Turn debugging off again when you are done.

----------------------------------
How to Update things on the Server
----------------------------------

You need to get the file to the server and then clear cache for your change to appear.  To do this:

1. Run ``kubectl -n archipelago get pods`` to find your pod name.
2. Copy your local file to the theme: ``kubectl cp node--page--121197.html.twig esmero-php-<pod-id>:/var/www/html/web/themes/custom/tamu_theme/templates/node -n archipelago``
3. Clear drupal cache: ``drush cc`` or ``Devel > Cache clear``

.. note::

  When you clear cache that way, you delete **ALL** cache.  A safer way is to: ``drush php:eval "\Drupal::service('twig')->invalidate();" && drush cache:tags node:121197 && drush cache:clear theme-registry``
