Aggie Journals Dashboard
========================

The `Aggie Journals Dashboard <https://tamulib-dc-labs.github.io/aggie-journal-dashboard/>`_ is a static website that reports usage and editorial
statistics for the journals we host on `Open Journal Systems
<https://pkp.sfu.ca/software/ojs/>`_ (OJS). It is hosted on GitHub Pages and
has no server-side component. A scheduled job collects statistics from each
journal's OJS REST API and saves them as JSON files in the repository. The
dashboard reads those files in the browser.


How it works
------------

The system has three parts:

1. **Data fetcher** (``fetch_data.py``). A Python script reads the list of
   journals from ``.config/api_keys.yml``, calls each journal's OJS REST API
   (``/api/v1/...``) with that journal's API token, and writes the results as
   JSON files under ``data/``.
2. **Scheduled workflow** (``.github/workflows/fetch-data.yml``). A GitHub
   Actions workflow runs the fetcher and commits any changed files in
   ``data/`` back to the repository.
3. **Static frontend** (``index.html``, ``assets/js/dashboard.js``,
   ``assets/css/style.css``). Plain HTML and JavaScript load the JSON files and
   render summary cards, charts, and tables. No database or API server is
   involved, and API keys never reach the browser.

.. code-block:: text

   ┌──────────────────┐   monthly / manual   ┌────────────────┐
   │  GitHub Actions  │ ───────────────────▶ │ fetch_data.py  │
   └──────────────────┘                      └───────┬────────┘
                                                     │ Bearer token
                                                     ▼
                                          ┌──────────────────────┐
                                          │ OJS REST API (each   │
                                          │ configured journal)  │
                                          └──────────┬───────────┘
                                                     │ JSON
                                                     ▼
   ┌──────────────────┐   fetch JSON     ┌──────────────────────┐
   │ Browser (index.  │ ◀─────────────── │ data/*.json committed│
   │ html + JS)       │                  │ to the repository    │
   └──────────────────┘                  └──────────────────────┘


Update schedule
~~~~~~~~~~~~~~~

The workflow runs:

* **Automatically** at 06:00 UTC on the first day of every month.
* **Manually** from the repository's *Actions* tab (*Fetch OJS Data → Run
  workflow*). A manual run can take an optional start and end date to make a
  custom date range (see :ref:`ojs-custom-range`).

The workflow does not run on every push. Fetching statistics for every journal
is slow, because the OJS statistics endpoints run heavy aggregation queries.

Each snapshot records the time it was fetched (``fetched_at``). The
dashboard's **About** tab shows this as "Data last updated".


Configuration
-------------

Journals are listed in ``.config/api_keys.yml``, one entry per journal:

.. code-block:: yaml

   journal-name:
     key: "your-jwt-api-key"
     site: "https://ojs.example.com/journal-path"
     title: "Journal Display Title"

``journal-name``
   A short identifier. It names the data files (``data/<journal-name>/``) and
   is the value passed to ``--site``.

``key``
   An OJS API token (JWT) for a user account on that journal. It is sent as an
   ``Authorization: Bearer`` header. The account needs enough privileges to
   read submissions and statistics, which normally means a Journal Manager.

``site``
   The base URL of the journal, including the journal path.

``title``
   The name shown in the dashboard.

This file is in ``.gitignore`` and is never committed. In GitHub Actions, the
workflow rebuilds it on the runner from the ``OJS_API_KEYS_YML`` repository
secret, so the keys exist only inside the short-lived job. To set or update the
secret:

.. code-block:: bash

   gh secret set OJS_API_KEYS_YML < .config/api_keys.yml


Running the fetcher by hand
---------------------------

.. code-block:: bash

   pip install -r requirements.txt

   # Fetch all standard date ranges for every journal
   python fetch_data.py

   # Fetch only one journal
   python fetch_data.py --site journal-name

   # Fetch a custom date range
   python fetch_data.py --date-start 2025-01-01 --date-end 2025-12-31

   # Use another config file or output directory
   python fetch_data.py --config /path/to/api_keys.yml --outdir /path/to/output

   # Preview the dashboard locally
   python -m http.server 8000

Then open ``http://localhost:8000``.


Date ranges (snapshots)
-----------------------

Each run collects one *snapshot* per date range for every journal. Users pick
the range from the **Time range** menu in the dashboard.

.. list-table::
   :header-rows: 1
   :widths: 22 22 56

   * - Range
     - File
     - Dates covered
   * - All Time
     - ``snapshot.json``
     - No date filter. Everything OJS has recorded.
   * - Current Year
     - ``current-year.json``
     - January 1 of this year through yesterday.
   * - Previous Year
     - ``previous-year.json``
     - January 1 through December 31 of last calendar year.
   * - Previous Fiscal Year
     - ``previous-fiscal-year.json``
     - The most recent complete fiscal year, September 1 through August 31.
   * - Last 90 Days
     - ``last-90-days.json``
     - The 90 days before the run, ending yesterday.
   * - Last 30 Days
     - ``last-30-days.json``
     - The 30 days before the run, ending yesterday.
   * - Last 7 Days
     - ``last-7-days.json``
     - The 7 days before the run, ending yesterday.

Ranges end on *yesterday* because the OJS statistics API rejects an end date of
today.

Because the workflow runs monthly, the rolling ranges (Last 7/30/90 Days and
Current Year) are relative to the date of the most recent run, not the date you
view the dashboard.

.. _ojs-custom-range:

Custom ranges
~~~~~~~~~~~~~

When ``--date-start`` and/or ``--date-end`` is given (or entered in a manual
workflow run), the fetcher collects **only** that range. It saves the result as
``custom.json`` and adds a **Custom Range** option to the menu, keeping the
existing standard snapshots. Each custom run replaces the previous custom
range.


What the date range affects
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not every statistic can be filtered by date. OJS accepts a date range only on
its statistics endpoints.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Data
     - Effect of the selected range
   * - Publication (article) views
     - Filtered. Only views recorded during the range are counted.
   * - Issue views
     - Filtered. Only views recorded during the range are counted.
   * - New submissions
     - Filtered by the dashboard: submissions whose *date submitted* falls in
       the range.
   * - New issues
     - Filtered by the dashboard: issues whose *date published* falls in the
       range.
   * - Submission list, status and stage counts
     - **Not filtered.** Always shows the current state of all submissions.
   * - Issue list
     - **Not filtered.** Always lists all issues.
   * - User counts
     - **Not filtered.** Always the current number of registered users.


Statistics collected
--------------------

For each journal, the fetcher calls five OJS API endpoints.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Endpoint
     - Date filtered?
     - Used for
   * - ``GET /api/v1/issues``
     - No
     - Issue list and new-issue counts
   * - ``GET /api/v1/submissions``
     - No
     - Submission list, status and stage breakdowns, new-submission counts
   * - ``GET /api/v1/stats/users``
     - No
     - User counts by role
   * - ``GET /api/v1/stats/publications``
     - Yes
     - Views per published article
   * - ``GET /api/v1/stats/issues``
     - Yes
     - Views per issue

The endpoints that are not date filtered are fetched once per journal per run
and reused for every snapshot.

All endpoints are paged in full. The fetcher keeps requesting pages until it
has the total number of items OJS reports (``itemsMax``), so large journals are
not cut off.


Publication (article) views
~~~~~~~~~~~~~~~~~~~~~~~~~~~

From ``stats/publications``, one record per published article:

``abstract_views``
   Views of the article's landing (abstract) page.

``galley_views``
   Views or downloads of the article's full-text files ("galleys"). This is the
   sum of the three counts below.

``pdf_views``
   Galley views of PDF files.

``html_views``
   Galley views of HTML files.

``other_views``
   Galley views of any other file type.

``total_views``
   ``abstract_views + galley_views``.

Each record also stores the article's OJS ID, title, short author list,
published URL, and DOI (if it has one).

OJS produces these counts from its own usage-statistics processing, which
follows the COUNTER guidelines (including filtering of known robots and
double-clicks). The dashboard reports the numbers OJS returns and does not
adjust them.


Issue views
~~~~~~~~~~~

From ``stats/issues``, one record per issue:

``toc_views``
   Views of the issue's table of contents page.

``issue_galley_views``
   Views or downloads of whole-issue files (for example, a full-issue PDF).

``total_views``
   ``toc_views + issue_galley_views``, as reported by OJS.

Each record also stores the issue ID, volume, number, year, identification
string (for example "Vol. 3 No. 2 (2024)"), and URL.


Issues
~~~~~~

From ``issues``, one record per issue: ID, volume, number, year,
identification string, whether it is published, date published, DOI, URL, and
description.


Submissions
~~~~~~~~~~~

From ``submissions``, one record per submission:

* ID
* **Status**: the editorial decision state.
* **Stage**: where the submission is in the workflow.
* Date submitted, date of last activity, and date last modified.
* Published URL (if published).

OJS status and stage codes are translated to labels:

.. list-table::
   :header-rows: 1
   :widths: 10 25 10 25

   * - Code
     - Status
     - Code
     - Stage
   * - 1
     - Draft
     - 1
     - Submission
   * - 2
     - Queued
     - 2
     - Review
   * - 3
     - Published
     - 3
     - Copyediting
   * - 4
     - Declined
     - 4
     - Production
   * - 5
     - Stalled
     - 5
     - Published

The fetcher also counts submissions by status and by stage
(``submission_status_breakdown`` and ``submission_stage_breakdown``). The
**Submission Status** chart on the Overview tab uses these counts.

.. note::

   The submissions endpoint returns only what the API token's user is allowed
   to see. With a Journal Manager token this is normally every submission in
   the journal.


Users
~~~~~

From ``stats/users``: the total number of registered users (*All Users*) and
the number of users in each role (Journal Manager, Section Editor, Assistant,
Author, Reviewer, Reader, Subscription Manager, and so on). A user with several
roles is counted in each role, so the role counts add up to more than the
total.


Summary figures
~~~~~~~~~~~~~~~

Each snapshot includes a ``summary`` block that the dashboard's stat cards use:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Field
     - Meaning
   * - ``total_issues``
     - Number of issues (published and unpublished).
   * - ``published_issues`` / ``unpublished_issues``
     - Issues split by published state.
   * - ``total_submissions``
     - Number of submissions visible to the API token.
   * - ``published_submissions``
     - Submissions with status *Published*.
   * - ``new_issues_in_period``
     - Issues published within the selected range. For All Time, the same as
       ``total_issues``.
   * - ``new_submissions_in_period``
     - Submissions submitted within the selected range. For All Time, the same
       as ``total_submissions``.
   * - ``total_abstract_views``
     - Sum of abstract views across all articles.
   * - ``total_galley_views``
     - Sum of galley views across all articles.
   * - ``total_pdf_views`` / ``total_html_views`` / ``total_other_views``
     - Galley views split by file type.
   * - ``total_view_count``
     - Total article views (abstract plus galley). Shown as **Total Views**.
   * - ``total_issue_views``
     - Sum of issue views (table of contents plus issue galleys).
   * - ``total_users``
     - Total registered users.


Using the dashboard
-------------------

Use the buttons at the top to pick one journal or **All Journals**, and the
**Time range** menu to pick a snapshot.

Single journal
~~~~~~~~~~~~~~

**Overview**
   Stat cards for submissions, issues, total views (with PDF views), abstract
   views, and users. For ranges other than All Time, the submission and issue
   cards show *new* items in the range. Also shows charts of the top
   publications by views, issue views, and submission status.

**Publications**
   Every article with its abstract, galley, and total views for the selected
   range. Titles link to the published article.

**Issues**
   Every issue with total, table-of-contents, and issue-galley views.

**Submissions**
   Every submission with its status, stage, date submitted, last activity, and
   a link if published. Not affected by the time range.

**Users**
   User counts by role. Not affected by the time range.

**About**
   The journal's URL and when its data was last updated.

All Journals
~~~~~~~~~~~~

Combines the selected range across every journal: number of journals, number of
publications, total views (with PDF views), abstract views, and new
submissions. It also shows a chart of the top journals by views and one
searchable table of publications from all journals, which can be filtered by
title, author, or journal.


Data files
----------

.. code-block:: text

   data/
   ├── sites.json                  # Index of journals and their available snapshots
   ├── <journal>.json              # Copy of the All Time snapshot
   └── <journal>/
       ├── snapshot.json           # All Time
       ├── current-year.json
       ├── previous-year.json
       ├── previous-fiscal-year.json
       ├── last-90-days.json
       ├── last-30-days.json
       ├── last-7-days.json
       └── custom.json             # Only after a custom-range run

``sites.json`` lists each journal's name, title, directory, and snapshots
(label, file, start date, end date). The dashboard reads it first to build the
journal buttons and the Time range menu.

Each snapshot file has this structure:

.. code-block:: json

   {
     "site_name": "journal-name",
     "site_title": "Journal Display Title",
     "site_url": "https://ojs.example.com/journal-path",
     "date_start": "2025-01-01",
     "date_end": "2025-12-31",
     "fetched_at": "2026-10-01T06:12:34Z",
     "issues": [],
     "submissions": [],
     "submission_status_breakdown": {},
     "submission_stage_breakdown": {},
     "user_stats": [],
     "publication_stats": [],
     "issue_stats": [],
     "summary": {}
   }

Because the files are committed, the repository's git history is a monthly
archive of each journal's statistics.


Reliability and error handling
------------------------------

* Requests to the statistics endpoints may take up to 120 seconds. Other
  endpoints may take up to 30 seconds.
* Timeouts and connection errors are retried twice, waiting 10 and then 20
  seconds. HTTP errors (4xx/5xx), such as an expired API key, are not retried.
* If a request still fails, the fetcher **keeps the existing snapshot file**
  rather than replacing it with empty data. A journal with a temporary outage
  keeps its previous figures (check ``fetched_at`` or the About tab to see how
  old they are).
* If one journal fails, the other journals are still fetched.


Limitations
-----------

* Submission, issue, and user data show the current state at fetch time. They
  are not historical, even for past ranges such as Previous Year.
* Data is only as fresh as the last workflow run (monthly by default).
* View counts come from OJS's own statistics. They depend on OJS having
  processed its usage logs for the period, so very recent days may be
  incomplete.
* Journals whose API token lacks the needed permissions, or whose statistics
  are not enabled, show zero or empty values.
