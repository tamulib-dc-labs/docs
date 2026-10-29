==============================
Products and Product Ownership
==============================

-----
About
-----

The **Product Owner** operates at the center of the product ecosystem, ensuring that stakeholder needs are understood,
customer input is effectively translated, and development efforts are aligned with strategic objectives. They hold decision
authority while maintaining continuous collaboration across institutional and technical boundaries.

This document lays out product ownership for products in the Digital Collections unit.  It describes what is expected of
the product owner, whom they represent, and what is necessary to successfully be a product owner for a service or application.

If you want to weigh in on the direction of a product, contact its Product Owner. To propose a new digital project, start with
the DPMT process rather than contacting a Product Owner directly. See :doc:`08_partners_and_stakeholders` for the full list
of internal and external groups we work with.

Terminology
===========

* **Product**: A service, application, or platform that Digital Collections operates, develops, or relies on to deliver
  its work. A product has a Product Owner, at least one instance, and stakeholders.

* **Stakeholder**: Any individual or group impacted by the product, directly or indirectly. This includes end users, institutional
  units, and external parties whose work or outcomes are affected.

* **Customer**: A subset of stakeholders who are actively engaged in the product development process. Customers interact directly
  with the Product Owner, contribute requirements, provide feedback, and influence product direction.

* **Product Owner**: The single person accountable for a product's direction, priorities, and health. A product has exactly
  one Product Owner at a time, even when many people contribute to it.

Roles of Product Owner
======================

* **Product Stewardship (Governance & Long-Term Planning)**: Ensure the long-term health, sustainability, and strategic alignment
  of the product. Establish and maintain governance structures, guide long-term product direction, and ensure continuity across
  development cycles. Balance immediate delivery needs with future viability, including technical sustainability, institutional
  alignment, and evolving stakeholder needs.
* **Stakeholder Management**: Maintain awareness of all stakeholder groups, ensure clear stakeholder identification and
  definition, and understand their needs and their impact on the product, and the product's impact on each stakeholder group.
* **Requirements Gathering**: Actively engage customers to identify needs, anticipate requirements, and refine problem spaces.
* **Backlog Curation**: Own and prioritize the product backlog in collaboration with the development team, balancing competing
  priorities while maintaining a coherent product vision.
* **Champion / Approval Authority**: Serve as the final decision-maker for product direction, scope, and acceptance of work.
  Act as the primary advocate for the product, ensuring it receives appropriate development time, resources, and organizational
  support. Represent the product in prioritization discussions, defend its value, and ensure its needs are clearly articulated.
* **Sprint Participation**: Engage in sprint planning, reviews, and ongoing team interaction to ensure alignment and delivery quality.

Decision Authority
==================

The Product Owner is the final decision-maker for the following, in consultation with customers and the development team:

* What gets built, fixed, or deferred, and in what order
* Whether completed work is accepted
* Whether the product is upgraded, migrated, or retired
* Who counts as a customer and how their feedback is gathered

Decisions that cross product boundaries (for example, a change in Fedora that affects CAP, SAGE, and Avalon) should be raised
with every affected Product Owner and, where they cannot agree, with the Director of Digital Collections. See
:doc:`03_people`.

What Every Product Owner Should Be Able to Do
=============================================

Regardless of the product, a Product Owner should be able to:

* Explain what the product does, who uses it, and why the Libraries run it
* Name the product's dependencies (see "Supports" and "Supported By" below) and what breaks if one of them goes down
* Describe each instance (Dev, Pre, Prod) and how a change moves between them
* Find the code, configuration, and documentation for the product
* Identify the upstream community, if there is one, and how to reach it
* Keep a current list of customers and known stakeholders
* Maintain a backlog, even if that backlog is short
* Say what the plan is for the product's future, including when it will be retired

Becoming or Handing Off a Product Owner
=======================================

When product ownership changes, the outgoing and incoming owners should work through the following together before the change
is recorded on this page:

#. Review the product's entry on this page and update anything that is out of date.
#. Walk through every instance, including how to log in, where logs live, and how to deploy.
#. Transfer access: repositories, upstream community accounts and mailing lists or Slack channels, and any vendor or
   consortium contacts.
#. Introduce the new owner to customers and to Technology Services contacts, where applicable.
#. Hand over the backlog, open issues, and any commitments made to stakeholders.
#. Update the "Current Product Owner" line and notify the team.

How to Read a Product Entry
===========================

Each product below uses the same fields where they apply.

* **Current Product Owner**: The person accountable for the product.
* **Repository**: Where the code or configuration lives.
* **Development Support from Technology Services**: Whether Technology Services (TS) staff develop the product.

  * *Yes*: TS provides development support.
  * *Yes (Third Party — Contribute)*: TS supports a third-party product and contributes changes back to it.
  * *No (Third Party — Consume)*: The product is third-party and we use it as released.
  * *No (DevOps and Deployment only)*: TS deploys and hosts the product but does not develop it.
  * *No (Not listed as a Technology Services product)*: TS does not formally list or support the product.

* **Campus Category**: *Common* products are widely used software that other institutions also run. *Unique* products are
  built at Texas A&M for needs specific to us.
* **Dependencies**: Each product has a Dependencies section with two lines. **Depends on** (Supported By) lists the products
  this product needs in order to work. **Used by** (Supports) lists the products that need this one. Before changing,
  upgrading, or retiring a product, check its "Used by" line and talk to those Product Owners.
* **Instances and Clusters**: The environments in which the product runs.
* **PODS and Containers**: The Kubernetes pods and containers that make up a running instance.
* **Product Owner Expectations**: What is asked of this product's owner beyond the general expectations above.
* **Future Plans**: Planned retirement, migration, or major change.

Products / Services at a Glance
====================

.. list-table::
   :header-rows: 1
   :widths: 14 10 22 27 27

   * - Product
     - Category
     - TS Dev Support
     - Depends On
     - Used By
   * - Allmaps
     - Common
     - N/A
     - N/A
     - Archipelago, Exhibits
   * - Archipelago
     - Common
     - No (DevOps and Deployment only)
     - Avalon
     - Exhibits
   * - Avalon Media System
     - Common
     - No (DevOps and Deployment only)
     - Fedora
     - Archipelago, Exhibits
   * - Browsertrix
     - Common
     - No
     - Need to complete
     - Need to complete
   * - Cantaloupe
     - Common
     - No (DevOps and Deployment only)
     - Fedora
     - IIIFService, Mirador
   * - CAP
     - Unique
     - Yes
     - Mirador, Tamu Library Components, Weaver
     - Fedora, SAGE
   * - Crossref
     - Common
     - No
     - Need to complet
     - Need to complete
   * - Datacite
     - Common
     - No
     - Need to complet
     - Need to complete
   * - Exhibits
     - Common
     - No (DevOps and Deployment only)
     - Archipelago, Avalon
     - Nothing
   * - Fedora
     - Common
     - No (Third Party — Consume)
     - CAP
     - Avalon, IIIF Service, SAGE, Spotlight
   * - From the Page
     - Common
     - No (Third Party — Consume)
     - Archipelago, IIIF Service, Cantaloupe
     - ???
   * - IA Bookreader
     - Unique
     - No (Not listed as a Technology Services product)
     - Not yet recorded
     - Not yet recorded
   * - IIIFService
     - Unique
     - Yes
     - DSpace, Fedora, Cantaloupe
     - From the Page, Spotlight
   * - MAGPIE
     - Unique
     - Yes
     - SAF Creator, Weaver
     - Fedora
   * - Mirador
     - Common
     - No (Third Party — Consume)
     - Cantaloupe
     - CAP, SAGE, Spotlight
   * - Newspapers
     - Common
     - Yes?
     - Need to complete
     - Need to complete
   * - OAKTrust
     - Common
     - No (Not listed as a Technology Services product)
     - DSpace
     - Spotlight?
   * - Open Journal System
     - Common
     - No (Not listed as a Technology Services product)
     - N/A
     - ???
   * - pyavalon
     - Unique
     - No
     - Avalon
     - Avalon
   * - SAF Creator
     - Common
     - Yes (Third Party — Contribute)
     - ???
     - DSpace, MAGPIE
   * - SAGE
     - Unique
     - Yes
     - Avalon, CAP, DSpace, Fedora, Mirador, Tamu Library Components, Weaver
     - N/A
   * - Spotlight
     - Common
     - Yes (Third Party — Contribute)
     - IIIF Service, Mirador, Fedora
     - N/A
   * - Strawberry Field Clover IIIF
     - Unique
     - No
     - N/A
     - Archipelago
   * - tamu_allmaps
     - unique
     - No
     - Need to complete
     - Need to complete

-----------
Archipelago
-----------

About
=====

Archipelago Commons is an open-source digital repository and digital asset management (DAM) platform built on top of
Drupal and developed by the Metropolitan New York Library Council. It's designed primarily for the GLAM community to
manage, preserve, and provide access to digital collections. As of 2026, it is the primary solution for cultural heritage
collections at Texas A&M University Libraries.

* **Current Product Owner**: Mark Baggett
* **Repositories**:

  * https://github.com/esmero
  * https://github.com/cantaloupe-project/cantaloupe

* **Development Support from Technology Services**: No (DevOps and Deployment only)

Dependencies
============

* **Depends on** (Supported By): Avalon, Strawberry Clover IIIF, TAMU Allmaps, AllMaps
* **Used by** (Supports): Exhibits

Instances and Clusters
======================

* Dev
* Pre
* Prod

PODS and Containers
===================

.. note::

   For Archipelago, pods and containers vary by Cluster.  For instance, production has redis and no s3, but other Clusters
   may have an s3 pod like seaweed.

* esmero-cantaloupe: Used as image server in each cluster
* esmero-minio: Used as storage instance in dev and pre.  Not used in prod.
* esmero-nlp: Used for complex processing including in the OCR process
* esmero-php: Used as Drupal, PHP, and Drush layer.
* esmero-solr: Solr instance
* esmero-web: Web server
* redis: Serves as caching layer for front end

Product Owner Expectations
==========================

* Serves as technical expert of platform within the Libraries
* Monitors Archipelago community development and contributes issues and other problems as necessary
* Liaises with Archipelago community
* Listens to feedback from library stakeholders and brings problems or solutions to Archipelago community or digital collections team
* Leads troubleshooting of problems with platform
* Monitors Archipelago security for needed fixes
* Ensures the application is up to date, functioning, and secure
* Monitors logs to ensure it is is functioning as expected

Related Documentation
=====================

See the ``applications/archipelago`` section of this documentation for workflows and troubleshooting.

-------------------
Avalon Media System
-------------------

About
=====

Avalon is an open-source system for managing and providing access to large collections of
digital audio and video.

* **Current Product Owner**: Mark Baggett
* **Development Support from Technology Services**: No (Third Party — Consume)
* **Campus Category**: Common
* **Related servers**: pyavalon

Dependencies
============

* **Depends on** (Supported By): Fedora
* **Used by** (Supports): Not yet recorded

Instances and Clusters
======================

* Dev
* Pre
* Prod

PODS and Containers
===================

* kaltura: streaming server
* avalon-db: database server
* avalon: application server
* avalon-solr: solr instance
* avalon-redis: caching layer
* avalonworker: handles transcoding of audio / video
* fedora (fcrepo4): serves as the repository

Product Owner Expectations
==========================

* Serves as technical expert of platform in the Libraries
* Monitors Avalon Slack channel
* Attends monthly Avalon calls and represents TAMU Libraries
* Determines roadmap and next steps for Avalon migration

Related Documentation
=====================

See the ``applications/avalon`` section of this documentation for workflows and troubleshooting.

----------
Cantaloupe
----------

About
=====

Cantaloupe is an open-source dynamic image server for on-demand generation of derivatives
of high-resolution source images.

It is currently the service behind Fedora collections only.

* **Current Product Owner**: Mark Baggett
* **Development Support from Technology Services**: No (Not listed as a Technology Services product)
* **Serves**: iriiifservice

Dependencies
============

* **Depends on** (Supported By): Not yet recorded
* **Used by** (Supports): IIIFService, Mirador

.. note::

   Archipelago runs its own Cantaloupe container (``esmero-cantaloupe``). That is a separate instance and is
   owned as part of Archipelago, not as part of this product.

Instances and Clusters
======================

* Dev
* Pre
* Prod

PODS and Containers
===================

* cantaloupe

Product Owner Expectations
==========================

* Serves as technical expert of the platform, its delegates file, and the IIIF Image API
* Troubleshoots issues with the platform

Future Plans
============

Spin down once Fedora migration is complete. This means

---
CAP
---

About
=====

The Curator's Administrative Platform provides a user interface for Fedora repositories. This functionality could be extended
to other repositories such as DSpace 7 with some development work. CAP ensures that curators use valid RDF predicates for
triples about Fedora resources. More details are on the Lyrasis/Duraspace website at
https://duraspace.org/introducing-cap-curators-administrative-platform-from-texas-am-university-libraries/ and in the code
base hosted at https://github.com/tamulib/cap.

* **Current Product Owner**: Mark Baggett
* **Repository**: https://github.com/tamulib/cap
* **Development Support from Technology Services**: Yes
* **Campus Category**: Unique

Dependencies
============

* **Depends on** (Supported By): Mirador, Tamu Library Components, Weaver
* **Used by** (Supports): Fedora, SAGE

Product Owner Expectations
==========================

* Listens to feedback from library stakeholders and articulates problems to dev team
* Serves as technical expert
* Advocates for development

Instances and Clusters
======================

* Dev
* Pre
* Prod

PODS and Containers
===================

* cap

Future Plans
============

Spin down once Fedora migration is complete.

------
Fedora
------

About
=====

Fedora is a digital repository that uses linked data (RDF). It is used as the assets management system for SAGE and Spotlight
collections. The same instance is also used for Avalon Media System, although it functions very differently.  Specifically,
Avalon only uses Fedora for asset management.  It does not use Fedora's Solr or Fuseki instance which can be problematic
for SAGE collections.

Also, TAMU has its own specific flavor of RDF based loosely around PCDM.

* **Current Product Owner**: Mark Baggett
* **Development Support from Technology Services**: No (Third Party — Consume)
* **Campus Category**: Common

Dependencies
============

* **Depends on** (Supported By): CAP
* **Used by** (Supports): Avalon, IIIF Service, SAGE, Spotlight

Product Owner Expectations
==========================

* Serves as technical expert of the platform and of TAMU's PCDM-based RDF model
* Coordinates changes that affect more than one dependent product (Avalon, IIIF Service, SAGE, Spotlight)
* Leads troubleshooting of problems with platform

Future Plans
============

A Fedora migration is planned. CAP and Cantaloupe will be spun down once it is complete.

.. note::

   TBD: record the target platform for each Fedora collection and the expected migration timeline.

-------------
IA Bookreader
-------------

About
=====

IA Bookreader was developed by the Internet Archive and open source contributors to provide
online access to scanned books.

* **Current Product Owner**: TBD
* **Development Support from Technology Services**: No (Not listed as a Technology Services product)

Dependencies
============

* **Depends on** (Supported By): Not yet recorded
* **Used by** (Supports): Not yet recorded

Product Owner Expectations
==========================

* TBD

-------------
IIIFService
-------------

About
=====

The IIIF Service provides IIIF manifest generation from DSpace RDF and/or Fedora PCDM.

* **Current Product Owner**: Mark Baggett
* **Development Support from Technology Services**: Yes
* **Campus Category**: Unique

Dependencies
============

* **Depends on** (Supported By): DSpace, Fedora, Cantaloupe
* **Used by** (Supports): From the Page, Spotlight

Product Owner Expectations
==========================

* Serves as technical expert of the platform and of the IIIF Presentation API
* Listens to feedback from library stakeholders and articulates problems to dev team
* Advocates for development

Related Documentation
=====================

See ``other_services/iiif.rst`` for background on IIIF at Texas A&M.

------
MAGPIE
------

About
=====

MAGPIE (Metadata Assignment GUI Providing Ingest and Export) provides a suite of features
for curating documents for deposit to repositories.

* **Current Product Owner**: Mark Baggett
* **Development Support from Technology Services**: Yes
* **Campus Category**: Unique

Dependencies
============

* **Depends on** (Supported By): SAF Creator, Weaver
* **Used by** (Supports): Not yet recorded

Product Owner Expectations
==========================

* Listens to feedback from library stakeholders and articulates problems to dev team
* Serves as technical expert
* Advocates for development

-------
Mirador
-------

About
=====

Mirador is an open-source, web-based, multi-window image viewing platform with the ability
to zoom, display, compare, and annotate images.

* **Current Product Owner**: Mark Baggett
* **Development Support from Technology Services**: No (Third Party — Consume)
* **Campus Category**: Common

Dependencies
============

* **Depends on** (Supported By): Cantaloupe
* **Used by** (Supports): CAP, SAGE, Spotlight

Product Owner Expectations
==========================

* Serves as technical expert of the viewer and its configuration
* Tracks upstream releases and decides when to upgrade
* Verifies that upgrades do not break CAP, SAGE, or Spotlight

--------
OAKTrust
--------

About
=====

OAKTrust is the Texas A&M University Libraries institutional repository. It collects, preserves, and provides access to the
University's scholarly output, along with that of partners such as Texas A&M AgriLife and TEEX. It runs on DSpace, which we
currently use without local modification.

* **Current Product Owner**: TBD
* **Development Support from Technology Services**: No (Not listed as a Technology Services product)

Dependencies
============

* **Depends on** (Supported By): DSpace
* **Used by** (Supports): Not yet recorded

Instances and Clusters
======================

* TBD

Product Owner Expectations
==========================

* Serves as technical expert of the platform
* Liaises with the DSpace community
* Listens to feedback from depositors and library stakeholders
* TBD: split responsibilities between the Product Owner and the Institutional Repository Administrator, who stewards the
  repository day to day (see :doc:`03_people`)

Related Documentation
=====================

See the ``applications/dspace`` section of this documentation for ingest workflows and troubleshooting.

-------------------
Open Journal System
-------------------

About
=====

Open Journal Systems (OJS) is an open-source journal management and publishing platform developed by the Public Knowledge
Project. The Libraries host journals on OJS in partnership with the Texas Digital Library (see
:doc:`08_partners_and_stakeholders`).

* **Current Product Owner**: Mark Baggett (oversees all instances of OJS)
* **Development Support from Technology Services**: No (Not listed as a Technology Services product)

Dependencies
============

* **Depends on** (Supported By): Not yet recorded
* **Used by** (Supports): Not yet recorded

Instances and Clusters
======================

* TBD

Product Owner Expectations
==========================

* Serves as technical expert of the platform
* Supports journal teams, including onboarding, ISSN registration, and DOI minting
* Tracks OJS upgrades and plans migrations between versions

Related Documentation
=====================

See the ``applications/ojs`` section of this documentation.

--------
pyavalon
--------

About
=====

TBD: describe what pyavalon does and why it exists.

* **Current Product Owner**: TBD
* **Development Support from Technology Services**: TBD
* **Related**: Avalon Media System

Dependencies
============

* **Depends on** (Supported By): Not yet recorded
* **Used by** (Supports): Not yet recorded

Product Owner Expectations
==========================

* TBD

-----------
SAF Creator
-----------

About
=====

SAF Creator is a desktop application that takes spreadsheets of metadata and documents and
creates a DSpace SAF archive.

* **Current Product Owner**: Mark Baggett
* **Development Support from Technology Services**: Yes (Third Party — Contribute)
* **Campus Category**: Common

Dependencies
============

* **Depends on** (Supported By): Not yet recorded
* **Used by** (Supports): DSpace, MAGPIE

Product Owner Expectations
==========================

* Listens to feedback from library stakeholders and articulates problems to dev team
* Serves as technical expert
* Advocates for development

----
SAGE
----

About
=====

SAGE (Solr AGgregation Engine) can combine Solr indices from multiple sources and make
their documents discoverable in user-configurable views.

* **Current Product Owner**: Mark Baggett
* **Development Support from Technology Services**: Yes
* **Campus Category**: Common

Dependencies
============

* **Depends on** (Supported By): Avalon, CAP, DSpace, Fedora, Mirador, Tamu Library Components, Weaver
* **Used by** (Supports): Not yet recorded

Product Owner Expectations
==========================

* Listens to feedback from library stakeholders and articulates problems to dev team
* Serves as technical expert, including Solr schema and index configuration
* Advocates for development

Related Documentation
=====================

See the ``applications/sage`` section of this documentation for import workflows.

---------
Spotlight
---------

About
=====

Spotlight is open-source software that enables librarians, curators, and other content
experts to easily build feature-rich websites that showcase collections.

* **Current Product Owner**: Mark Baggett
* **Development Support from Technology Services**: Yes (Third Party — Contribute)
* **Campus Category**: Common

Dependencies
============

* **Depends on** (Supported By): IIIF Service, Mirador, Fedora
* **Used by** (Supports): Not yet recorded

Product Owner Expectations
==========================

* Listens to feedback from library stakeholders and articulates problems to dev team
* Serves as technical expert
* Contributes fixes upstream where appropriate
