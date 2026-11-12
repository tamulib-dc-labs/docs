Teaching the OJS 3.5 Editorial Workflow (60 min)
================================================

Session at a glance
-------------------

One pre-staged test submission carries the whole hour: attendees watch it move
from Submission to Published, then practice on scenarios.

**Audience:** journal editors and section editors (copyeditors and layout
editors welcome). **Goal:** by the end, each attendee can find their
submissions on the 3.5 dashboard, take a submission through one review round,
and know where copyediting and production happen. **Out of scope:** journal
settings, user management beyond invitations, and theming.

.. list-table::
   :header-rows: 1
   :widths: 12 28 60

   * - Time
     - Block
     - What attendees leave with
   * - 0–10
     - Orientation
     - The four stages and the new 3.5 dashboard
   * - 10–20
     - Submission stage
     - Assigning an editor, discussions, sending to review
   * - 20–35
     - Review stage
     - Adding reviewers, reading reviews, recording a decision
   * - 35–45
     - Copyediting and Production
     - Galleys, DOIs, scheduling for an issue
   * - 45–55
     - Scenarios
     - Finding the right action under pressure
   * - 55–60
     - Wrap-up
     - Where to get help afterward

Before the session
------------------

Start prep at least a week out: in 3.5, Journal Editors can no longer assign
roles without sending an invitation the user must accept, so dummy accounts
depend on someone clicking email links. Only Site Administrators (TDL, for our
instance) can edit user details directly.

**1. Get a sandbox journal.** Ask TDL for a test journal on the 3.5 instance,
or use a real journal with clearly labeled TEST submissions you delete
afterward. Confirm the instance sends email, since invitations depend on it.

**2. Create the cast.** Use mailboxes you control (shared or departmental
addresses work well). For each, go to Settings > Users & Roles > Invite to a
Role, search to confirm no existing account, enter the name and role, then
Save and Continue > Invite user to the role. Accept each invite from its
mailbox.

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Account
     - Role
     - Used in
   * - Ed Itor
     - Journal Editor
     - All blocks (your main view)
   * - Sam Section
     - Section Editor
     - Submission stage assignment
   * - Ana Author
     - Author
     - Submitting, revisions, author's view
   * - Rev One
     - Reviewer
     - Review stage
   * - Rev Two
     - Reviewer
     - Review stage, declined-review scenario
   * - Cory Copy
     - Copyeditor
     - Copyediting stage
   * - Lee Layout
     - Layout Editor
     - Production stage

**3. Pre-stage four submissions** (as Ana Author, using Start a New
Submission), each with an obviously fake title:

#. **"TEST A"** left in the Submission stage, unassigned (you assign it live).
#. **"TEST B"** sent to Review with Rev One and Rev Two assigned; complete Rev
   One's review ahead of time so there is something to read.
#. **"TEST C"** in Copyediting, with a draft file and a Copyeditor assigned.
#. **"TEST D"** in Production, with a PDF ready to upload as a galley, plus a
   future issue created to schedule it into.

**4. Set up the screen.**

- ☐ Two browser profiles: one logged in as Ed Itor, one as Ana Author or a
  reviewer, to show both sides of a handoff. As a Journal Manager you can also
  use **Login As** from the Participants menu, but every action taken that way
  is logged.
- ☐ Zoom the browser to 125% so the dashboard reads on a projector.
- ☐ Start the recording.
- ☐ Open the PKP editorial workflow guide in a tab for the wrap-up.

Block 1 (0–10 min): Orientation
-------------------------------

The point to land: four stages, and the 3.5 dashboard is a set of filtered
views over them. Navigation changed in 3.5; the stages did not.

#. **Draw the lifecycle** (whiteboard or one slide): Submission → Review →
   Copyediting → Production → Scheduled → Published, with Declined branching
   off Submission and Review. Say once: any stage can be skipped (for example,
   Accept and Skip Review).
#. **Log in as Ed Itor** and open the Dashboard from the user menu. It opens on
   **Assigned to Me**.
#. **Walk the columns:** ID, Submission, Stage, Days (time in the current
   stage), Editorial Activity, Actions (View).
#. **Point out the stage dots.** Name each status: Incomplete, Submission,
   Review (with round number), Copyediting, Production, Scheduled for
   Publication, Published, Declined.
#. **Click through the views** in the left menu and watch the counts. Mention
   that Needs Editor and Declined are only visible at Journal Manager level;
   Section Editors see only their own declines.
#. **Search and filter.** Search for "TEST" to show all four submissions, then
   open Filters and show Sections and Days Since Last Activity. Tip for
   editors: Days Since Last Activity is the fastest way to find stalled items.
#. **Show the bell icon** (Tasks), top right. Mention the weekly email summary
   of items needing action.
#. **Open TEST A with View** and name the three columns of the submission
   record:

   - Left: the **Workflow** menu (the four stages) and the **Publication** menu
     (title, metadata, galleys, issue).
   - Center: stage status, **Files**, and **Discussions**.
   - Right: **action buttons** (decisions) and **Participants**.
   - Top right: **Activity Log** (with editor-only Notes) and **Library**.

.. tip:: **Say this:** "If you get lost, the left menu tells you where you
   are, the right column tells you what you can do."

**3.4 users will ask:** Workflow and Publication used to be tabs across the
top; they now sit in the left menu. Deleting Incomplete submissions is new
(three dots next to Filter > Delete Incomplete Submissions).

Block 2 (10–20 min): Submission stage
-------------------------------------

The point to land: nothing happens until an editor is a participant; then
three buttons decide the submission's path.

**Demo on TEST A (unassigned):**

#. Open TEST A. Note the right column has no decision buttons yet, because no
   editor is assigned.
#. Explain automatic assignment in one breath: if the journal has one editor,
   or editors assigned to the section or category, OJS assigns and notifies
   them automatically. Unassigned items show in the **Needs Editor** view.
#. In **Participants**, click **Assign**. Search by role, choose Section
   Editor, and point out the count of submissions already assigned to each
   person (useful for balancing workload).
#. Select Sam Section. Show the two choices that matter:

   - Can **record** a decision vs. can only **recommend** one.
   - Can or cannot **edit publication details**.

#. Keep the default email template, click **OK**. Sam now appears in
   Participants.
#. Point out that a **Pre-Review Discussion** was created automatically.
#. **Add a discussion:** click Add discussion, pick Ana Author as participant,
   choose the generic Discussion template, write "Please confirm the figures
   are your own," and click **OK**.
#. Switch to the author browser and show Ana sees the discussion. Reply as Ana
   with **Add Message**.
#. Back as Ed Itor, show the three action buttons and explain each:

   - **Send to Review**: moves to the Review stage; you choose which files
     reviewers get.
   - **Accept and Skip Review**: jumps straight to Copyediting (editorials,
     book reviews).
   - **Decline Submission**: desk reject; reversible with **Revert Decline**.

#. Click **Send to Review**, check the files reviewers should see, and click
   **OK**. TEST A's stage dot changes on the dashboard.

.. tip:: **Say this:** "Discussions are the paper trail. Replying to the
   notification email from your inbox does not log anything in OJS. Reply in
   the Discussions panel."

Block 3 (20–35 min): Review stage
---------------------------------

The point to land: assign reviewers, watch the icons, confirm each review,
then record one decision. This block gets the most time because it is where
editors get stuck.

**Part 1, assign a reviewer (live, on TEST A, now in Review):**

1. On the dashboard, open the **Needs reviewers** view. TEST A is there with
   an **Assign Reviewers** button in Editorial Activity.
2. Click it. Walk the reviewer list: affiliation, active reviews, days since
   last assigned. Mention that author-suggested reviewers appear here too (new
   in 3.5).
3. Click the blue arrow beside a reviewer to show their history and interests.
4. Point to the bottom of the list: **Create New Reviewer** (no account yet)
   and **Enroll Existing User** (has an account, not a reviewer).
5. **Select Reviewer** on Rev One. In the request window, set the **Response
   Due Date** and **Review Due Date**, open **Files to be Reviewed**, and
   confirm the review type.
6. **Anonymity check:** if the review is Anonymous Reviewer/Anonymous Author,
   select only anonymized files. OJS hides names in the system, but not inside
   the Word file or its document properties.
7. Click **Add Reviewer**.

**Part 2, read the dashboard icons (switch to TEST B):**

8. Open the **Awaiting reviews** and **Reviews submitted** views and read TEST
   B's Editorial Activity icons aloud.

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Icon
     - Meaning
   * - Yellow circle with number
     - Days left to respond to the request
   * - Outlined red circle
     - Response overdue by that many days
   * - Outlined blue circle
     - Review in progress; days until due
   * - Filled red circle
     - Review overdue by that many days
   * - Pink circle with slash
     - Reviewer declined
   * - Pink circle with X
     - Review cancelled
   * - Green mail
     - Review submitted; editor must confirm
   * - Green checkmark
     - Review confirmed by an editor

**Part 3, read and confirm a review (TEST B):**

9. In the Reviewers panel, click **Read Review** beside Rev One. Show the
   recommendation and comments.
10. Click **Confirm** at the bottom. Show the follow-ups that appear: **Thank
    Reviewer** and **Revert Decision**.
11. Open the three-dots menu on Rev Two to show Email Reviewer, Edit (change
    due dates), and Cancel/Unassign Reviewer.

**Part 4, record a decision (TEST B):**

12. Show the four action buttons: **Request Revisions**, **Accept
    Submission**, **Create New Review Round**, **Decline Submission**.
13. Click **Request Revisions**. Choose whether the revision needs a new
    review round, edit the author email, optionally notify reviewers, and
    click **Record Decision**.
14. Switch to the author browser. Show Ana's view of the revision request and
    where she uploads the revised file.
15. Back as Ed Itor, show the revised file under **Revisions**. Explain the
    next move is a new round, or **Accept Submission**, which sends it to
    Copyediting.

.. tip:: **Say this:** "Open a new review round only after the author uploads
   revisions. Otherwise the author may upload into the wrong round."

Block 4 (35–45 min): Copyediting and Production
-----------------------------------------------

The point to land: Copyediting turns a draft file into a copyedited file;
Production turns that into galleys, checks the metadata, and schedules the
article into an issue. Move briskly; most journals have one person doing both.

**Copyediting (TEST C, about 4 minutes):**

1. Open the **All in copyediting** view and open TEST C.
2. Show the two file panels: **Draft Files** (what came out of review) and
   **Copyedited Files** (the finished version).
3. Point out Cory Copy in Participants. Assigning works exactly like assigning
   an editor: **Assign**, role Copyeditor, **Search**, **OK**. Assigning opens
   a discussion with the request.
4. In **Copyedited Files**, click **Upload/Select Files**. Show the three
   options: upload a new file, select the draft unchanged, or select a file
   from a discussion. Check the file and click **OK**.
5. Click **Send to Production**, keep the author email, confirm the copyedited
   files are selected, and click **Record Decision**.

**Production (TEST D, about 6 minutes):**

6. Open TEST D from **All in production**. Show **Production Ready Files** and
   Lee Layout in Participants.
7. In the left **Publication** menu, open **Galleys** > **Add galley**. Label
   it PDF, choose the language, click **Save**, upload the PDF, and click
   **Complete**.
8. Click **Preview** (top right) to show the article page as readers will see
   it.
9. Walk the rest of the Publication menu in one pass: Title & Abstract,
   Contributors, Metadata, References, JATS XML (new in 3.5, if your journals
   publish XML), Permissions & Disclosure, Issue. Remind people to click
   **Save** on each page.
10. **DOIs:** if the journal uses Crossref, show the **DOIs** item in the left
    sidebar. Filter by **Needs DOI**, check TEST D, and use **Bulk Actions** >
    Assign DOIs. Mention that Deposit is a separate step (Bulk Actions >
    Deposit DOIs) unless automatic depositing is on.
11. Click **Schedule for Publication**, choose the future issue you created in
    prep, and click **Save**. TEST D now shows Scheduled on the dashboard.
12. Close the loop: in the left sidebar, open **Issues** > Future Issues,
    click the blue arrow on that issue, and show **Preview** and **Publish
    Issue**. Do not click Publish Issue on a live journal.

.. tip:: **Say this:** "Once an article is published, small fixes mean
   Unpublish, fix, reschedule. Substantive changes, like a correction or
   retraction, mean Create New Version. And OJS won't push metadata changes to
   Crossref on its own; you redeposit."

Block 5 (45–55 min): Scenarios
------------------------------

Read each scenario aloud and have attendees say (or, in a hands-on room,
click) where they would go. Aim for 2 minutes each; skip the last ones if time
runs short.

**1. A reviewer hasn't answered the request, and it's past the response date.**
   On the dashboard you'll see an outlined red circle. Click it to send a
   reminder or adjust the due date, or use the reviewer's three-dots menu >
   Unassign Reviewer, then add someone else.

**2. A reviewer declined.**
   Pink circle with a slash. Open the submission > Reviewers > **Add
   Reviewer** and assign a replacement. To try the same person again, use
   **Reinstate Reviewer**; they must accept the new invitation.

**3. You declined a submission by mistake.**
   Open the **Declined** view (Journal Manager level), open the submission,
   and click **Revert Decline**. It returns to its previous stage.

**4. The author replied to the OJS email from Outlook, and you can't find the message in OJS.**
   Inbox replies aren't logged. Ask the author to reply in the Discussions
   panel, or paste the reply into a discussion yourself so the record is
   complete.

**5. An editorial or book review doesn't need peer review.**
   In the Submission stage, use **Accept and Skip Review**.

**6. A typo in a published article's abstract.**
   Publication menu > **Unpublish**, fix it, **Save**, then **Schedule for
   Publication** again. If it has a DOI, redeposit the metadata from the DOIs
   page.

**7. Which submissions have stalled?**
   Any dashboard view > **Filters** > Days Since Last Activity. Editors also
   get a weekly email listing copyediting and production items inactive for 30
   or more days.

**8. A colleague needs to join the editorial team.**
   Settings > Users & Roles > **Invite to a Role**. They must accept the
   emailed invitation before you can assign them. If they never receive it,
   the fix goes to the Site Administrator (TDL).

Block 6 (55–60 min): Wrap-up
----------------------------

End on where to get help, not on a recap.

#. Put the lifecycle diagram back up and ask: "Which stage do you expect to
   spend the most time in?" Take one or two answers.
#. Share the leave-behinds (paste these in the chat or the follow-up email):

   - `Learning OJS 3.5: The Editorial Workflow
     <https://docs.pkp.sfu.ca/learning-ojs/editorial-workflow/en/>`__, for
     editors, copyeditors, and layout editors
   - `Learning OJS 3.5 for Reviewers
     <https://docs.pkp.sfu.ca/learning-ojs/reviewer/en/>`__ and `for Authors
     <https://docs.pkp.sfu.ca/learning-ojs/author/en/>`__, to forward to their
     reviewers and authors
   - `About OJS 3.5 <https://docs.pkp.sfu.ca/learning-ojs/about-ojs/en/>`__,
     including what changed in 3.5
   - The session recording

#. Tell them who to contact: the library for workflow and journal setup
   questions; TDL (through the library) for account, email, and invitation
   problems.
#. Take questions until time.

**After the session:**

- ☐ Delete or decline the TEST submissions, or ask TDL to remove the test
  journal.
- ☐ Send the follow-up email with links and the recording.
- ☐ Note the questions you couldn't answer; they're your FAQ for next time.

Sources
-------

- PKP, `Learning OJS 3.5: The Editorial Workflow
  <https://docs.pkp.sfu.ca/learning-ojs/editorial-workflow/en/>`__ (dashboard,
  submission, review, copyediting, production, and publication chapters)
- PKP, `Learning OJS 3.5 for Journal Managers
  <https://docs.pkp.sfu.ca/learning-ojs/journal-managers/en/>`__ (inviting
  users, DOIs)
- PKP, `OJS 3.5.0 release announcement
  <https://pkp.sfu.ca/2025/06/16/350-release-announcement/>`__
