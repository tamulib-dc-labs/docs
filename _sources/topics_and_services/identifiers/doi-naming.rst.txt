================================
Conventions for Structuring DOIs
================================

This document outlines the DOI patterns currently in use at Texas A&M University Libraries. It also identifies patterns
that are reserved and should not be reused.

--------------------------------------------------------
DOIs for Open Journal Systems (OJS) Articles and Issues
--------------------------------------------------------

OJS generates DOIs using its built-in **Automatic DOI Assignment** feature.

Typical formats include:

- **Randomized pattern (current default):**
  Example: ``10.21423/jrs-v04n04pi``
  These DOIs use the journal’s slug plus a randomized suffix.

- **Semantic pattern (legacy):**
  Example: ``10.21423/bovine-vol1977no12p30-34``
  Some older OJS titles follow this more descriptive format.

**Important:**

Do not create DOIs that begin with a current OJS journal slug, since those are reserved.

A list of current slugs is maintained in the
`OJS Titles document list <https://docs.google.com/spreadsheets/d/1bxw5-ICUHBRvOPO-aeONZJmOIuYqYZ3AFMzWG6aiqIM/edit?usp=sharing>`_.

----------------------------------
DOIs for OAKTrust Repository Items
----------------------------------

OAKTrust DOIs follow the repository’s **handle-based pattern**.

For example:

- DOI: ``10.21423/oak/1969.1/197075``
- Corresponding handle:
  `https://hdl.handle.net/1969.1/197075 <https://hdl.handle.net/1969.1/197075>`_

This convention ensures a consistent mapping between DOIs and OAKTrust handles.

--------------------------
DOIs for Pressbooks Titles
--------------------------

Pressbooks DOIs follow a **randomized suffix pattern**.
The format uses the ``10.21423/odp.`` prefix, followed by a random string.
Each DOI resolves directly to a Pressbooks-hosted publication.

- Example DOI:
  ``https://doi.org/10.21423/odp.vmfn5541``

- Resolves to:
  `https://odp.library.tamu.edu/odp-guidelines/ <https://odp.library.tamu.edu/odp-guidelines/>`_

In order to ensure uniqueness, the :code:`opd.` namespace is reserved for Pressbooks and other applications in use by
the Open Publishing unit.

---------------------------------------------------
DOIs for Pending Publications or External Resources
---------------------------------------------------

Sometimes we will get a request for a DOI for a pending publication or where it is unclear where it will ultimately live.
In these situations, even if it will live in OAKTrust, we need a reserved pattern. For these, always lead with :code:`ppub-ext-`

For instance, we will use the pattern ``https://doi.org/10.21423/ppub-ext-swhrc-fG7kQ2`` with the last six being randomly generated.
**swhrc** is a slug for the requestor.
