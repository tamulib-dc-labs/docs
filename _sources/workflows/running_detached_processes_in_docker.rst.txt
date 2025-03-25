================================================
Running Detached Processes in a Docker Container
================================================

Often times, you will need to run a process in the background in a Docker container. This explains how to do that without
screen or tmux.

------------------
Using nohup Inside
------------------

If you are in a Docker container, you should be able to use :code:`nohup` like below:

.. code-block:: shell

    nohup your_command > output.log 2>&1 &

So, to run a DSPACE import, you could do something like:

.. code-block:: shell

    nohup /dspace/bin/dspace import -a -e "mark.baggett@tamu.edu" -c a0621c24-2e7c-4b33-a893-8b7798e0a4ad -s batch_5_tn -m batch_5_tn_not_zipped_post_crash2.txt > mark.log 2>&1 &

------------------------
Using nohup from Outside
------------------------

.. code-block:: shell

    docker exec -d <container_name> nohup /dspace/bin/dspace import -a -e "mark.baggett@tamu.edu" -c a0621c24-2e7c-4b33-a893-8b7798e0a4ad -s batch_5_tn -m batch_5_tn_not_zipped_post_crash2.txt > mark.log 2>&1 &

---------------
Running Batches
---------------

A basic example of how to setup batches. You should run this with :code:`nohup`.

.. code-block:: shell

    #!/bin/bash

    # Define variables
    EMAIL="mark.baggett@tamu.edu"
    COLLECTION="a0621c24-2e7c-4b33-a893-8b7798e0a4ad"

    run_import() {
      local BATCH_NAME=$1
      local METADATA_FILE=$2
      local LOG_FILE=$3

      echo "Starting import for $BATCH_NAME..."
      nohup /dspace/bin/dspace import -a -e "$EMAIL" -c "$COLLECTION" -s "$BATCH_NAME" -m "$METADATA_FILE" > "$LOG_FILE" 2>&1
      echo "Import for $BATCH_NAME started. Logs: $LOG_FILE"
    }

    # Add import information
    run_import "batch_8_tn" "batch_8_tn_not_zipped_prod2.txt" "mark_prod_batch_8.log"

    echo "All imports started."
