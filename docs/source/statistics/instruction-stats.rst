=================================================
Instruction Stats: Choosing a Category
=================================================

This document is guided by the Libraries' `A Guide to the Libraries' Instruction Stats System <https://docs.google.com/document/d/1jZ8dK4u69tJzERr37SZ2TXDlH5FPwoCnEa3PCNd-kGY/edit?usp=sharing>`_.

Instruction and outreach statistics are recorded in the **Instructional Stats**
tab of the Instruction Manager system (Evans, Annex, WCL, and Cushing).
One-on-one reference consultations are **not** recorded here; they go in
RefAnalytics.

.. mermaid::

   flowchart TD
       START([Instruction or outreach activity]) --> Q0{"Is it a one-on-one reference<br/>interaction or consultation?"}

       Q0 -- Yes --> RA["Record in RefAnalytics<br/>not Instruction Manager"]
       Q0 -- No --> Q1{"Is it for a curricular course with a<br/>department and number and an<br/>instructor of record?"}

       Q1 -- Yes --> CLASS["Library Class<br/>Record class section and format:<br/>in person, online, or hybrid"]
       Q1 -- No --> Q2{"Is the audience a K-12 school group<br/>not affiliated with the university?"}

       Q2 -- Yes --> K12["K-12 School Visit<br/>Librarian-led tour or workshop"]
       Q2 -- No --> Q3{"Is it tied to new student orientation?<br/>New Student Conferences, Fish Camp,<br/>departmental or graduate orientation"}

       Q3 -- Yes --> ORI["Orientation Presentation"]
       Q3 -- No --> Q4{"Is it library-wide professional<br/>development or training<br/>for library staff?"}

       Q4 -- Yes --> INT["Internal Library Training"]
       Q4 -- No --> Q5{"Is it a tour of library<br/>spaces or exhibits?"}

       Q5 -- "Yes, library-led" --> TOUR["Library Tour"]
       Q5 -- "Campus tour stopping<br/>at the library" --> SKIP["Not recorded"]
       Q5 -- No --> Q6{"Was the primary purpose teaching<br/>library resources, research skills,<br/>or services?"}

       Q6 -- Yes --> WS["Workshop<br/>Reported to ACRL"]
       Q6 -- "No: tabling, promotion,<br/>quick interactions" --> OUT["Outreach<br/>Internal reporting only"]

       classDef instr fill:#dbeafe,stroke:#1e40af,color:#1e3a8a
       classDef out fill:#dcfce7,stroke:#166534,color:#14532d
       classDef elsewhere fill:#f3f4f6,stroke:#4b5563,color:#1f2937
       class CLASS,K12,ORI,INT,TOUR,WS instr
       class OUT out
       class RA,SKIP elsewhere

Edge cases
==========

Workshop or Outreach?
   Some outreach events include presentations or guided learning. If the
   primary purpose is instructional and participants are learning skills,
   concepts, resources, or research practices, record it as a **Workshop**
   so it is included in ACRL instructional reporting. Examples: Professional
   Development Series presentations, Aggie Moms presentations, Friends of the
   Libraries presentations, Peer Mentor Training.

Co-taught or multi-unit events
   Only **one** person records the event; list the others in the
   *Additional Library Instructor* field. Duplicate entries inflate the data.
   For example, the Head of Student Engagement and Outreach enters Open House
   for all participating groups.

Multiple sessions with the same students
   Use **one** entry and set *Number of Sessions (same students)*; you will be
   prompted for each session date.

Entering on someone else's behalf
   Select the person who taught at the top of the form. Otherwise the stat is
   credited to whoever entered it.

Time spent with librarian
   For presentations, enter the length of the session (often 50–90 minutes).
   For tabling, enter how long an individual spends with you (often about
   5 minutes).

Requesting individual or group
   Use the full department name. For activities originating in the Libraries,
   use ``Libraries-<unit name>``.

CE Course, Credit Course, Other
   Use these sparingly. Consult the Director of the Office of Information
   Literacy before choosing one, since most have only historical uses.