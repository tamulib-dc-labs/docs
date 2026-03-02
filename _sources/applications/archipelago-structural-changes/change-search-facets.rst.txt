=================================
Changing fields for search facets
=================================

1. Go to :code:`/admin/structure/strawberry_keynameprovider`.

2. In the table, locate "Agents from LoD and Local". Click edit.

3. In the text box "One or more comma separated valid JMESPaths", add :code:`creator, contributor`. Delete all subject fields (such as :code:`subject_lcnaf_personal_names[].label, subjects_local_personal_names, subject_lcnaf_corporate_names[].label, subject_lcnaf_personal_names[].label`). Click save.

4. In the table, locate "Subject Labels". Click edit.

5. In the text box "One or more comma separated valid JMESPaths", add :code:`subjects_local`. Click save.

6. Go to :code:`/admin/config/search/search-api/index/default_solr_index`. Click "Queue all items for reindexing". Then click "Index now".