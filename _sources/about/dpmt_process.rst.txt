=============
DPMT Workflow
=============

-----
About
-----

This page describes the workflow used for DPMT projects from start to completion.

------------
What is DPMT
------------

The Digital Project Management Team (DPMT) is a team of individuals responsible for digitizing and archiving Texas A&M special collections and making them available online. The team is made up of representatives for each operational step of the process.

-----------------
Workflow Overview
-----------------

Project Intake & Proposal
=========================

1. Stakeholder submits an `IDEA Document <https://docs.google.com/document/d/1YZszCwbYvEnoJjc22-ruklMgG_jdiZEV6gE0FBfEoYc/edit?usp=sharing>`_ to DPMT
2. Mark adds the project to the `Pre-Project Checklist <https://docs.google.com/spreadsheets/d/1hp5zOrvEr2zFYAkSb-pVWuoRiC8Ps0pNYHYEgWVjRSc/edit?gid=0#gid=0>`_
3. Stakeholder reviews the collection, selects items, and submits an `Inventory <https://docs.google.com/spreadsheets/d/1_ny0kemXFwD79OXVa5FSqMnoMPt1iJfl01RID9B4wr4/edit?gid=0#gid=0>`_
4. Stakeholder submits an `Access Rights Review <https://docs.google.com/document/d/18D61Y5MoZDRsYlRf27Fr6yqVoiXWCEE85xRIlSK5Z-o/edit?usp=sharing>`_
5. Mark schedules an IDEA review meeting

Feasibility Review
==================

1. DPMT teams review submitted content
2. Mark creates a `Feasibility Review Document <https://docs.google.com/spreadsheets/d/1wVqaBgO4dDbxTbrq75fakv6qzIFkghcTIuFFNAKFMoE/edit?gid=0#gid=0>`_
3. Mark schedules a Project Kickoff meeting

Project Planning
================

1. Jeannette determines metadata requirements
2. Mark determines repository & discovery platform
3. John determines access restrictions
4. Phelan determines digitization requirements
5. Mark adds the project to the Project Snapshot spreadsheet

Metadata & Ingest
=================

1. Jeannette packages metadata using SAF Creator
2. Mark ingests content into the pre-production repository
3. DPMT performs QA review
4. Mark ingests into the production repository

Access, Discovery, and Preservation
===================================

1. Mark writes digital exhibit / collection page content
2. Mark submits thumbnail & description to Bonnie
3. Jeannette creates a catalog record (if applicable)
4. Bonnie adds the collection to the Digital Collections website
5. Abi ensures the collection is preserved

---------
Flowchart
---------

.. mermaid::

    flowchart TD

    %% Intake
    subgraph Intake["Project Intake"]
        A1[Stakeholder submits IDEA Document]
        A2[Mark adds project to Pre-Project Checklist]
        A3[Stakeholder submits Inventory]
        A4[Stakeholder submits Access Rights Review]
        A5[Mark schedules IDEA review meeting]
    end

    %% Feasibility
    subgraph Feasibility["Feasibility Review"]
        B1[DPMT reviews submitted content]
        B2[Mark creates Feasibility Review Document]
        B3[Mark schedules Kickoff meeting]
    end

    %% Planning
    subgraph Planning["Project Planning"]
        C1[Jeannette determines metadata needs]
        C2[Mark selects repository & discovery platform]
        C3[John determines access restrictions]
        C4[Phelan determines digitization needs]
        C5[Mark updates Project Snapshot spreadsheet]
    end

    %% Digitization
    subgraph Digitization["Digitization & Processing"]
        D1[Jaq processes collection / sends to DiSC]
        D2[Phelan scans and writes to CIFS]
        D3[Kaila processes files on CIFS]
        D4[Mark generates service files]
        D5[Jeannette refines inventory from scans]
    end

    %% Metadata & Ingest
    subgraph Ingest["Metadata & Ingest"]
        E1[Jeannette packages metadata with SAF Creator]
        E2[Mark ingests to pre-production repository]
        E3[DPMT performs QA review]
        E4[Mark ingests to production repository]
    end

    %% Access & Preservation
    subgraph Access["Access, Discovery & Preservation"]
        F1[Mark writes collection or exhibit content]
        F2[Mark submits thumbnail & description to Bonnie]
        F3[Jeannette creates catalog record]
        F4[Bonnie adds collection to Digital Collections site]
        F5[Abi preserves the collection]
    end

    %% Flow
    A1 --> A2 --> A3 --> A4 --> A5
    A5 --> B1 --> B2 --> B3
    B3 --> C1 --> C2 --> C3 --> C4 --> C5
    C5 --> D1 --> D2 --> D3 --> D4 --> D5
    D5 --> E1 --> E2 --> E3 --> E4
    E4 --> F1 --> F2 --> F3 --> F4 --> F5

--------------------
Original Description
--------------------

* Submits IDEA Document to DPMT (Stakeholder)
* Project is added to Pre-Project Checklist spreadsheet (Mark)
* Reviews collection, selects items appropriate for digitization, and submits inventory (Stakeholder)
* Submits Access Rights Review Document (Stakeholder)
* Schedules meeting to discuss IDEA document (Mark)
* Reviews Content Submitted by Stakeholder (DPMT Teams)
* Creates Feasibility Review Document based on DPMT Feedback (Mark)
* Schedules Kickoff meeting with stakeholder and DPMT (Mark)
* Determines Metadata needs (Jeannette)
* Determines Repository and Discovery Platform (Mark)
* Determines Access Restrictions (John)
* Determines Digitization Needs (Phelan)
* Adds to Project Snapshot spreadsheet (Mark)
* Processes collection and / or sends to DiSC analog objects with completed Inventory (Jaq)
* Scans files and writes to cifs (Phelan)
* Processes files on cifs (Kaila)
* Generates service files from items on cifs (Mark)
* Refines from initial inventory using scans on cifs (Jeannette)
* Metadata is packaged with SAF creator (Jeannette)
* Ingests into pre-production repository and discovery platform (Mark)
* Collection is reviewed for QA (DPMT)
* Ingests into production repository and discovery platform (Mark)
* Digital exhibit or digital collection page content is written (Mark)
* Thumbnail and description is created and submitted to Bonnie (Mark)
* Catalog record is created if applicable (Jeannette)
* Collection is added to the Digital Collections page on the website (Bonnie)
* Collection is preserved (Abi)

