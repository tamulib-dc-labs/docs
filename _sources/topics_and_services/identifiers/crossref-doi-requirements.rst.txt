======================================
General Requirements for Crossref DOIs
======================================

This document outlines the general requirements and expectations that apply to any DOI registered
through Crossref, regardless of content type or application. It is meant to complement
:doc:`doi-naming` (which covers our naming conventions) and :doc:`minting_a_doi` (which covers
Crossref workflows) by focusing on the underlying *obligations* we take on as a DOI registrant.

-----------
Persistence
-----------

A DOI is a promise that the identifier will always resolve, even if the underlying content moves.

- The DOI itself must **never change** once assigned, even if the title, URL, or hosting platform
  changes.
- If the content's location changes, we are responsible for updating the DOI's target URL in
  Crossref so the DOI continues to resolve correctly.
- DOIs should not be deleted or reassigned to different content.

.. todo::

   Add our internal process/contact for updating a DOI's target URL when content moves.

----------
Permanence
----------

Once minted and deposited, a DOI is intended to be a permanent identifier for that specific work.

- Do not mint a DOI for content that is not intended to be retained long-term.
- Do not reuse a DOI for a different or substantially revised work; if a new version is needed,
  consider minting a new DOI and linking the two (see Crossref's guidance on relationships between
  DOIs).
- Withdrawn or retracted content should still resolve, but with updated metadata reflecting its
  status (see the Pending Publications withdrawal guidance in :doc:`minting_a_doi`).

----------
Uniqueness
----------

- Each DOI must be unique and must not duplicate a DOI already registered by us or another
  Crossref member.
- Follow the naming conventions in :doc:`doi-naming` to avoid collisions with reserved patterns
  (e.g., OJS journal slugs, the ``odp.`` namespace, ``ppub-ext-`` prefixes).

-------------------------
Minimum Required Metadata
-------------------------

Crossref requires a baseline level of metadata at the time of deposit. At minimum, this generally
includes:

- Title
- Contributor(s)/author(s)
- A resolvable URL (the "resource" the DOI points to)
- Publication or acceptance date, as applicable

.. todo::

   Confirm the minimum metadata set per work type (journal article, book, dataset, pending
   publication, etc.) and link to Crossref's schema documentation for each.

------------------------------
Responsibility for Maintenance
------------------------------

Registering a DOI with Crossref is an ongoing commitment, not a one-time action.

- We are responsible for keeping metadata accurate and up to date.
- We are responsible for maintaining the resolution target for the life of the DOI.

For these reasons, we generally do not create DOIs for any platforms where we do not have control.  Instead, where
permissions allow, we make a duplicate of that resource (post-print) and preserve it in OAKTrust or another platform
and point the DOI at that resource.

.. todo::

   Add notes on who owns this responsibility internally (e.g., unit/role) and how DOIs are
   audited over time.

----------
References
----------

- `Crossref: DOI Display Guidelines <https://www.crossref.org/documentation/register-maintain-records/creating-and-managing-dois/doi-display-guidelines/>`_
- `Crossref: Schema Library <https://www.crossref.org/documentation/schema-library/>`_
