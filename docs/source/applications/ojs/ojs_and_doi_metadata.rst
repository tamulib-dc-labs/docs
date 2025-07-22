====================
OJS and DOI Metadata
====================

---------------------------------------
Updating Metadata for Existing Articles
---------------------------------------

* Enable and configure required plugins
* Find an existing aricle in the OJS instance.
* Unpublish the article -- temporarily.
* Add metadata.
* Republish.

----------
References
----------

References are an option in OJS. References collect a submission's references in a separate field.

References highlight an articles provenance and where it sits in the scholarly map. References give researchers and other users of
Crossref metadata a vital data point through which to find your content, which in turn increases the chances of your content being
read and used.

You can configure by going to :code:`Workflow > Submission > Metadata > References` and clicking the check box next to
:code:`Enable references metadata`.  You can also use radio buttons to set who provides the references.

Once references are enabled, you can enter each reference on a line to produce a reference list during the publication
process.

The :code:`Crossref Reference Linking Plugin` enables automatic extraction of DOIs from the reference list. The plugin
uses the Crossref API to check against your plain text references provided to locate any possible DOI matches.
It also allows the display of reference lists on the article landing page.

---------
Abstracts
---------

Abstracts are added automatically by providing an abstract at :code:`Publication > Title & Abstract`.

---------------
Author Metadata
---------------

Author Metadata can be edited in :code:`Publication > Contributors` section using the :code:`Edit` button under each author's name in
the initial submission or from the submissions section.

In edit, you can add an ORCID iD and affiliation (where they are employed). Adding this information increases the likelyhood that 
the article is found by applications used to measure the research output of the university.

If you want to add ROR IDs, you need the ROR Plugin which collects and displays ROR IDs for author affiliations.