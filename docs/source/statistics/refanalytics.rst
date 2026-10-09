==============================================
RefAnalytics: Classifying a Patron Interaction
==============================================

This document is based on `RefAnalytics Guide for Recording Patron Interactions <https://docs.google.com/document/d/1WEIoIK5KBM5hYA9nCLXje0IqDgqSQeNU/edit?usp=sharing&ouid=105546367335888507442&rtpof=true&sd=true>`.

**Guiding principle:** classify by the *expertise provided*, not by the location,
service point, or communication channel (in person, phone, email, chat, text,
virtual meeting).

.. mermaid::

   flowchart TD
       START([Patron interaction]) --> Q1{"Is it a planned instructional activity?<br/>Workshop, class session, presentation,<br/>orientation, credit course, outreach"}

       Q1 -- Yes --> INS["Instruction Session<br/>Record in Instruction Manager,<br/>not RefAnalytics"]
       Q1 -- No --> Q2{"Did you engage with an information<br/>or research need?<br/>Use, recommend, interpret, evaluate,<br/>or teach a resource or research tool"}

       Q2 -- No --> Q4{"What kind of help?"}
       Q4 -- Navigation --> DIR["Non-Reference: Directional<br/>Copier, stacks, restroom,<br/>service points, offices"]
       Q4 -- Equipment or software --> TECH["Non-Reference: Technical<br/>Printing, paper jams,<br/>equipment operation"]
       Q4 -- Anything else --> OTH["Non-Reference: Other<br/>Hours, parking, circulation,<br/>policy, lost and found"]

       Q2 -- Yes --> Q3{"Was it substantial, individualized<br/>research guidance or extended support?<br/>Includes interactions that grew<br/>into substantial support"}
       Q3 -- Yes --> CON["Consultation<br/>Research planning, search strategy,<br/>Zotero/EndNote training, scholarly comm,<br/>data, GIS, DH, archival discovery"]
       Q3 -- No --> REF["Reference Transaction<br/>Catalog/database help, resource<br/>recommendations, citation help,<br/>brief instruction, referrals"]

       classDef ref fill:#dbeafe,stroke:#1e40af,color:#1e3a8a
       classDef con fill:#dcfce7,stroke:#166534,color:#14532d
       classDef non fill:#f3f4f6,stroke:#4b5563,color:#1f2937
       classDef ins fill:#fef3c7,stroke:#92400e,color:#78350f
       class REF ref
       class CON con
       class DIR,TECH,OTH non
       class INS ins

Edge cases
==========

Referrals
   If you engaged long enough to identify an information need (including a need
   for specialized IT, data, or software help) and then referred the patron, it is
   a **Reference Transaction**. If you only gave directions or routed the patron
   without engaging the need, it is **Non-Reference (Directional)**.

Technology help
   Teaching a patron to use technology in support of research or academic work is
   **Reference** or **Consultation**, depending on depth. Purely operational help
   (printing, paper jams) is **Non-Reference (Technical)**.

Small groups
   Group size does not decide the category. A customized research consultation is a
   **Consultation** whether it involves one person or a small group; a planned
   teaching activity is an **Instruction Session** at any size.

Research teams
   A consultation with a research team counts as **one** consultation, unless
   separate individualized consultations are held with individual team members.