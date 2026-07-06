======
People
======

This page documents who makes up Digital Collections, what each person focuses on, and how the team
reports and collaborates. It is meant to be a quick orientation for new team members — pair it with
:doc:`01_about_digital_collections` for a description of the services these roles support.

---------
Org Chart
---------

.. mermaid::

   graph TD

   MB["Mark Baggett<br>Director of Digital Collections"]
   CB["Corina Barr<br>Digital Collections Librarian"]
   CS["Charity Stokes<br>Institutional Repository Administrator"]
   JVK["Jvk Chaitanya<br>Repository Applications Librarian"]
   AC["Angela Colmenares<br>AI and Machine Learning Librarian"]
   SSM["Sharvari Shekhar Mhatre<br>Institutional Repository Student Technician"]

   MB --> CB
   MB --> CS
   MB --> JVK
   MB --> AC
   CS --> SSM

-----
Roles
-----

* **Mark Baggett — Director of Digital Collections.** Sets strategic direction for the unit and leads
  the team responsible for repository infrastructure, metadata practices, and digital publishing
  services across the Libraries. Currently services as product owner for most of the digital library program technologies
  and oversees all instances of Open Journal Systems.
* **Corina Barr — Digital Collections Librarian.** Supports the curation, description, and delivery of
  cultural heritage digital collections and exhibits.
* **Charity Stokes — Institutional Repository Administrator.** Stewards OAKTrust and the systems that
  manage and provide access to the University's scholarly output.
* **Jvk Chaitanya — Repository Applications Librarian.** Designs, develops, and maintains the digital
  repository infrastructure behind our cultural heritage and institutional repository systems, including
  metadata pipelines, ingest workflows, and web archiving. Also supports other team members with technical development of
  new tooling.
* **Angela Colmenares — AI and Machine Learning Librarian.** Leads the integration of AI and ML tools
  into library workflows, with a focus on metadata creation and enrichment, automated captioning, and
  Retrieval-Augmented Generation (RAG) for digital collections.
* **Sharvari Shekhar Mhatre — Institutional Repository Student Technician.** Supports OAKTrust
  operations and day-to-day institutional repository tasks under Charity Stokes.

---------
Locations
---------

Team Locations
===============

This section describes where team members are physically located.

.. mermaid::

   flowchart TB
       subgraph EA["Evans Annex"]
           direction TB
           subgraph EA6["Floor 6 — Digital Initiatives"]
               r624["624<br/>Mark Baggett"]
               r617["617<br/>Corina Barr"]
               r648["648<br/>Jvk Chaitanya"]
               r615["615<br/>Small DI Conference Room"]
               r614["614<br/>Large DI Conference Room"]
           end
           subgraph EA3["Floor 3 — Cataloging"]
               r325["325<br/>Charity Stokes"]
               rStu["Student Stations<br/>Shavari Mhatre"]
           end
           subgraph EA4["Floor 4 — Preservation"]
               r["421<br/>Preservation Meeting Room"]
           end
       end

       subgraph EV["Evans"]
           direction TB
           subgraph EV2["Floor 2"]
               r212C["212C — Map Room<br/>Angela Colmenares"]
           end
       end
