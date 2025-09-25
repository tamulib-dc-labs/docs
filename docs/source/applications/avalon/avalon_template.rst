===========================
Template for Avalon Batch Imports
===========================

Here is a template used for Avalon Batch Imports. All columns are verified to be compatible with Avalon 7.8.

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1QcxBWxmplvGvT3OgbTsCV0Fc9dHSRHgMwp9CYABo4aE/edit?gid=0#gid=0" height="400" width="1200" frameborder="0" allowfullscreen></iframe>


**Things to consider**

* If you are uploading videos, go to the "captions" page. If you are uploading audio only, go to the "transcript" page.
* Technically this works with a xlsx spreadsheet, but a csv prevents numerical fields from autocorrecting.
* Title and File are the only required fields.
* Creator, Contributor, Genre, Language, Subject, Geographic Subject, Temporal Subject, Note Type, and Note are all repeatable.
* Note Type must be immediately followed by Note.
* Caption File must be immediate followed by Caption Label.
* Transcript File must be immediate followed by Transcript Label.
* Language should be a three-letter code (ie "eng").
* Offset must follow HH:MM:SS.sss format. Make sure it is in plain text.
* Date Issued must follow this format:
    * YYYY-MM-DD
    * YYYY-MM
    * YYYY
    * YYYX (if decade is known but year is not)
    * YYYY-MM-DD/YYYY-MM-DD (if range)
    * unknown/unknown

**Ways this differs from official documentation**
* Unknown if Date Created works
* "Topical Subject" does not work. Use "Subject" instead.
* Do not use the term "Main Contributor". The field is "Creator".
* "Statement of Responsibility" seems to not do anything.
* Do not use "Transcript File Label". The field is "Transcript Label".
* You do not need to select files to upload from a Dropbox. You do not need Filezilla or any other Secure File Transfer Protocol (SFTP) client. Putting them on the cifs drive is enough.
* If there is an error during ingest, do not reupload the spreadsheet after making changes. It will reupload all files, giving you duplicates. Create a new spreadsheet for only the files that failed. 