================================
Changing Branding in Archipelago
================================

This guide explains how to update the site name, slogan, and logo in an Archipelago site using the Chiloé subtheme.

1. Change the Site Name and Slogan
==================================

1. Go to:

   ``Configuration > System > Basic site settings``

   Direct URL:
   ``/admin/config/system/site-information``

2. Update the following fields:

   - **Site name** — e.g., ``Texas A&M Digital Collections``
   - **Slogan** — Update or clear this field as needed.

3. Click **Save configuration**.

The updated site name will appear in the browser title and in the site header
(unless hidden in a later step).

2. Replace the Logo
===================

1. Go to:

   ``Appearance > Settings > Archipelago (Chiloé)``

   Direct URL:
   ``/admin/appearance/settings/archipelago_subtheme_chiloe``

2. Scroll to the **Logo image** section.

3. Uncheck:

   - ``Use the logo supplied by the theme``

4. Upload your institutional logo file.

   Recommended:
   - Use a transparent PNG or SVG.
   - Ensure adequate resolution for retina displays.

5. Click **Save configuration**.

3. (Optional) Hide the Site Name Text
=====================================

If your logo already includes the site name, you may wish to hide the text
version of the site name.

1. Go to:

   ``Structure > Block layout``

2. Ensure the active theme is:

   ``Archipelago (Chiloé)``

3. Locate the **Site branding** block in the **Top Header** region.

4. Click **Configure**.

5. Uncheck:

   - ``Site name``

6. Click **Save block**.

Clear Cache (If Changes Do Not Appear)
======================================

If updates are not visible immediately:

1. Go to:

   ``Configuration > Development > Performance``

2. Click:

   ``Clear all caches``

Notes
=====

- Logo sizing and spacing may be affected by theme CSS.
- For advanced branding changes (colors, typography, layout), consult your
  Archipelago subtheme documentation or a developer.
