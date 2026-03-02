=================================
Changing colors to fit TAMU brand
=================================

----------------------------------
Changing colors across entire site
----------------------------------

1. Go to :code:`/admin/appearance/settings/archipelago_subtheme_chiloe`.

2. Click "Barrio Color Scheme Settings" dropdown.

3. Reset base colors
    a. Set Primary base color to :code:`#500000`.
    b. Set Secondary base color to :code:`#a7a7a7`.
    c. Set Tertiary base color to :code:`#500000`.
    d. Set Quarternary base color to :code:`#a7a7a7`.

4. Set H1, H2, H3, and Footer Background colors to "Primary color".

5. Click "Save configuration".


-------------------------------
Changing colors on audio player
-------------------------------

1. Go to :code:`/admin/structure/types/manage/digital_object/display/digital_object_with_a_v_player`.

2. Scroll down to "Erdbeere" and click the gear. Scroll to the "Advanced: a JSON with Wave Surfer Options." text box.

3. Set the following:

.. code:: json

    "waveColor": "rgb(115, 47, 47)",
    "progressColor": "#3c001c",
    "cursorColor": "#500000",

4. Click "Update". Then click "Save".