==============================
Products and Product Ownership
==============================

-----
About
-----

The **Product Owner** operates at the center of the product ecosystem, ensuring that stakeholder needs are understood,
customer input is effectively translated, and development efforts are aligned with strategic objectives. They hold decision
authority while maintaining continuous collaboration across institutional and technical boundaries.

This document lays out product ownership for products in the Digital Collections unit.  It describes what is expected for
the product owner, whom they represent, and what is necessary to successfully be a product owner for a service or application.

Terminology
===========

* **Stakeholder**: Any individual or group impacted by the product, directly or indirectly. This includes end users, institutional
units, and external parties whose work or outcomes are affected.

* **Customer**: A subset of stakeholders who are actively engaged in the product development process. Customers interact directly
with the Product Owner, contribute requirements, provide feedback, and influence product direction.

Roles
=====

* **Product Stewardship (Governance & Long-Term Planning)**: Ensure the long-term health, sustainability, and strategic alignment of the product. Establish and maintain governance structures, guide longterm product direction, and ensure continuity across development cycles. Balance immediate delivery needs with future viability, including technical sustainability, institutional alignment, and evolving stakeholder needs.
* **Stakeholder Management**: Maintain awareness of all stakeholder groups, ensure clear stakeholder identification and definition, and understand their needs and their impact on the product, and the product's impact on each stakeholder group.
* **Requirements Gathering**: Actively engage customers to identify needs, anticipate requirements, and refine problem spaces.
* **Backlog Curation**: Own and prioritize the product backlog in collaboration with the development team, balancing competing priorities while maintaining a coherent product vision.
* **Champion / Approval Authority**: Serve as the final decision-maker for product direction, scope, and acceptance of work. Act as the primary advocate for the product, ensuring it receives appropriate development time, resources, and organizational support. Represent the product in prioritization discussions, defends its value, and ensures its needs are clearly articulated.
* **Sprint Participation**: Engage in sprint planning, reviews, and ongoing team interaction to ensure alignment and delivery quality.

-----------
Archipelago
-----------

Archipelago Commons is an open-source digital repository and digital asset management (DAM) platform built on top of
Drupal and developed by the Metropolitan New York Library Council. It's designed primarily for the GLAM community to
manage, preserve, and provide access to digital collections. As of 2026, it is the primary solution for cultural heritage
collections at Texas A&M University Libraries.

Current Product Owner: Mark Baggett
Repository: https://github.com/tamulib/cap
Development Support from Technology Services: No (DevOps and Deployment only)

Instances and Clusters
======================

* Dev
* Pre
* Prod

PODS and Containers
===================

* esmero-cantaloupe: Used as image server in each cluster
* esmero-minio: Used as storage instance in dev and pre.  Not used in prod.
* esmero-nlp: Used for complex processing including in the OCR process
* esmero-php: Used as Drupal, PHP, and Drush layer.
* esmero-solr: Solr instance
* esmero-web: Web server

Product Owner Expectations
==========================

* Serves as technical expert of platform in the Libraries
* Monitor Archipelago community development and contribute issues and other problems as necessary
* Listen to feedback from library stakeholders and bring problems or solutions to Archipelago community or digital collections team

-------------------
Avalon Media System
-------------------

About
=====

Avalon is an open-source system for managing and providing access to large collections of
digital audio and video.

Current Product Owner: Douglas Hahn
Development Support from Technology Services: No (Third Party — Consume)
Campus Category: Common
Supports: SAGE
Supported By: Fedora

----------
Cantaloupe
----------

Cantaloupe is an open-source dynamic image server for on-demand generation of derivatives
of high-resolution source images.

Development Support from Technology Services: No (Not listed as a Technology Services product)

---
CAP
---

About
=====

The Curator's Administrative Platform provides a user interface for Fedora repositories. This functionality could be extended to other repositories such as DSpace 7 with some development work. CAP ensures that curators use valid RDF predicates for triples about Fedora resources. More details are on the Lyrasis/Duraspace website at https://duraspace.org/introducing-cap-curators-administrative-platform-from-texas-am-university-libraries/ and in the code base hosted at https://github.com/tamulib/cap.

Current Product Owner: Mark Baggett
Repository: https://github.com/tamulib/cap
Development Support from Technology Services: Yes
Campus Category: Unique
Supports: Fedora, SAGE
Supported By: Mirador, Tamu Library Components, Weaver

Product Owner Expectations
==========================

* Listen to feedback from library stakeholders and articulate problems to dev team

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

Current Product Owner: Mark Baggett
Development Support from Technology Services: No (Third Party — Consume)
Campus Category: Common
Supports: Avalon, IIIF Service, SAGE
Supported By: CAP

-------------
IA Bookreader
-------------

IA Bookreader was developed by the Internet Archive and open source contributors to provide
online access to scanned books.

Development Support from Technology Services: No (Not listed as a Technology Services product)

-------------
IRIIIFService
-------------

About
=====

The IIIF Service provides IIIF manifest generation from DSpace RDF and/or Fedora PCDM.

Current Product Owner: Douglas Hahn
Development Support from Technology Services: Yes
Campus Category: Unique
Supports: From the Page, Spotlight
Supported By: DSpace, Fedora

------
MAGPIE
------

About
=====

MAGPIE (Metadata Assignment GUI Providing Ingest and Export) provides a suite of features
for curating documents for deposit to repositories.

Current Product Owner: Douglas Hahn
Development Support from Technology Services: Yes
Campus Category: Unique
Supported By: SAF Creator, Weaver

-------
Mirador
-------

About
=====

Mirador is an open-source, web-based, multi-window image viewing platform with the ability
to zoom, display, compare, and annotate images.

Current Product Owner: Douglas Hahn
Development Support from Technology Services: No (Third Party — Consume)
Campus Category: Common
Supports: CAP, SAGE, Spotlight
Supported By: Cantaloupe

--------
OAKTrust
--------

Development Support from Technology Services: No (Not listed as a Technology Services product)

-------------------
Open Journal System
-------------------

Development Support from Technology Services: No (Not listed as a Technology Services product)

-----------
SAF Creator
-----------

About
=====

SAF Creator is a desktop application that takes spreadsheets of metadata and documents and
creates a DSpace SAF archive.

Current Product Owner: James Creel
Development Support from Technology Services: Yes (Third Party — Contribute)
Campus Category: Common
Supports: DSpace, MAGPIE

----
SAGE
----

About
=====

SAGE (Solr AGgregation Engine) can combine Solr indices from multiple sources and make
their documents discoverable in user-configurable views.

Current Product Owner: Bonnie Gardner
Development Support from Technology Services: Yes
Campus Category: Common
Supported By: Avalon, CAP, DSpace, Fedora, Mirador, Tamu Library Components, Weaver

---------
Spotlight
---------

About
=====

Spotlight is open-source software that enables librarians, curators, and other content
experts to easily build feature-rich websites that showcase collections.

Current Product Owner: Douglas Hahn
Development Support from Technology Services: Yes (Third Party — Contribute)
Campus Category: Common
Supported By: IIIF Service, Mirador
