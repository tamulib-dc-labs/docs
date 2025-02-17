===========================================
RDFizing DSPACE Works to Generate Manifests
===========================================

irIIIFService requires RDF graphs in order to generate manifests for items in DSPACE. This document describes how to get
a list of handles and generate turtle for irIIIFService.

-------------
Making a List
-------------

Assuming you have a DSPACE collection and want to create RDF for everything in it, you can use Python to get a list of
handles. Just specify the collection object you want to use and where to write the handles like on lines 48 and 49.

.. code-block:: python
    :emphasize-lines: 48-49

    import httpx
    from rdflib import Graph, Namespace, URIRef


    class Namespaces:
        def __init__(self):
            self.dc = "http://purl.org/dc/elements/1.1/"
            self.dcterms = "http://purl.org/dc/terms/"
            self.void = "http://rdfs.org/ns/void#"
            self.rdf = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
            self.xsd = "http://www.w3.org/2001/XMLSchema#"
            self.bibo = "http://purl.org/ontology/bibo/"
            self.foaf = "http://xmlns.com/foaf/0.1/"
            self.dspace = "http://digital-repositories.org/ontologies/dspace/0.1.0#"


    class DspaceItem:
        def __init__(self, uri):
            self.uri = uri
            self.namespaces = Namespaces()
            self.g = self.__get_graph()

        def __get_graph(self):
            r = httpx.get(self.uri, timeout=60)
            try:
                if r.status_code == 200:
                    g = Graph()
                    g.parse(data=r.content, format='turtle')
                    return g
                else:
                    raise Exception(f"Failed to download {self.uri}. Status code: {r.status_code}")
            except Exception as e:
                raise Exception(f"Failed to download {self.uri}: {e}")

        def get_children(self):
            return [str(o) for s,p,o in self.g if p == URIRef(f"{self.namespaces.dcterms}hasPart")]

        def prep_for_rdfizer(self, output):
            children = self.get_children()
            handles = [f"{child.split('/')[-2]}/{child.split('/')[-1]}" for child in children]
            with open(output, "w") as fh:
                for handle in handles:
                    fh.write(f"{handle}\n")



    if __name__ == "__main__":
        x = DspaceItem(uri="https://oaktrust-pre.library.tamu.edu/server/rdf/handle/1969.1/86434")
        x.prep_for_rdfizer("maps.txt")

-----------------------------------------
Copying your List and a Process to DSPACE
-----------------------------------------

In order to script with rdfizer, you need the DSPACE CLI. The DSPACE CLI is usually at :code:`/dspace/bin/dspace` but
not in PATH. The running container also likely does not have a text editor that you can use.

To create a bash script and get your files to the container, you can use :code:`cat`.  This isn't ideal, but you can
write a shell script like :code:`process.sh` by running :code:`cat >> process.sh` then pasting this:

.. code-block:: bash

    #!/bin/bash

    # Check if a filename was provided
    if [ "$#" -ne 1 ]; then
        echo "Usage: $0 <input_file>"
        exit 1
    fi

    INPUT_FILE="$1"

    # Check if the file exists
    if [ ! -f "$INPUT_FILE" ]; then
        echo "Error: File '$INPUT_FILE' not found!"
        exit 1
    fi

    # Read the file line by line and execute the command
    while IFS= read -r line; do
        # Trim any leading/trailing whitespace
        VALUE=$(echo "$line" | xargs)

        # Skip empty lines
        if [ -n "$VALUE" ]; then
            echo "Processing: $VALUE"
            /dspace/bin/dspace rdfizer -i "$VALUE"
        fi
    done < "$INPUT_FILE"

You can then save the file by pressing :code:`CTRL + D`.  You'll need to make sure you can execute the file so make sure
you have execute or give yourself full permissions by :code:`chmod 777 process.sh`.

Now, you'll need to get your files there too.  You can do the same process like :code:`cat > files.txt`, pasting your files
you created earlier, and then running like :code:`./process.sh files.txt`.
