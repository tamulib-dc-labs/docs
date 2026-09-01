.. _doi-policy:

===========
DOI Policy
===========

.. contents:: On this page
   :local:
   :depth: 2

Overview
========

This policy governs when and why the Digital Collections unit of the Texas
A&M University Libraries assigns Digital Object Identifiers (DOIs) to
content it hosts or stewards. It is intended for staff evaluating DOI
requests and for depositors who want to understand what qualifies.

A DOI is only as reliable as the organization that stands behind it. Every
practice in this document traces back to one requirement: **an
organization may only assign a DOI to content it has direct, ongoing
responsibility for, and every DOI must resolve to a stable landing page
that the organization controls** — never directly to the content itself.
This principle, and the reasoning behind it, is drawn from DataCite and
Crossref policy documentation and from how peer institutions have written
it into their own practice (see :ref:`doi-policies-reviewed`).

Scope
=====

This policy applies to DOI requests for content in three areas the
Digital Collections unit is responsible for:

#. Items in the **Institutional Repository** (OAKTrust)
#. Items in the **Data Repository**
#. Articles and issues in **OJS journals we host**

Requests for DOIs on content outside these three areas — including
externally hosted websites, personal or departmental sites, or platforms
the Libraries do not administer — fall outside this policy. See
:ref:`doi-stewardship` for why that boundary exists.

Registration Agency of Record
==============================

The Libraries maintain an active institutional membership with
**Crossref** and assign DOIs exclusively through that membership. Crossref
membership carries binding obligations — most importantly, that every DOI
resolve to a unique landing page carrying a full bibliographic citation,
that the DOI be displayed on that page, and that the Libraries remain
responsible for keeping the link current. Those obligations are the basis
for most of the requirements below.

.. _doi-why:

Why We Assign DOIs
===================

DOIs are not a formality attached to a finished item; they are a
commitment. Before a DOI is minted, the underlying reasoning is:

* **Persistent citation.** A DOI gives a work one stable, resolvable
  citation link for its lifetime, independent of any particular URL,
  server migration, or platform change.
* **Discoverability and reference linking.** Crossref DOIs plug content
  into the scholarly citation graph — reference lists, indexing services,
  and discovery layers rely on them to connect a citation to the work it
  points to.
* **Meeting funder and publisher requirements.** Data-sharing mandates
  and journal submission requirements increasingly expect a citable,
  persistent identifier, not just a URL.
* **Signaling institutional stewardship.** Minting a DOI is the Libraries
  telling the scholarly record, in effect, "we are responsible for this
  content and will keep the link working." That signal is only honest if
  it is backed by an actual persistence commitment — see
  :ref:`doi-stewardship`.

Because that last point is a commitment, not a technical trick, a DOI is
never minted purely because it was requested. It is minted because the
content lives somewhere the Libraries control and intend to maintain.

.. _doi-what:

What We Assign DOIs To
========================

Institutional Repository (OAKTrust)
------------------------------------

**What qualifies:** Research articles and reports, technical reports and
white papers, conference papers or proceedings, digital media objects,
and other scholarly or institutional outputs deposited in OAKTrust.

**Why OAKTrust content is eligible:** Content in OAKTrust is already
under direct institutional stewardship — it is deposited into
infrastructure the Libraries operate, with an existing item-level landing
page and a persistence commitment behind it. That satisfies the
stewardship precondition on its own. A DOI adds what OAKTrust's native
handle-based identifier does not provide by itself: inclusion in
Crossref's reference-linking graph, compatibility with citation managers
that expect a DOI rather than a handle, and discoverability through
services that index by DOI.

**Note:** not every item type deposited in OAKTrust automatically
qualifies. Some peer institutions (e.g., Georgetown) exclude theses and
dissertations from DOI minting even though they accept them into the
repository. Digital Collections should apply the same eligibility list
above rather than assuming everything in OAKTrust qualifies by default.

Data Repository
----------------

**What qualifies:** Research datasets curated and hosted under Digital
Collections stewardship, where the dataset's full metadata and access
conditions are known and documented.

**Why datasets get their own DOI:** A dataset is a distinct scholarly
output from the article that discusses it, and it needs its own citable,
trackable identifier so it can be attributed, cited, and reused
independently — this is the same reasoning that underlies FAIR data
principles and most funder data-sharing mandates.

**Duplicate-DOI check (required before minting):** Before assigning a
DOI to a dataset, confirm it has not already been assigned one by another
registration agency — for example, a dataset self-deposited by a
researcher into a Dataverse-based repository typically receives a DOI
automatically at deposit. If a DOI already exists for the object, do not
mint a second one for the same content. Instead, reference the existing
DOI as a related identifier in the new record (or decline to mint, if the
existing DOI already serves the citation need). Both DataCite and
Crossref policy explicitly prohibit assigning a DOI to content that
already carries one elsewhere.

OJS-Hosted Journals
---------------------

**What qualifies:** Articles and issues published in Open Journal Systems
(OJS) titles that the Libraries host and administer, such as the *Texas
Water Journal*.

**Why journal content is the clearest case for a DOI:** Journal articles
are the original use case Crossref was built around. Reference linking —
using Crossref DOIs to connect a citing article to the article it cites —
is a condition of Crossref membership, not an optional feature. For an
open-access journal in particular, a DOI is often what allows the journal
to appear in major indexing and discovery services (e.g., DOAJ-linked
tools, citation databases) at all. Because the Libraries directly operate
the OJS instance, the stewardship and landing-page requirements are met
by construction: each article already has a stable, Libraries-controlled
URL.

.. _doi-stewardship:

Stewardship Requirements
==========================

A DOI request should not be approved unless all of the following are
true:

#. **The Libraries have direct responsibility for the content** — it is
   deposited in OAKTrust, the Data Repository, or a Libraries-hosted OJS
   journal. Content hosted on infrastructure the Libraries do not control
   (a personal or departmental website, an external platform, etc.) does
   not qualify, regardless of how the request is framed, because the
   Libraries cannot guarantee the persistence commitment a DOI implies.
#. **The Libraries can update the content and its metadata** over time,
   not just at the moment of minting.
#. **The content is not already assigned a DOI elsewhere** (see the
   duplicate-DOI check above).
#. **A landing page exists and meets the requirements below.**

Landing Page Requirements
===========================

Every DOI must resolve to a landing page — never directly to a PDF,
dataset file, or other raw content. The landing page must:

* Display a full bibliographic citation for the item.
* Display the DOI itself as a resolvable link (``https://doi.org/...``).
* Provide a way to access the item (or, if access is restricted, explain
  the restriction — the metadata must still be openly available even
  when the content is not).
* Remain at a stable URL that Digital Collections controls, so that if
  the underlying platform changes, the landing page URL can be preserved
  or properly redirected rather than broken.

If content is later withdrawn, retracted, or removed, the landing page
should be converted to a tombstone page rather than deleted: it should
state that the item existed and explain why it is no longer available,
and the DOI's target URL should be updated to point to it. The DOI itself
is never deleted.

Request & Review Workflow
============================

#. Depositor or content owner submits a request through the Digital
   Collections request form, along with descriptive metadata (title,
   creator(s), date, abstract, hosting URL, responsible unit, resource
   type, and license).
#. Digital Collections reviews the request against the eligibility
   criteria in :ref:`doi-what` and the stewardship requirements in
   :ref:`doi-stewardship`.
#. If approved, the DOI is minted in Crossref and the metadata record is
   registered.
#. The DOI is returned to the depositor and added to the item's landing
   page.

Roles and Responsibilities
=============================

* **Digital Collections** evaluates requests, mints and registers DOIs,
  and is responsible for keeping DOI target URLs current if content
  moves within Libraries-controlled infrastructure.
* **Content owners / depositors** are responsible for providing accurate,
  complete metadata and for notifying Digital Collections if an item is
  moved, corrected, or withdrawn.
* **Digital Collections** (not the individual depositor) remains the
  Crossref-facing steward of record for every DOI minted under this
  policy, consistent with Crossref's requirement that only the
  registering organization may update a DOI's metadata and target URL.

.. _doi-policies-reviewed:

Policies Reviewed
====================

This policy was drafted after reviewing the following documentation from
our registration agency, DataCite (reviewed for general persistent-
identifier best practice, since much of its landing-page and stewardship
guidance mirrors Crossref's own), Crossref itself, and a sample of peer
institutional policies.

.. list-table::
   :header-rows: 1
   :widths: 18 42 40

   * - Source
     - Document
     - Relevant to this policy
   * - Crossref
     - `Current Membership Terms <https://www.crossref.org/membership/terms/>`_
     - Member obligations for persistent URLs, archive/defunct-DOI
       provisions
   * - Crossref
     - `Understanding Your Member Obligations <https://www.crossref.org/documentation/metadata-stewardship/understanding-your-member-obligations/>`_
     - Requirement for unique landing page URLs and legal rights to
       register content
   * - Crossref
     - `Display Guidelines <https://www.crossref.org/display-guidelines/>`_
     - DOI display and landing-page citation requirements
   * - Crossref
     - `Resource and Full-Text URLs <https://www.crossref.org/documentation/content-registration/administrative-metadata/resource-resolution-url/>`_
     - Landing page vs. direct-resolution guidance
   * - DataCite
     - `DOI Registration Policy <https://support.datacite.org/docs/doi-registration-policy>`_
     - Stewardship requirement; prohibition on duplicate DOIs
   * - DataCite
     - `Best Practices for DOI Registration <https://support.datacite.org/docs/best-practices-for-datacite-members>`_
     - Landing page requirement; tombstone-page handling
   * - DataCite
     - `Best Practices for DOI Landing Pages <https://support.datacite.org/docs/landing-pages>`_
     - Landing page vs. direct-content resolution
   * - Georgetown University Library
     - `DOI Minting <https://library.georgetown.edu/doi-minting>`_
     - Scoping DOI eligibility to items deposited in the institutional
       repository; exclusion of certain item types (e.g. theses)
   * - Murdoch University
     - `DOI Minting <https://libguides.murdoch.edu.au/RDM/DOIs>`_
     - Tying eligibility to the institutional repository as primary
       publication point
   * - University of Miami Libraries
     - `DOIs, Data Publication, Sharing and Preservation <https://guides.library.miami.edu/doi-data-publication>`_
     - Explicit depositor responsibility for perpetual access
   * - Queen's University Belfast
     - `Digital Object Identifier Policy <https://www.qub.ac.uk/directorates/InformationServices/TheLibrary/CustomerService/PoliciesandRegulations/DigitalObjectIdentifierPolicy>`_
     - Structure and governance of a short, formally owned DOI policy
   * - Texas A&M University–Corpus Christi
     - `DOIs at TAMU-CC Repository <https://guides.library.tamucc.edu/TAMU-CC_Repository/DOI>`_
     - Peer A&M System institution's eligibility and deposit requirements
   * - Texas A&M University Libraries
     - `Requesting a DOI <https://library.tamu.edu/digital-collections/dois.html>`_
     - Current internal service description, content eligibility list,
       and intake workflow this policy formalizes

Revision History
===================

.. list-table::
   :header-rows: 1
   :widths: 12 15 25 48

   * - Version
     - Date
     - Author
     - Summary
   * - 0.1
     - 2026-09-01
     - Digital Collections
     - Initial draft, compiled from DataCite and Crossref policy
       documentation and review of peer institutional DOI policies.

