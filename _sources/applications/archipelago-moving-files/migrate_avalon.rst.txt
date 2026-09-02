============================
Migrating Avalon Collections
============================

Clone `pyavalon <https://github.com/tamulib-dc-labs/pyavalon>`_ repository.

In pyavalon run the following code:

:code:`pyavalon create_ami_set -c <collection_id> -i prod -o ami_set.csv`

This will create an AMI set for a specific collection. You may need to do some minor review to the generated output to ensure consistant formatting.

The ADO type for these items will be StreamingAudio. Do not use this for restricted items. Archipelago will not have access to the files and hence won't be able to upload media.

=======================================
Migrating Avalon Restricted Collections
=======================================

Run :code:`create_ami_set`, but edit the Image and Document columns to include a filepath to the vtt and media.

Media files can be found on digital_project_management or cush_digital_collections drives. Transcript/captions files can be either found in edge-grant-reviewer or whisper-reviewer repositories.

Media can be hosted on `Esmero Web <https://tamulib-dc-labs.github.io/docs/applications/archipelago-moving-files/esmero-web.html>`_. Read that documentation for further instructions. 

Be sure you change the ADO type from StreamingAudio to AudioObject or VideoObject.