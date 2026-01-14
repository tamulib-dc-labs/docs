=========================
Digital Project Workflows
=========================

With the addition of the Center of Digital Humanities Research (CoDHR) joining the Libraries**,
the scope and variety of digital work supported by the Libraries has expanded. In addition
to internally owned and stewarded collections, the Libraries will now increasingly support **Digital
Humanities projects** that originate outside the Libraries and involve materials not owned by Texas
A&M University Libraries, including those not held by **Cushing Memorial Library**.

This shift requires clearer distinctions between:

* **In-house digital projects**, where the Libraries assume curatorial,
  descriptive, access, and preservation responsibility
* **Service-oriented digital humanities projects**, where the Libraries
  provide digitization and technical support without assuming ownership or
  long-term stewardship

The **Digital Project Management Team (DPMT)** remains essential for
projects where the Libraries may own the materials and where the project
requires full lifecycle management, policy review, and long-term commitment
for the management of the work and its associated files. However, the needs
and lifecycle of Digital Humanities projects is very different. These projects
have digitization needs but do not necessarily have needs for descriptive metadata,
website development, preservation, or asset management.

To ensure consistency, transparency, and effective use of digitization
resources, **all proposed digital projects will be funneled through a single
intake and decision framework** that lives with the Digital Collections department.
This approach will allow the Libraries to:

* Confirm project approval and institutional alignment
* Clearly distinguish stewardship projects from service engagements
* Set and communicate digitization priorities
* Apply the appropriate workflow without overburdening limited resources

The decision process below guides project routing into either the
**standard Digital Collections workflow through DPMT** or the **Digital Humanities
Service Track**.

-----------------------------
Project Routing Decision Tree
-----------------------------

.. mermaid::

   flowchart TD

   A["IDEA Document Submitted to DPMT"]
   B{"The Project was approved<br>and submitted by CoDHR?"}
   C{"Are the resources<br>owned by the Libraries<br>(including Cushing)?"}
   D["Standard Digital Collections<br>Workflow (DPMT)"]
   E["Digital Humanities<br>Service Track"]
   F["Standard Digital Collections<br>Workflow (DPMT)"]

   A --> B
   B -- No --> F
   B -- Yes --> C
   C -- Yes --> D
   C -- No --> E

--------------------------------
Digital Humanities Service Track
--------------------------------

This workflow applies to Digital Humanities (DH) projects in which the
Libraries are providing digitization and technical services for materials
that are **not owned by Texas A&M University Libraries or the University**.

These projects are treated as **service engagements**, not as collection
acquisitions.

-----
Scope
-----

The DH Service Track supports:

* Digitization of materials
* Optional file processing and derivative creation
* Minting of ARK identifiers
* Optional loading into the asset management system with minimal metadata
* Optional metadata enhancement

It does **not** include full curatorial review, public exhibits, or
long-term collection stewardship.

If a DH project requires any optional steps, the IDEA document must state so explicitly.

----------------------
Full DH Track Workflow
----------------------

.. mermaid::

   flowchart TD

   A["DH Project Request submitted<br>(CoDHR)"]
   B["Project Acknowledged and Presented at DPMT<br>(Mark)"]
   C{"IDEA Document is Clear and<br> There are No Issues (DPMT)"}

   D["Timeline and Prioritization is Given to Project (DPMT)"]
   E["Physical Materials are Transferred to DiSC (CoDHR)"]
   F["Digitization and any Processing is Completed (DiSC)"]
   G["Service Files are Created (Mark)"]
   H["ARKs are Minted for Each File and Item (Mark)"]
   I["Service Files are Returned to<br> CoDHR following ARK conventions (Mark)"]
   J{"Was Rights Analysis Performed and Items a Good Candidate for DAMS"}

   K["Items and Files Ingested with Minimal metadata (Mark)"]
   L{"Is there time for metadata remediation"}

   M["Metadata Remediated (Jeannette)"]
   N["Items Persist with Minimum Metadata"]

   O["Project Complete"]
   P["CoDHR Notified and Asked to Resubmit (Mark)"]

   A --> B --> C
   C -- Yes --> D --> E --> F --> G --> H --> I --> J
   C -- No --> P
   J -- Yes --> K --> L
   J -- No --> O
   L -- Yes --> M
   L -- No --> N

-------------------
DPMT Track Workflow
-------------------

See :doc:`DPMT Process <dpmt_process>`
