==================
Adding OCR to ADOs
==================

After uploading a book, Archipelago runs OCR in the background to create extracted text for every book item. Although this is done automatically through hydroponics, this can take days to complete. This process can be sped up by running specifical tasks on specific ADOs. 

1. Go to :code:`/search-and-replace`.

2. In the search bar, type the name of the ADO you wish to run OCR for. Select the item from the search results. Be sure to select "trigger strawberry runners process/reprocess for archipelago digital objects content item". Then click "Apply to Selected Items".

3. On the confirmation page, check the "pager" and "text" boxes. Then click "Apply".

4. Go to :code:`/admin/config/system/queue-ui`.

5. Check the box "Strawberry Runners Process via Cron Queue Worker". Then click "Apply to selected items".

6. Once that runs, click "Strawberry Runners Process on Background Queue Worker". Then click "Apply to selected items".

7. Once all the queues are empty except "Archipelago Temporary File Composter Queue Worker", click that box. Select "Remove leases" in the Action drop down menu. Then click "Apply to selected items".

8. Select "Archipelago Temporary File Composter Queue Worker" again. Select "Clear" in the Action drop down menu. Then click "Apply to selected items".

9. Go to `rancher-devpre <https://rancher-devpre.library.tamu.edu/dashboard/home>`_.

10. Select :code:`dev-cluster`. Under :code:`Workloads`, select :code:`esmero-php`. Click the three dots at the right side of the row. Click execute shell.

11. Once inside the shell, enter :code:`cd /tmp`.

12. Enter :code:`du -sh`.

13. Enter :code:`ls -la`.

14. Enter :code:`rm -rf *`. This deletes all the completed tasks.