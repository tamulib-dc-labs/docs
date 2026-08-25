sistent identifiers handle ark doi · RST
.. _persistent-identifiers:

===============================================
Persistent Identifiers: Handle vs. ARK vs. DOI
===============================================

A guide for choosing the right identifier scheme for digital collections and
repository content.

Why this matters
=================

A persistent identifier (PID) is a long-lasting reference to a digital
object. It is a link that keeps working even if the object's URL changes.
Handles, ARKs, and DOIs are the three schemes you'll run into most often in
library and archives work. They solve the same basic problem (link rot) but
differ in who controls them, what they cost, what they imply about the
resource, and what audience expects them.

Picking the wrong one isn't fatal -- you can usually mint more than one
identifier for the same object -- but it's worth being deliberate, since it
affects citation practice, discoverability, and long-term maintenance
overhead.

The short version
==================

.. list-table::
   :header-rows: 1
   :widths: 18 27 27 28

   * -
     - Handle
     - ARK
     - DOI
   * - Full name
     - Handle System
     - Archival Resource Key
     - Digital Object Identifier
   * - Governing body
     - Corporation for National Research Initiatives (CNRI) / DONA Foundation
     - California Digital Library (originally), now community-governed via the ARK Alliance
     - International DOI Foundation, via registration agencies (Crossref, DataCite, etc.)
   * - Typical cost
     - Free if self-hosting a resolver; fees if using a Handle prefix service
     - Free -- no central registry fees, though some assigners charge internally
     - Registration fees per DOI or per year, paid to a registration agency
   * - Who mints them
     - Anyone running Handle server software with a prefix
     - Any organization with a Name Assigning Authority Number (NAAN)
     - Only registration-agency members (publishers, universities, data repositories, etc.)
   * - Resolution
     - ``hdl.handle.net`` global resolver, or local resolver
     - ``n2t.net`` (Name-to-Thing) global resolver, or local resolver
     - ``doi.org`` global resolver
   * - Implies scholarly citation?
     - Not inherently
     - Not inherently
     - Yes -- DOIs carry strong expectations of formal, citable, versioned scholarly output
   * - Common in
     - Institutional repositories (DSpace, Fedora, etc.)
     - Archives, special collections, digital library objects, cultural heritage
     - Journal articles, datasets, technical reports, anything meant to be formally cited
   * - Metadata requirement
     - Minimal / none required by the system itself
     - Minimal / none required
     - Required -- registration agencies mandate a metadata record (title, creator, publication date, etc.)

What each one actually is
==========================

Handle
------

A Handle is simply ``prefix/suffix`` (e.g., ``2346/12345``) that resolves
through the Handle System to a URL. It's infrastructure-level and
deliberately unopinionated about what kind of resource it points to. DSpace
repositories mint Handles by default for every item and collection, which
is why they're common for institutional repository content: theses,
dissertations, technical reports, and other repository deposits.

Handles are a fine default when you need *a* stable identifier and don't
have a specific reason to reach for something more specialized. They don't
carry any implicit promise about formal citability or scholarly publication
status. In other word,s they're plumbing, not a statement.

ARK
---

An ARK looks like ``ark:/12345/x6f78d`` and is designed specifically for
archival and cultural heritage contexts. Its design goals are notable: an
ARK is meant to resolve not just to the object but optionally to a
**commitment statement** (what the institution promises about the object's
persistence) and **metadata** (via appending ``?`` or ``??`` to the
identifier and a convention baked into the spec itself). That makes ARKs a
natural fit for digital collections, digitized manuscripts, maps,
photographs, and other special-collections material where you want the
identifier itself to carry a bit of self-description.

ARKs are free to mint (you just need a NAAN, which is free to request),
which has made them popular with archives and libraries that want
persistent IDs without ongoing registration fees per object. This is a
meaningful consideration at digitization scale, where you might be minting
thousands of identifiers.

DOI
---

A DOI looks like ``10.xxxx/yyyy`` and is built on top of the Handle System
technically, but the *social contract* around DOIs is much stronger.
Registering a DOI means committing to maintain a metadata record with a
registration agency (Crossref for scholarly literature, DataCite for
datasets and repository content, among others), and the DOI ecosystem
assumes the object is a formally published, citable unit of scholarship.
Getting a DOI typically costs money which can be per-DOI or membership fees through
the registration agency.

Because of that infrastructure and expectation, DOIs are the right call
when the object needs to be **formally citable**: journal articles,
datasets tied to a publication, technical reports meant to be cited in the
scholarly record.

Decision guide
===============

Ask, in order:

#. **Does this need to be formally, scholarly citable? The kind of thing
   someone will put in a reference list?**
   → **DOI.** (This is really the deciding question. If yes, stop here.)

#. **Is this a digitized cultural heritage object: a manuscript, map,
   photograph, or similar where you want the identifier to also carry a
   commitment/metadata statement, and you're minting many of them without
   per-object fees?**
   → **ARK.**

#. **Is this a repository deposit (thesis, dissertation, report, dataset)
   where you just need a stable, resolvable link and your platform already
   mints these by default?**
   → **Handle.**

#. **Not sure, or it could go either way?**
   → Default to whatever your platform issues natively (e.g., DSpace →
   Handle), and layer a DOI on top later if the object turns out to need
   formal citation. Identifiers aren't mutually exclusive -- the same
   object can have a Handle *and* a DOI.

A few practical notes
=======================

.. note::

   You can have more than one. It's common for an object to have a Handle
   (from the repository platform) and a DOI (for formal citation)
   simultaneously. The DOI becomes the "citable" identifier; the Handle
   remains the resolvable link within the repository ecosystem.

.. warning::

   DOIs require upkeep. Once minted, DOI metadata has to stay accurate at
   the registration agency (title changes, corrections, etc.), and there's
   an ongoing cost relationship with the registration agency. Don't mint a
   DOI for something you don't intend to maintain that record for.

- **ARKs' optional inflections (** ``?`` **,** ``??`` **) are a real
  feature, not decoration.** If you're choosing ARKs partly for their
  self-description properties, actually implement resolver support for the
  commitment and metadata suffixes -- otherwise you're just using an ARK as
  a plain identifier and losing the reason you picked it.
- **None of these prevent link rot on their own.** They only work if
  someone maintains the resolver mapping. An identifier scheme is a
  governance commitment, not a technical guarantee.

.. todo::

   Add institution-specific policy here before publishing: who has minting
   authority, which system is authoritative for which content type, and
   DOI registration agency / account details.

.. warning::

    DOIs are persistent identifiers (PIDs), which means that they are intended
    to be a permanent means of identifying and accessing a particular resource.
    Because of this, a DOI cannot be deleted and if it no longer resolves must
    point at a Tombstone page that explains why the resource is no longer available.
    If this happens, refer to the `DataCite Best Practices <https://support.datacite.org/docs/tombstone-pages>`_.
