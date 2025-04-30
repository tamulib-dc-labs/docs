=================================
Understanding Our DSPACE Entities
=================================

This document describes our use of DSPACE Entities at Texas A&M University. It explains what is meant by "left" and "right"
and lays out what a CSV and SAF import should look like.

----------------------------
A Brief Overview of Entities
----------------------------

In DSpace, an Entity is a special type of Item which often has Relationships to other Entities. Every Entity is an Item
(the default DSPACE type). This means they must belong to a Collection. Not every Item is an Entity though.

Entities have a :code:`dspace.entity.type` field which defines their "Entity type." Based on that type, an Entity may be
related to other Entities via a Relationship. One Entity type may support several relationship types at once. Examples
of relationship types include "isPersonOfProject" or "isPublicationOfAuthor." In DSpace, an Entity is a special type of
Item which often has Relationships to other Entities.

Entities of different types may also have customized visualizations in the User Interface.  These visualizations may also
dynamically pull in metadata from related Entities.  For example, a Publication entity may be displayed in the User
Interface with an author name dynamically pulled in from a related Person entity.  The metadata "appears" as though it
is part of the Entity you are viewing, but it is dynamically pulled via the Relationship.

Entities and their Relationships are also completely configurable. DSpace provides some sample models out of the box,
which you can use directly or adapt as needed.

---------------------------
How Entities Relate to PCDM
---------------------------

The Entity model also has similarities with the `Portland Common Data Model (PCDM) <https://pcdm.org/>`_, with an Entity
roughly mapping to a "pcdm:Object" and existing Communities and Collections roughly mapping to a "pcdm:Collection".
However, at this time DSpace Entities concentrate more on building a graph structure of relationships, instead of a tree
structure.

----------------------------
Understanding Left and Right
----------------------------

Relationships between entities are conceptualized as :code:`left` and :code:`right`. For some reason, the way this is done
is backwards from what I'd expect. In laymans terms, the :code:`leftType` is the "parent," and the :code:`rightType` is
the "child." For instance, let's think about a :code:`Journal` and a :code:`JournalVolume`. In this conceptualization, the
parent is "Journal" and the :code:`leftType`. The Journal needs a relationship that ties it to the child. This is expressed
via the :code:`leftwardType` relationship. You might think this would be something like :code:`isJournalOfJournalVolume`,
but it is in fact the opposite.  The relationship on the parent will always be about the child because when we edit metadata
about the parent we will be updating it's relationship to the child. In other words, :code:`leftwardType` will always be
a property that refers to the child in a predicate like :code:`isChildOfParent`.

Vice versa, :code:`rightwardType` is a property on the child but it will always refer to the parent in a relationship like
:code:`isParentOfChild`.

--------
Journals
--------

Journals are configured out of the box when entities are enabled.  There are more optional relationships, but so far,
our default layout looks like this:

.. mermaid::

    graph TD
        Journal[Journal]
        JournalVolume[JournalVolume]
        JournalIssue[JournalIssue]
        Publication[Publication]

        Journal -->|isVolumeOfJournal-left| JournalVolume
        JournalVolume -->|isJournalOfVolume-right| Journal
        JournalVolume -->|isIssueOfJournalVolume-left| JournalIssue
        JournalIssue -->|isJournalVolumeOfIssue-right|JournalVolume
        JournalIssue -->|isPublicationOfJournalIssue-left| Publication
        Publication -->|isJournalIssueOfPublication-right| JournalIssue

This is enabled with this configuration:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE relationships SYSTEM "relationship-types.dtd">

    <relationships>

        <!-- Sample relationship types setup used for the entities development
         This file can be imported using the initialize-entities launcher -->
        <type>
            <leftType>Journal</leftType>
            <rightType>JournalVolume</rightType>
            <leftwardType>isVolumeOfJournal</leftwardType>
            <rightwardType>isJournalOfVolume</rightwardType>
            <leftCardinality>
                <min>0</min>
            </leftCardinality>
            <rightCardinality>
                <min>0</min>
            </rightCardinality>
        </type>
        <type>
            <leftType>JournalVolume</leftType>
            <rightType>JournalIssue</rightType>
            <leftwardType>isIssueOfJournalVolume</leftwardType>
            <rightwardType>isJournalVolumeOfIssue</rightwardType>
            <leftCardinality>
                <min>0</min>
            </leftCardinality>
            <rightCardinality>
                <min>0</min>
            </rightCardinality>
        </type>
        <type>
            <leftType>JournalIssue</leftType>
            <rightType>Publication</rightType>
            <leftwardType>isPublicationOfJournalIssue</leftwardType>
            <rightwardType>isJournalIssueOfPublication</rightwardType>
            <leftCardinality>
                <min>0</min>
            </leftCardinality>
            <rightCardinality>
                <min>0</min>
            </rightCardinality>
            <copyToRight>true</copyToRight>
        </type>
    </relationships>

---------------------------
Proposed Change to Journals
---------------------------

Because we have use cases where the model is more simple, I propose we change our XML to support this:


.. mermaid::

    graph TD
        Journal[Journal]
        JournalVolume[JournalVolume]
        JournalIssue[JournalIssue]
        Publication[Publication]

        Journal -->|isVolumeOfJournal-left| JournalVolume
        JournalVolume -->|isJournalOfVolume-right| Journal
        JournalVolume -->|isIssueOfJournalVolume-left| JournalIssue
        JournalVolume -->|isPublicationOfJournalVolume-left| Publication
        JournalIssue -->|isJournalVolumeOfIssue-right|JournalVolume
        JournalIssue -->|isPublicationOfJournalIssue-left| Publication
        Publication -->|isJournalIssueOfPublication-right| JournalIssue
        Publication -->|isJournalVolumeeOfPublication-right| JournalVolume

----------------------
Conference Proceedings
----------------------

In the case that we don't modify things like above, we minimally need something like this:

.. mermaid::

    graph TD
        Conference[Conference]
        ConferenceProceeding[ConferenceProceeding]
        ConferencePaper[ConferencePaper]

        Conference -->|isConferenceProceedingOfConference-left| ConferenceProceeding
        ConferenceProceeding -->|isConferenceOfConferenceProceeding-right| Conference
        ConferenceProceeding -->|isConferencePaperOfConferenceProceeding-left| ConferencePaper
        ConferencePaper -->|isConferenceProceedingOfConferencePaper-right| ConferenceProceeding

Our existing metadata will need to be modified to support this:

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE relationships SYSTEM "relationship-types.dtd">

    <relationships>
        <type>
            <leftType>Conference</leftType>
            <rightType>ConferenceProceeding</rightType>
            <leftwardType>isConferenceProceedingOfConference</leftwardType>
            <rightwardType>isConferenceOfConferenceProceeding</rightwardType>
            <leftCardinality>
                <min>0</min>
            </leftCardinality>
            <rightCardinality>
                <min>0</min>
            </rightCardinality>
        </type>
        <type>
            <leftType>ConferenceProceeding</leftType>
            <rightType>ConferencePaper</rightType>
            <leftwardType>isConferencePaperOfConferenceProceeding</leftwardType>
            <rightwardType>isConferenceProceedingOfConferencePaper</rightwardType>
            <leftCardinality>
                <min>0</min>
            </leftCardinality>
            <rightCardinality>
                <min>0</min>
            </rightCardinality>
        </type>
    </relationships>