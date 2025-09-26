====================
Reporting 500 Errors
====================

Often times, users report getting 500 errors when visiting OAKTrust. This is more common in a browser like Chrome than
in Firefox.

Without accurate details of what's occurring, these reports are treated as anecdotal and don't receive proper
investigation. For this reason, we should ask users to submit HTTP archives (HARs).  HARs capture everything happening
between the users browser and the website's server. Their contents show what caused the 500 response.

---------------
Capturing a HAR
---------------

Chrome
======

1. Open Chrome.
2. Right-click anywhere in the browser window and select :code:`Inspect`.
3. Go to the :code:`Network` tab in that little window that pops up.
4. Check the box next to :code:`Preserve log`.
5. In the address bar, type: https://oaktrust.library.tamu.edu and press Enter.
6. In the Network panel, click the :code:`Export HAR button` (a small download icon near “Preserve log”).
7. Ask the user to email the file or share it via Google Drive.

-----------------
Reporting the 500
-----------------

1. Open a new ticket.
2. Add the Har to the `OAKTrust HARs <https://drive.google.com/drive/folders/1A22t10lQbYxRuW8foeAIGoNTA_kx95Cy?usp=drive_link>`_ directory.
3. Submit a link to the HAR in Google Drive in the body of your ticket.
