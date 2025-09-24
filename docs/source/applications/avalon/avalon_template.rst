===========================
Template for Avalon Batch Imports
===========================

Here is a template used for Avalon Batch Imports.

.. raw:: html

    <iframe src="https://docs.google.com/spreadsheets/d/1QcxBWxmplvGvT3OgbTsCV0Fc9dHSRHgMwp9CYABo4aE/edit?gid=0#gid=0" height="400" width="1200" frameborder="0" allowfullscreen></iframe>


**Things to consider**

* Technically this works with a xlsx spreadsheet, but a csv helps prevent numerical fields from autocorrecting.
* Creator, Contributor, Genre, Subject, Geographic Subject, Temporal Subject, Note Type, and Note are all repeatable.
* Note Type must be immediately followed by Note.
* Caption and Transcript should not both be used. If you are uploading videos, go to the "captions" page. If you are uploading audio only, go to the "transcript" page.
* Caption File must be immediate followed by Caption Label.
* Transcript File must be immediate followed by Transcript Label.
* Language should be a three-letter code (ie "eng").
* Caption Language should be a two-letter code (ie "en").
* Offset must follow HH:MM:SS.sss format. Make sure it is in plain text.
* Date must follow this format:
    * YYYY-MM-DD
    * YYYY-MM
    * YYYY
    * YYYX (if decade is known but year is not)
    * YYYY-MM-DD/YYYY-MM-DD (if range)
    * unknown/unknown