========================
Minting DOIs in Crossref
========================

--------------------
Pending Publications
--------------------

In some cases, our stakeholders need a DOI **before** the item is formally published or available online.
Crossref supports this through a special record type called a
`Pending Publication <https://www.crossref.org/documentation/schema-library/markup-guide-record-types/pending-publications/>`_.
A Pending Publication is a temporary Crossref record that allows us to register a DOI early, with minimal metadata,
while signaling to readers that a final version is forthcoming.

Pending Publications appear in Crossref with a green banner reading:

    **“Manuscript has been accepted.”**

This banner communicates that the content is not yet fully published but has been accepted by the publisher.

Why use a Pending Publication?
------------------------------

Use a Pending Publication when:

- A DOI is needed in advance for grant reporting, early citation, or repository workflows.
- The item has been accepted but is not yet publicly available.
- Metadata is incomplete (e.g., volume, issue, page numbers, final URL).

Crossref allows you to register the DOI immediately and update the metadata later once the final version is ready.

Creating a Pending Publication
------------------------------

To create a Pending Publication, you:

1. Use the ``pending_publication`` work type in your Crossref deposit.
2. Supply the minimum required metadata:
   - Title
   - Authors
   - Acceptance date
   - Intent-to-publish statement
   - DOI you are minting
3. Deposit via your normal Crossref workflow (XML upload, API deposit, or system integration).

Once deposited, the DOI resolves to a basic record with the green “accepted” banner.

Updating a Pending Publication After Formal Publication
-------------------------------------------------------

**Crossref does not have a special “update” operation.**
When the work is finally published, you simply **deposit new metadata to the exact same DOI**.
Crossref will then replace or expand the metadata accordingly.

Typical metadata added at this stage includes:

- Publication date
- Final title (if changed)
- Journal, volume, issue, and pages
- Final landing page URL
- Abstract
- License
- Funding and affiliation details
- References

This update creates the official published version of the DOI.

Withdrawals and Corrections
---------------------------

The behavior differs depending on whether your organization uses **Crossmark**.

For Crossmark users
~~~~~~~~~~~~~~~~~~~

If the Pending Publication needs to be **withdrawn**, you may include a
**Crossmark scholarly update assertion**, such as ``withdrawal``.

This tells Crossref to automatically:

- Change the green banner to a **red “Accepted manuscript has been withdrawn”** banner
- Record the update in Crossmark metadata
- (Optionally) link to a new DOI representing the update/notice

This is the recommended approach if your workflow includes Crossmark.

For organizations *not* using Crossmark
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Without Crossmark, Crossref cannot automatically change the green Pending Publication banner.
Even if you redeposit metadata, the record will continue to display:

    **“Manuscript has been accepted.”**

Therefore, if you withdraw a Pending Publication you **must** communicate this manually in the
``<intent_to_publish>`` field.

Example:

::

   <intent_to_publish>
       This item has been withdrawn by the authors and will not be published.
   </intent_to_publish>

This ensures that downstream users and metadata consumers understand the withdrawal even though the banner will not change.

Sample Pending Publication
--------------------------

A sample XML document will look like this:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <doi_batch version="5.3.1"
               xmlns="http://www.crossref.org/schema/5.3.1"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
               xsi:schemaLocation="http://www.crossref.org/schema/5.3.1
               http://www.crossref.org/schema/deposit/crossref5.3.1.xsd">

      <head>
        <doi_batch_id>pending-pub-example-001</doi_batch_id>
        <timestamp>20250101000000</timestamp>

        <depositor>
          <depositor_name>Your Organization Name</depositor_name>
          <email_address>contact@example.org</email_address>
        </depositor>

        <registrant>Your Organization Name</registrant>
      </head>

      <body>
        <pending_publication>

          <titles>
            <title>Example Title of a Pending Publication</title>
          </titles>

          <contributors>
            <person_name sequence="first" contributor_role="author">
              <given_name>Alice</given_name>
              <surname>Smith</surname>
            </person_name>
            <person_name sequence="additional" contributor_role="author">
              <given_name>Bob</given_name>
              <surname>Johnson</surname>
            </person_name>
          </contributors>

          <acceptance_date>
            <month>01</month>
            <day>10</day>
            <year>2025</year>
          </acceptance_date>

          <intent_to_publish>
            This manuscript has been accepted and is awaiting publication.
          </intent_to_publish>

          <doi_data>
            <doi>10.1234/example.pendingpub.001</doi>
            <resource>https://example.org/pending/example.pendingpub.001</resource>
          </doi_data>

        </pending_publication>
      </body>

    </doi_batch>
