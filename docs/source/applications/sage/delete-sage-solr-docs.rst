=============================
Deleting Items from SAGE Solr
=============================

SAGE stores documents based on the id set in the Reader and Writer of the application. This is often based on an id of
the original source application. Occassionaly, that id pattern will change.  When you do an update, it will create brand
new records.  SAGE has no mechanism on how to delete the old duplicate records. This document explains how.

--------------------
A Solr Delete Script
--------------------

On your local machine, write a file like the one below.  It's usually better to write locally as we cannot guarantee our pod will
have a text editor (or one where I have all the commands memorized).

.. code-block:: shell

    #!/bin/bash

    # Configuration
    SOLR_URL="http://localhost:8983/solr/sage-core"
    ID_FILE="ids.txt"

    # Optional: check the file exists
    if [[ ! -f "$ID_FILE" ]]; then
      echo "Error: file '$ID_FILE' not found"
      exit 1
    fi

    count=0
    errors=0

    while IFS= read -r id || [[ -n "$id" ]]; do
      # Skip blank lines
      [[ -z "$id" ]] && continue

      response=$(curl -s -o /dev/null -w "%{http_code}" \
        -X POST \
        -H "Content-Type: application/json" \
        "${SOLR_URL}/update" \
        --data-raw "{\"delete\": {\"id\": \"${id}\"}}")

      if [[ "$response" == "200" ]]; then
        echo "Deleted: $id"
        ((count++))
      else
        echo "ERROR ($response): $id"
        ((errors++))
      fi

    done < "$ID_FILE"

    # Commit the deletes
    echo "Committing..."
    curl -s -X POST \
      -H "Content-Type: application/json" \
      "${SOLR_URL}/update" \
      --data-raw '{"commit": {}}'

    echo ""
    echo "Done. Deleted: $count | Errors: $errors"

Save the file something like :code:`delete_docs.sh`. Then:

.. code-block:: shell

    chmod +x delete_docs.sh

Notice, that the file references a text file called ids.txt.

Also create a file with all the ids you want to delete on separate lines.

---------------------
Copying to the Server
---------------------

Copying with :code:`kubectl` is easiest.  Assuming you have it installed and set up (see instructions elsewhere here),
switch contexts:

.. code-block:: shell

    kubectl config use-context prod-apps-cluster

Then copy files to the pod where you will run.  You'll need to identify pod name with :code:`kubectl` or via Rancher directly.

.. code-block:: shell

    kubectl cp ids.txt sage-solr-7fc7c9986b-tmf7k:/tmp -n sage
    kubectl cp delete_docs.sh sage-solr-7fc7c9986b-tmf7k:/tmp -n sage

----------
Run Script
----------

You can run the script locally with :code:`kubectl`, but assuming you've copied like above, you can just connect to the
pod using your method of choice and run it:

.. code-block:: shell

    ./delete_docs.sh

If successful, this will look like this:

.. code-block:: shell

    solr@sage-solr-7fc7c9986b-tmf7k:/tmp$ ./delete_docs.sh
    Deleted: Mi0yNWRkNDVmYS04NWZjLTRiYjMtODE0ZS05NDQzYzg2ZWZlM2Y=
    Deleted: Mi1kNzk4NjhjOS0yZDA2LTQ0M2UtYTBlYy1lM2E5NmFmZjk3ZTM=
    Deleted: Mi1lZmZkYjMxMS1mM2VlLTQ3MTItYjNmZS01MjgyZDkxZmNkYTQ=
    Deleted: Mi0xODc1N2FlZi0wN2JkLTQ1ZWYtYWYzNS1iMjFmZjJiNDM2OTM=
    Deleted: Mi03OTI0ZWY0OS01ODM0LTRhNWItYTE5OS0wMWVmYWNhYjcyOTg=
    Deleted: Mi02N2RmZTkzNi1hNTI0LTRlMWYtYmU1Mi0yZWQzMzI2NGVjZjM=
    Deleted: Mi1jY2Q4OGU4Mi1jNGE3LTQ3NTgtOWMzZC05OGY4NTg2MmViNDY=
    Deleted: Mi0zNmJmODBkNC1iMTFhLTRlNWQtYmNhMi03NGE5ZmY5YmEyYzU=
    Deleted: Mi00YzI1MTEzMy02YmI3LTQ5YmQtOTcwMi05Njk4ZjlkMTNmOWE=
    Deleted: Mi01NTk4NjNhYi0wNzkzLTQxMzctYjJkOC1jZDhkZjllZjhmMjk=
    Deleted: Mi05ZmRjZTMzZS02OWIzLTRjNjMtYmViZC1lNTJlNDNiYmNkZmU=
    Deleted: Mi03YjBlODcxYi1kOTEzLTQ4MmYtYjkxYy0wYmQ1N2EzNzcyZDg=
    Deleted: Mi0zZjgyNWU4NS03N2ViLTQxMDUtYTcxOC1iNTk0NGI5MmEwZTg=
    Deleted: Mi0xNTk3OWFiMS1hMTMzLTRkZTYtOWNlMS02NGRiMjNmNWFlMzE=
    Deleted: Mi1iYjZjZWE4Zi05YjZlLTQwZTAtOTEzMi1lNzg4MTg4MGRmYzc=
    Deleted: Mi05ZjkyNzQ1ZC02YTNhLTRmOWQtYjQ2ZC0yYzVjMTE5NTI2ZGU=
    Deleted: Mi1hOTlkNTA0ZS0zODllLTQ2ZTgtODhmNC1hMjU0YTlhMjdlYmM=
    Deleted: Mi0xNDAwMTJlOC0zMjhkLTRjYTUtYjEwZS1lYjQzNWY1ODJkYjE=
    Deleted: Mi1mZWRmOWI4OC1hNTU0LTQxZGItOWMwOC1hYWYwZGNjZWY3ZTY=
    Deleted: Mi03OWEyZWZhOS0zMTJiLTQ1ZGUtYmM2NS00ZmI0ZWU4OTA1YWY=
    Deleted: Mi1mYTYzM2FiMy1kYzM4LTQ3ZmMtOWE4ZC05Y2FjODQxNjc1MjI=
    Deleted: Mi03MWMzMDBhMi0wZDIyLTQ3YWEtYWJmYS1mZWRkNDcwZjFhNWU=
    Deleted: Mi1mMjI1MTVlNS03ZmNjLTRiNzktYWY4ZC04OWZjYmYzNmVmNTk=
    Deleted: Mi04Y2MwNGNkNC1lNDNhLTRlN2EtOTEyZi1hNTA2YTkxNTlkNzE=
    Deleted: Mi03Mzc2M2RkNy03YzA0LTRjYzAtOGNkMS1kNDk5NjdmMWFiYjc=
    Deleted: Mi03NzMwMmFlZS03ZWZjLTQ2OGEtYTViYy04ZTFkNDAxOTJhMzI=
    Deleted: Mi0xOTM3ZmE2Yi1kMzYwLTRlZjctOTA2My1mZTZiNjc3ZWFkMDk=
    Deleted: Mi01MTgzMGI0MS00NzMzLTQ0OTItYjE2YS1iMDMzYmI0ODFhZjQ=
    Deleted: Mi1hNDU0NjMxZS1kYjY1LTRiNjgtYWEyMC0yZWEwMzZjZjViMDA=
    Deleted: Mi1hNGI3MjA0MC0zZDUwLTRkZWQtODYwMi0zYzUxODA1NDhiMDc=
    Deleted: Mi1lZjg0NzVlZi0yMDU1LTQ0OTYtOGRkYy03YzdhMDIzYjM5ZDI=
    Deleted: Mi00ODkwMmMwNC0zOTkzLTQwODQtOGNjZS1lMzFkZjUwNjkyMGE=
    Deleted: Mi1kMWM0ZGE1ZS01YjZjLTRkZDYtYWEzOS04OTY0NTU1NGIzN2E=
    Deleted: Mi1lNjdkMWRhMS1kOWU5LTRlNTQtODQyZi0zOTIyNmE2ZWU5N2Y=
    Deleted: Mi1lMDJhMDEyYi1lNzBjLTRhYzQtOTEyNi02Y2UwMWVkNTIwYTA=
    Deleted: Mi1hOTJlNjYxMy1iMDVkLTRkZjktODNkNi0zMGNjOThkZTFhYzg=
    Deleted: Mi01ODJhYjliZC0xMTM0LTQ1ZGYtYTA0NC00MjAxOWZhMDhlZTQ=
    Deleted: Mi1kMGQwMTQzZC0wNjUxLTQ0NDEtYjdmZC0zNDQ0NTQ0YjJmMWE=
    Deleted: Mi0yM2FiNmEwMy01M2NkLTRlMGItODA1Yy03ZTEyOTkwMTc2M2E=
    Deleted: Mi01YjQ2ZmVhZS0xM2U3LTRhOWMtYWQ0NC0wNjA4ZTlkNGJiMWQ=
    Deleted: Mi1jODk1Mjg4Mi05MGM4LTQ0OTYtYjRhOC0wMWI1MjJmNzZlNWY=
    Deleted: Mi1jMDEwZjVkMS00OGVhLTRiOGQtOTg1Zi1kNzZjMzAxZmQzOWQ=
    Deleted: Mi0zYzdkNmQzZS04NWYzLTRhZjAtYjYyOC1mZWM3ZWU0ZWY3NWQ=
    Deleted: Mi0xNTJmMzEwZC1lMjIxLTQzMDktOGU2Yy0wNDJiODMxN2IwYzY=
    Deleted: Mi1hYzdlMWQ5NS1jOTM1LTQ2OGEtOGJlYy0xNmUwOGNkOGExN2Q=
    Deleted: Mi00Nzk2M2FiMi0xNWVlLTQzYTktYTk2Ni1hNTQwNDUxNDI0NDM=
    Deleted: Mi0zMzRlNjc2NS1kOWE0LTRhZjEtOTdhYS0zMTIzMGZlNWE1MWQ=
    Deleted: Mi01OTk4MWU4OC0wMjY2LTQ1MWQtOGVhZi0xMmZlNzA2ZTY2OWM=
    Deleted: Mi1iYWQ3OGVmNy1jZGY1LTQxMWEtOTgzMS1mNjdkN2Y3Njg2MmM=
    Deleted: Mi01M2FmMjQzYy02YjY3LTRhZWMtYWI0YS01NTE2MjNjOTQ0MWE=
    Deleted: Mi1jN2MxNGViNC05MTg3LTRlYmYtYjc2OS1hOGIzZDk3YjVhNmU=
    Deleted: Mi01YTk3MTM2MC1mMWI5LTQ2ODQtYjJkOS04ZjEzN2Y1NDlkNzY=
    Deleted: Mi1iZjRkNmFhNC00NjIwLTRlODQtODBmYy1lM2MzZGEwOWNmNzc=
    Deleted: Mi1kNzBlMWQyZS04OWU0LTRhODMtYjMzOC03MjlmZjQ0NTRjYTg=
    Deleted: Mi04ZmQ2YWVhMC0yNGMyLTQ5MDAtODRiOS1kOTM3YjZiNWU3ODM=
    Deleted: Mi1iOGQ3NGVkNy1kODY5LTRlMzgtOGU1MS1lMWMxNjcyZGRlNTE=
    Deleted: Mi1hYWUzNjdhNC1iNjk0LTQxNjktYjcwMC00NzRjMDliNDc3ZDM=
    Deleted: Mi1kNWY3YTA4OC02NjVjLTRhZDgtODg0MS00OTg3OGMzNjljM2I=
    Deleted: Mi00ZGExMTc5YS0zNzc0LTRlMzUtODIxOS1kNzViZDI2ODVmNzM=
    Deleted: Mi1hZmQ2OWI1Yy1lODdlLTQ5OTYtYmNmMC1iNjgyNGY2NDhhZGQ=
    Deleted: Mi0xZGM1NmI3Zi0xOGU2LTQ5NjQtODhmMy1mYzZiOWY1ZDA2YTQ=
    Deleted: Mi02OTE0ZWQ4OS1hNzk2LTQ5ZDEtYjA4ZS1jYzRmY2JjYTQ5ZjA=
    Deleted: Mi1mMmQ3Njk3YS1hMjBhLTQ5ZGMtYjAyZS02MWQ5NTEwNTcwNmU=
    Deleted: Mi01Njc4ZDUwNi0yZjc2LTQwZWEtYmI5Yi0zOWQ0ZGZiMTU2ZWM=
    Deleted: Mi01ZjE3ZGY0Yy0zYTU3LTQ2MTItOTI4Ny0wYmI1OGJmMGVmMDk=
    Deleted: Mi02M2VlNzU5Yi1mNGZlLTRmZjItYWZlZC02ZTdhY2M5ZDAzYzI=
    Deleted: Mi05ZGI4NmJhYy1kNGQ0LTRiOGUtODkxMy04YjUyMjIwOGZmNmY=
    Deleted: Mi0wM2NiZmMwYy02OGE2LTRkODItODQyNi02N2VkNGEyODk1MWQ=
    Deleted: Mi00MGUwOWM3Zi1hZGY1LTQyMTItYmM3ZC1kZjllNTA0NWM4NTY=
    Deleted: Mi04OWQ4ZjcwZS00ZGMzLTRjZGEtYWE3MC02MjQwMTVkM2YwYmY=
    Deleted: Mi1mNGE4ZmZhZi00ZDY4LTQxNzUtOWE0NS1hM2VmZGQ5OTQwYzY=
    Deleted: Mi01NmUzZjk0MS0xYzg3LTRkZWYtOGYzZi0yYmEzZWU4ZGE0ZjQ=
    Deleted: Mi1iZDJlZTFmMC1lOThmLTQ1MjgtODU4OC03YzY4M2QzNzBjOGE=
    Deleted: Mi02ZDY4MmJjMy1jNzQwLTQwMTItYWJjZi00ZGMyNWNhNGNlZTU=
    Deleted: Mi01ZGI4NjkxMS1lZWMxLTQzYTEtYjUxZi0zZTZmODM3NWJlZDI=
    Deleted: Mi0yZmIyYTZkNS02M2Q4LTRiZTMtOWI4YS05NjI4ODNmZDBhMmI=
    Deleted: Mi00ODQyMjcwMy01M2FiLTQ2NTMtOTBlZi1kMDEzNTM2MjIxNTY=
    Deleted: Mi1kOGY4NzhkOC0wZWJmLTQ1YWMtYmYwOC0zMDMzYTk4MTVjZTc=
    Deleted: Mi04MzAzZTg0Ni05ODVlLTQ4NmQtODhlOS05NDljYTY3OWZlZDY=
    Deleted: Mi00NDU2M2JjOC1lMjQ0LTQ2ODYtYmNiMS1iMDZjZmE3N2NiMWQ=
    Deleted: Mi1jYTg5MzAxYy03ZDNlLTQ5MDYtYjlhNS00MjMzMWUzNTFlZDE=
    Deleted: Mi02ZGViOTk3Ni1mMDFmLTQ5OWYtOWJmNC1kYTE1NTBmNDc4NTA=
    Deleted: Mi0yYjFlMTU4MC05Y2I2LTQ4MDctYTUyMi1lZTNhOTZlNzdkYjU=
    Deleted: Mi0zMWU3NWIzMS1lZGJiLTRlYzgtYTdhOS00ZTQwYzlmOTM2Y2Q=
    Deleted: Mi1jNjA5MTkxMi03NDg4LTRjNzYtODk3YS0zYWQyMTQ5NzE1NjI=
    Deleted: Mi03YmEzNGY2OS05N2ZkLTRmNjUtYjYxMS1mM2UwNTFmZDAxMDY=
    Deleted: Mi1lYTZiOGFkZS1jZmMxLTRiNDEtYmY5ZS02MzIzMDQ1YTk3Zjc=
    Deleted: Mi01M2JjNmJmYi01NGQxLTQxNDQtOTAyZS05ZTM1ZjcxNWVlMDg=
    Deleted: Mi0xZjY4OWNkZC04NTQ4LTRmNDMtOWJmMS03YjFlYjMzZmM0MzA=
    Deleted: Mi0xMzQ4MzA0ZS1mNTAyLTQxODMtOWJiYi1kNTIwZDIxNTZmZjM=
    Deleted: Mi0yNGM3MWQwZC05MjE1LTQ0ZTAtYWJiZS0zZGFjZDRmMjU1MTI=
    Deleted: Mi04ODdmNWEzNy1kMTdjLTQyY2YtODY5Mi04NzllM2I4NGNkY2Y=
    Deleted: Mi0xZjg4YzFkMy1kNmYzLTQ1YTMtODgwNy05OGQ5NWVjN2Q0NWM=
    Deleted: Mi02ODExZTRkZi1mNTg4LTQ3NjctYWMzYy1jNWM3MmY5NDUxNzE=
    Deleted: Mi00NjUxNzkxZC0zODI0LTQ4ZGQtYmZiMy1jYmM5ZjViODNjMWY=
    Deleted: Mi1jYzljZGFjYy04NjdiLTRjMzYtODlhMy01Mjk3ZmNlYTc2ZGY=
    Deleted: Mi02ZmVmMWU3MS0yMjg2LTQ3OTEtODNmNC01ZTk2YjY2NTRmZTI=
    Deleted: Mi03ZmE2MzkyMC0zOWE4LTQwMDgtYjQ1OS02MTVjYTE2ZjUyODY=
    Deleted: Mi1jODNjNzAzMC04NjBlLTRlMzUtYmQwNS0yMDUyMzc5ZWEyMmM=
    Deleted: Mi1mZmE5NWNjNy03ZjAzLTQzNDQtODQzMC1hNDBjNzg3MGRiZjI=
    Deleted: Mi03OTRmNWEzZS1hYjllLTRlNmYtOTRkNi1jNzE4MmM1ODg2OTc=
    Deleted: Mi04ZDBjZjQyYS05MjFkLTQxNDMtOWRjOC00NTJiNjZhY2ZkMTE=
    Deleted: Mi04YTVlYzE1OC1mZTAwLTQzMGYtOTc4YS02MzE1MTNmMmIyYzI=
    Deleted: Mi1jYzMxZTI4YS02ZjE3LTRiMDMtOTJmYS1hNWI4YmNiMDgwNGM=
    Deleted: Mi0yYThhZmY5My1kMDVjLTQwZDItYTZiNS0yNDczZjk1MzdhNTA=
    Deleted: Mi0zYThmYTBlYS03NTY3LTQ3YTEtYTBjMy01Y2M2Y2E2ZDE3MGM=
    Deleted: Mi1hMDk5OGQ3Ni0xOGIyLTRlMjItYjZmYi02ZGIzZDU3MGQwZjY=
    Deleted: Mi1mNDg1YjMzMi1hMzAxLTQ5OGQtYmUyNS04YWYwYmMyZTExZDQ=
    Deleted: Mi1mMzNiNGI2Mi1hNmExLTQyZjQtOTEwMy0xMmUyODRkMjAyNDY=
    Deleted: Mi01MWQ1YWYyZi1hYjdhLTQwMzktYTM3YS05MjNiY2Y2MzcxZTc=
    Deleted: Mi1lNzBhNzdjMi1kMDRkLTRmMGMtOWUzMy0yOGYzNWUxOTUwMWM=
    Deleted: Mi03MzNlMDE1OC0zNDc5LTQ5ZmEtYTk0NS1lY2VjMGQ0ZDhhNDU=
    Deleted: Mi04ZTdlNjJlNi1hYWI4LTQxNzUtODkxZC05OTZjZDlmMjE3NzU=
    Deleted: Mi05OGE1OWE4MS00MTY1LTQ5YjktYjgwZi02Mjg4YzAyYzQ2NjQ=
    Deleted: Mi1lMmNmYzBkYi1mYjI2LTQ0NDUtYjVmMy0wYWJiM2E3MmFjZTY=
    Deleted: Mi1jYzhiNzk2ZC1lMTE0LTRkNDctOGU0OS1hMGU1ZTVkZjQ5NTI=
    Deleted: Mi1mYzM0NTEyMS05Y2ZhLTQ0MGYtOTYwOC02ODc4MjNiZDQ3ZTE=
    Deleted: Mi1iOWI1M2Q0OC00ODc5LTRiZDYtYWY0NS01ZTk2ZmU3ZWMzZmQ=
    Deleted: Mi1iZDg5YWNlNS03MjMwLTQzMDktYjM3MC1mZGQxZTlmMzA2ZWE=
    Deleted: Mi1hNTRjNTU2YS00YjFkLTRjZTctYjA4Yy0zYzE2MzMzZDZhNTg=
    Deleted: Mi1iYTFhOTMxZS0yY2VkLTQ5OGYtYmUxNy1jYWRjYTY2NGY2YjM=
    Deleted: Mi1lZjUzNGQ1OC01YzY2LTQ5MmUtYTE2MC02Yzc5N2FjMGIwMjU=
    Deleted: Mi1mNTVlMDY2NC1jOTA3LTRkOTYtYjMxZC0xY2FkNjBiYWIwMmU=
    Deleted: Mi0yZDVhN2E3NC0xMjY2LTQ4YzEtYmE0Zi1mY2JhNDY3MGJjNjA=
    Deleted: Mi1kODI0ZTc5My0zM2I5LTQ0MzYtYmE4Mi0xMzU0Nzk2MTc5Zjg=
    Deleted: Mi0zMjVhN2EzYy0yYTVjLTRlMWItOThhMy1kZDNlMjUwMGE1YzI=
    Deleted: Mi01NDdmOTcwMS0wYjU2LTRlZGEtODdhYy0yZDhmYzEwZjY3ZjA=
    Deleted: Mi0xZjllMWU5Zi1mNmUyLTQ3MTAtOTNiNy0yZWJmYWZhMTVmNmY=
    Deleted: Mi1iZmEwOGYzOC02MTE2LTQ2NDMtYjNjMS0yNGUwZmY1NDgzNGI=
    Deleted: Mi0zNTE3ODNjMC0yYmQxLTQ1YzItYTc3ZS01YjM1ZmZiNWM1YjE=
    Deleted: Mi02NzM2YjY0MS00OTM3LTRmZjYtYjgwMy02YWM1YTJiMDFkNWM=
    Deleted: Mi1lNWQ3MjNkMC1jNzYyLTQ2OWEtYWYzNi0xOWY0Y2NhMjEyZDY=
    Deleted: Mi0zNTg1YTRhMi1iMjlmLTQ2MWUtOTYzZC0yNGE0MTdhNTc0MDc=
    Deleted: Mi0zNzdiMTc1NS1mNTk1LTQ2MmYtYjc3YS00ZDkzMTBhYTU1NDA=
    Deleted: Mi1lMGU0Zjk2ZS03ODQzLTRjZWMtYTVmZi01NDQzMzg2ZjBhNzA=
    Deleted: Mi1jODViYmRlZS02OTk3LTQ5ZTEtYmVkYy00ZTdhNjg3MTdiNmQ=
    Deleted: Mi01YTM3NWU1ZS0wNzYxLTQ1MTAtYTJlMi05YmU0NmZlZTFlZDg=
    Deleted: Mi02M2I3ZjExYi1jNWIzLTRmZTItOTk2NS1mYmY2ZGQ0OWQ4MWQ=
    Deleted: Mi1lZTQ5ODk5Yy0zMTc4LTRlYzQtYTQ2Yy1mMTgwY2FkZjQ4ZWM=
    Deleted: Mi1hOTgxYjYxYS0zMmQ3LTQ5MDEtYjdkMS0xZTBhMjhjZmNlNWE=
    Deleted: Mi0zZjk0MzdlYS0wNjdiLTQyMDUtODk5YS0zMTE3NjY4NzQ3OTQ=
    Deleted: Mi02NjBjOGRiOC0wYjE2LTQ0ODEtYmU2OC04MmU0Njk1MDllNzU=
    Committing...
    {"responseHeader":{"status":0,"QTime":43}}

    Done. Deleted: 142 | Errors: 0

