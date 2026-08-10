.. _ojs34-editorial-workflow-tutorial:

===================================================
OJS 3.4 Editorial Workflow: Configuration & Practice
===================================================

.. note::

   **Format:** Self-paced or instructor-led tutorial
   **Length:** 20–30 minutes
   **Audience:** Journal editors and section editors
   **Prerequisites:** An editor-level (or Journal Manager) account on an OJS 3.4 journal

Learning Objectives
====================

By the end of this tutorial, you will be able to:

* Explain the four editorial stages that make up every OJS 3.4 submission's lifecycle.
* Configure the journal's **Workflow Settings** (Submission, Review, Publisher Library, and Emails
  tabs) to match your journal's editorial policies.
* Move a submission through the workflow — from initial intake to a published galley — and know
  which editorial decision to make at each stage.

.. contents:: On this page
   :local:
   :depth: 2

Part 1 — The Four Editorial Stages at a Glance
================================================

Every submission in OJS 3.4 moves through up to four editorial stages, plus a final
**Publication** tab used for scheduling:

#. **Submission** — Intake and triage. The editor decides whether a manuscript is appropriate for
   review.
#. **Review** — Peer review and author revisions.
#. **Copyediting** — Language, style, and clarity edits after a submission passes review.
#. **Production** — Galleys (PDF, HTML, ePub, etc.) are prepared for publication.

A submission does not have to pass through every stage in order — an editor can skip Review
entirely, send a submission backward, or decline it at almost any point. Each stage has its own
**Participants** panel (for assigning people) and a **Discussions** panel (for private,
stage-scoped conversation with authors, reviewers, or fellow editors).

Part 2 — Configuring the Editorial Workflow
=============================================

Before working submissions, a Journal Manager (or an editor with settings access) should configure
**Settings → Workflow**, which has four tabs.

2.1 Submission Tab
--------------------

Controls what happens *before* and *during* the moment an author submits:

* **Disable Submissions** — turn off new submissions journal-wide, or per section via
  *Journal Sections*.
* **Metadata** — enable metadata fields (e.g., keywords, subjects, supporting agencies) and choose
  whether authors fill them in or only editors can.
* **Components** — define file types authors can upload (manuscript, figure, data set, etc.);
  mark components as supplementary or dependent.
* **Checklist** — a list of requirements (formatting, citation style, blinding, etc.) authors must
  confirm before submitting.
* **Author Guidelines** — instructions shown to authors during submission.

2.2 Review Tab
----------------

Controls peer review policy:

* **Setup** — choose the default review mode (open, blind, double-blind); this can be overridden
  per submission. Enabling **one-click reviewer access** lets invited reviewers open the review
  page directly from their email without logging in (editors lose the ability to edit/CC that
  invitation email when this is on).
* **Reviewer Guidance** — criteria and instructions shown to reviewers for judging suitability.
* **Review Forms** — optional structured forms editors can assign so reviewers answer specific
  questions rather than free text only.

2.3 Publisher Library
------------------------

A shared file repository for boilerplate documents — author contracts, release forms, style
guides — that editors can quickly attach to a submission's library during any stage.

2.4 Emails
------------

OJS sends automated emails at nearly every workflow transition (acknowledgement, review invite,
decision letters, etc.). This tab lets you:

* Edit the signature appended to outgoing mail.
* Edit the default subject/body of any template.
* Filter templates by sender, recipient, workflow stage, or enabled status.

.. tip::

   Configure these four tabs *before* your first live submission arrives — Author Guidelines,
   the Checklist, and Reviewer Guidance in particular shape what authors and reviewers see from
   their very first interaction with the journal.

Part 3 — Working a Submission Through the Editorial Process
==============================================================

This is the day-to-day workflow an editor follows once submissions start arriving.

3.1 Stage 1 — Submission
---------------------------

A new submission lands here automatically. The editor reviews the files and decides how to
proceed, optionally assigning a section editor (**Participants** panel) or opening a
**Pre-Review Discussion** with the author first.

**Editorial actions available:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Action
     - What it does
   * - Send to Review
     - Moves the submission into the Review stage for peer review.
   * - Send to Copyediting
     - Skips peer review entirely and sends the submission straight to Copyediting.
   * - Decline Submission
     - Removes the submission from the active workflow and archives it.

3.2 Stage 2 — Review
-----------------------

Peer review happens in **rounds**, starting at Round 1. Each round has its own panels:

* **Review Files** — the files reviewers can see (unless restricted per reviewer).
* **Reviewers** — assign reviewers, set due dates, and track recommendations; confirm a review
  once it's complete.
* **Revisions** — author-uploaded revised files, ready to move forward once approved.
* **Review Discussions** — private conversation among editors, sub-editors, and reviewers
  (authors cannot join or message reviewers directly). Discussions carry over across rounds.

**Editorial decisions at the end of a round:**

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Decision
     - What it does
   * - Request Revisions
     - Minor revisions — the editor can approve them without a new review round.
   * - Resubmit for Review
     - Major revisions — a new review round is created once the author resubmits.
   * - Send to Copyediting
     - The submission has passed review and moves forward.
   * - Decline Submission
     - The submission did not pass review; it is archived.

Every decision automatically emails the author using the templates configured in
:ref:`Emails <ojs34-editorial-workflow-tutorial>` (Part 2.4).

3.3 Stage 3 — Copyediting
----------------------------

A copyeditor (assigned via **Participants**) aligns the writing with house style, checks grammar
and clarity, and prepares the text for layout. If you have no dedicated copyeditor, use this stage
yourself to fact-check and clean up the manuscript.

* **Draft Files** — files selected by the editor for copyediting (typically the approved review
  revisions).
* **Copyediting Discussions** — clarify points with the author or coordinate with the copyeditor.
* **Copyedited** — the finished files, uploaded by the copyeditor (or editor) and ready to move on.

**Editorial action:** *Send to Production* — forwards the submission (and any files in
**Copyedited**) to the Production stage. This is the only decision available at this stage; to
decline this late, an editor must first send the submission back to an earlier stage.

3.4 Stage 4 — Production
---------------------------

Production assistants (assigned via **Participants**) turn the copyedited files into publication
**galleys** — separate formats such as PDF, HTML, or ePub.

* **Production Ready Files** — the finished copyedited files used to generate galleys.
* **Production Discussions** — coordination between editors and production assistants.

Once galleys are ready, the editor uses **Schedule for Publication** to move the submission from
the Workflow panel into the **Publication** tab.

3.5 The Publication Tab
--------------------------

The final step before (and after) an article goes live:

* Review and edit the article's metadata.
* Upload the galley file(s).
* Set access/permissions and assign the article to an issue.
* **Create New Version** — publish an updated version of an already-published article while
  preserving prior versions for the public record.
* **Unpublish Article** — remove an article from its issue and public view if needed.

Quick Reference — Editorial Decisions Cheat Sheet
=====================================================

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Stage
     - Decision
     - Result
   * - Submission
     - Send to Review / Send to Copyediting / Decline
     - Advances to Review, skips straight to Copyediting, or archives the submission.
   * - Review
     - Request Revisions / Resubmit for Review / Send to Copyediting / Decline
     - Minor fix without a new round, major revision with a new round, advance, or archive.
   * - Copyediting
     - Send to Production
     - Only available action; declining requires moving back to an earlier stage first.
   * - Production
     - Schedule for Publication
     - Moves the submission to the Publication tab for metadata, galleys, and issue assignment.

Wrap-Up & Additional Resources
==================================

* Every stage has a **Participants** panel (who's assigned) and a **Discussions** panel (private,
  stage-scoped messaging) — get comfortable with both; you'll use them constantly.
* Configuration lives in **Settings → Workflow**; day-to-day work happens in each submission's
  **Workflow** tab.
* Official documentation: `PKP Learning OJS 3 — Editorial Workflow
  <https://docs.pkp.sfu.ca/learning-ojs/en/editorial-workflow.html>`_ and
  `PKP Learning OJS 3 — Workflow Settings <https://docs.pkp.sfu.ca/learning-ojs/en/settings-workflow>`_.
* Source reference for this tutorial: `PKP OJS User Guide — Editorial Workflow
  <https://github.com/pkp/ojs-user-guide/tree/main/en/editorial-workflow>`_ and
  `Workflow Settings <https://github.com/pkp/ojs-user-guide/blob/main/en/settings/workflow-settings.md>`_.

.. seealso::

   Pair this tutorial with a live walkthrough in a sandbox/staging journal so editors can click
   through each stage and decision on a real (test) submission.
