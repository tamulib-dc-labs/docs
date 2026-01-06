===================
Minting DOIs in OJS
===================

-----
About
-----

This document describes how to mint DOIs in OJS. If you are looking for information about
minting DOIs in Crossref in a another application, see :doc:`../identifiers/minting_a_doi`.

------------------
Requesting an ISSN
------------------

Before you setup DOI mintning, you should have acquired an ISSN. To request an ISSN, see 
:doc:`applying_for_issns`.

Once you have been provisionally awarded an ISSN, add it to Publishing Details.

.. image:: ../../_static/images/publishing-details.png
    :alt: An Image Showing OJS Publishing Details

-----------------
Initial DOI Setup
-----------------

To setup DOIs intially, go to :code:`Distribution - DOIS - Setup`. From here, check allow. For the DOI Prefix, always use :code:`10.21423`.
Consult with the journal team about :code:`Automatic DOI Assignment`. If they intend to add the DOI to the PDF, :code:`Upon reaching the copyediting stage`
should be chosen.  The DOI Format should always be :code:`Default`.

.. image:: ../../_static/images/doi-setup.png
    :alt: An Image Showing OJS DOI Setup

Since we use Crossref and personal email accounts for authentication, you must set your user name like so: :code:`email@example.com/role`.:align:

You can find your role in the Crossref Admin portal.

.. image:: ../../_static/images/crossref-role.png
    :alt: An Image Showing How Roles are Displayed in the Crossref Admin Portal

Following this pattern, I would set my username to :code:`mark.baggett@tamu.edu/texu`.

----------------
DOI Registration
----------------

To setup DOI registration, you need to install the :code:`Crossref Manager Plugin`. This will make the
:code:`DOIs Registration` page appear. Set up details with you email address, a name for the registrant, and Crossref Account Details.

.. image:: ../../_static/images/doi-registration.png
    :alt: An Image Showing OJS DOI Registration

-----------------
Addressing Errors
-----------------

If an article appears with an error on the DOI page, you can click it and resubmit the request to Crossref. If it fails,
the :code:`View Error` screen will explain why.
