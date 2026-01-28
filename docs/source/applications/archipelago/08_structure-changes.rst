==================================
Changing Structures on Archipelago
==================================

List of things to change from default Archipelago and how to change them.

-----------------------------------------
Removing Date Updated from Search Results
-----------------------------------------

1. Go to :code:`admin/structure/display-modes/view`. 

2. Select "Add view mode for Content". Name it "Digital Object with Creator and Date" and enable the view for Digital Object and Digital Object Collection. Click save.

3. Go to :code:`admin/structure/types/manage/digital_object/display`.

4. Select "Digital Object with Creator and Date". Scroll to the bottom of the page and change "One column layout" to "Two column". Click save to reload the page with updated layout options.

5. Drag "Title" to "Top".

6. Drag "Dah woozh" to "First". For Format, select "Strawberry Field Formatter for Custom Metadata Templates". Click the gear. 

    a. For "Choose your metadata template", select "Multiple Thumbnails via IIIF and FontAwesome (10)".

    b. For the URL, type "http://schema.org".

    c. For the public facing label, enter "Thumbnail". Click update.

7. Drag "Search result excerpt" to "First" underneath "Dah woozh".

8. Drag "Strawberry (Descriptive Metadata Source)" to "Second". For Format, select "Strawberry Field Formatter for Custom Metadata Templates". Click the gear.

    a. Choose "Object Metadata Abstract for Search Results (8)" for metadata template.

    b. For the URL, type "http://schema.org".

    c. For the public facing label, enter "Descriptive Metadata". Click update. Scroll to the bottom of the page and click save.

9. Go to "Browse Digital Objects". Click "edit view" on the search results.

10. Under Format > Show, click "Settings."

11. Change view mode for datasource Content, bundle Digital Object from "Digital Object with thumbnail and abstract" to "Digital Object with Creator and Date".

12. Change view mode for datasource Content, bundle Digital Object Collection from "Digital Object with thumbnail and abstract" to "Digital Object with Creator and Date".

13. Click Apply. Then click save.
