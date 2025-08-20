======================
Minting ARKs with EZID
======================

What is an ARK?
===============

An **ARK (Archival Resource Key)** is a type of persistent identifier designed to provide long-term access to digital information. ARKs are used by libraries, archives, data centers, and publishers to ensure that digital objects remain accessible over time, even if their storage location changes.

EZID and ARKs
=============

`EZID <https://ezid.cdlib.org/>`_ is a service provided by the California Digital Library that enables users to create and manage persistent identifiers, including ARKs and DOIs. EZID provides a straightforward API for minting and updating ARKs, making it easier for institutions to integrate persistent identifiers into their digital asset management workflows.

Why ARKs are Important
======================

ARKs are critical for:

- **Persistence**: They remain stable even when digital objects move or change over time.
- **Interoperability**: ARKs can be resolved globally using services like N2T.net.
- **Curation**: Metadata embedded in ARKs, particularly using the `erc:` element, helps describe and manage resources over time.
- **Transparency**: ARKs can convey information about the resource's provider and its status through qualifiers and metadata.

The ERC Element
===============

EZID supports metadata using the `erc:` (Electronic Resource Citation) tag, a simple and standardized schema used to describe digital resources. The `erc:` format is often used in ARK records to provide essential citation metadata. 

Typical ERC elements include:

- **who**: The agent or creator responsible for the resource.
- **what**: The title or name of the resource.
- **when**: The date associated with the resource.
- **where**: A pointer to the resource’s location, often a URL.

Example::

    erc.who: Mark Baggett
    erc.what: Avalon Metadata Mapping Guide
    erc.when: 2025-08-01
    erc.where: https://example.org/avalon/mapping

EZID allows these `erc:` fields to be updated over time, supporting good stewardship and curation practices for digital collections.

What To Do When You Have Limited Metadata
=========================================

Occasionally, we may have an issue where we are missing a certain :code:`who, what, when, or where` value.  In these cases, do the following.

---
Who
---

:code:`Who` should be similar to :code:`dc:creator`. When we don't know, put :code:`Unknown`. If we aren't sure but it's done by someone at a 
specific institution, list the institution.

----
What
----

:code:`What` should be similar to :code:`dc:title`. We need this value to help us identify what was originally described. This value should always
be descriptive even if it's not a title. For instance, it could be a filename or something else. If needed, it is also valid to concatenate multiple
values together like :code:`title - filename.tif`.

----
When
----

:code:`When` should be similar to :code:`dc:date`. When we don't know, put :code:`Unknown` or an edtf value approximating the date.

-----
Where
-----

:code:`Where` should be the url of the resource online. This will normally be a work page, but could also be another form of url.

Generating ARKs Programmatically
================================

To generate ARKs in batches, you can simply create a CSV with your standard erc fields.  Then you can run code like below that will generate each ARK and record them on
a spreadsheet:

.. code-block:: python

    import csv
    import requests
    import os


    class EZIDARKGenerator:
        def __init__(self, shoulder_url='https://ezid.cdlib.org/shoulder/ark:/81423/d2'):
            self.url = shoulder_url
            self.headers = {'Content-Type': 'text/plain'}
            self.auth = (os.getenv("EZID_USER"), os.getenv("EZID_PASSWORD"))
            self.completed = []
        
        def create_metadata(self, who, what, when, where):
            """Create metadata content string for EZID request.
            
            Args:
                who (str): the agent responsible for the resource — typically the creator, author, or contributor.
                what (str): the title of the work
                when (str): the date of publication for the original work
                where (str): URL or current location of the resource

            Returns:
                dict: The data formatted for the Post and Creation of the Ark
            """
            return (
                f'erc.who: {who}\n'
                f'erc.what: {what}\n'
                f'erc.when: {when}\n'
                f'_target: {where}\n'
                f'_status: reserved\n'
            )
        
        def create_ark(self, who, what, when, where):
            """Create a single ARK identifier.
            
            Args:
                who (str): the agent responsible for the resource — typically the creator, author, or contributor.
                what (str): the title of the work
                when (str): the date of publication for the original work
                where (str): URL or current location of the resource

            Returns:
                dict: Data sent to the ARK with the ARK returned
            """
            metadata_content = self.create_metadata(who, what, when, where)
            data = metadata_content.encode('utf-8')
            
            response = requests.post(self.url, data=data, headers=self.headers, auth=self.auth)
            # https://n2t.net/ark:/81423/d2tg6j
            full_message = response.content.decode('utf-8')
            ark = ""
            if "success" in  full_message:
                ark = f"https://n2t.net/{full_message.split(' ')[-1]}"
            return {
                'who': who,
                'what': what,
                'when': when,
                'where': where,
                'message': full_message,
                'ark': ark,
            }
        
        def process_csv(self, input_file):
            """Process CSV file and create ARKs for each row.
            
            Args:

                input_file (str): The CSV that contains your ARK information with appropriate headings.
            """
            with open(input_file, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                
                for row in reader:
                    result = self.create_ark(
                        row['who'],
                        row['what'],
                        row['when'],
                        row['where']
                    )
                    self.completed.append(result)
        
        def save_results(self, output_file):
            """Save completed results to CSV file."""
            fieldnames = ['who', 'what', 'when', 'where', 'message', 'ark']
            with open(output_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in self.completed:
                    writer.writerow(row)
        
        def run(self, input_file, output_file):
            """Main method to process input and save results."""
            self.process_csv(input_file)
            self.save_results(output_file)
            return self.completed


    if __name__ == "__main__":
        input_csv = "quick.csv"
        output_csv = "output3.csv"
        generator = EZIDARKGenerator()
        results = generator.run(input_csv, output_csv)
        print(f"Processed {len(results)} records")