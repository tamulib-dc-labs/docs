========
Glossary
========

This page collects terms, acronyms, and system names that come up across the Digital Collections
documentation. It is meant as a quick reference for new team members — deeper documentation for many
of these systems lives in :doc:`04_cultral_heritage`, :doc:`999_legacy`, and the
``applications/`` and ``workflows/`` sections of this site.

Archipelago-specific terminology (ADO, AMI, Strawberry Field, TWIG, and friends) has its own glossary
at :doc:`../applications/archipelago/00_archipelago-terms`; the most load-bearing of those terms are
also summarized below for convenience.

.. glossary::
   :sorted:

   ADO
      Archipelago Digital Object. Any digital object or digital object collection managed in
      Archipelago. Every ADO has a **type** (or *worktype*), such as "Book" or "Image", that
      determines how it is displayed.

   AMI
      Archipelago Multi-Importer. The module used to batch ingest ADOs into Archipelago from a
      spreadsheet.

   ARK
      Archival Resource Key. A persistent identifier scheme used to provide long-term, stable access
      to digital objects even if their storage location changes. We mint ARKs via :term:`EZID`. See
      :doc:`../topics_and_services/identifiers/minting_arks`.

   Avalon
      Avalon Media System, the platform used to deliver streaming audio and video collections,
      built on :term:`Fedora`.

   Cantaloupe
      The IIIF image server used to serve zoomable, deep-viewable images for our digital collections.

   CAP
      Curator's Administration Platform. An in-house, open-source application that provides a common
      UI and API for institutional repositories participating in a Digital Asset Management Ecosystem.

   CWS
      Creative Works Series. An :term:`ADO` type used for multi-page or multi-part objects (such as a
      book) where individual pages or parts need to be browsed and, in some cases, programmatically
      paired with OCR/HTR text.

   DOI
      Digital Object Identifier. A persistent identifier commonly used for journal articles,
      datasets, and other scholarly outputs, often minted through :term:`EZID` or OJS.

   DPMT
      Digital Project Management Team. The cross-functional team responsible for reviewing,
      prioritizing, and shepherding digitization and digital collection projects from intake through
      completion. See the DPMT process documentation for how projects move through the team.

   DSpace
      The open-source repository platform that powers :term:`OAKTrust`, our institutional repository.

   EZID
      A persistent identifier service (provided by the California Digital Library) that we use to
      mint and manage :term:`ARK` and :term:`DOI` identifiers.

   Fedora
      The repository backend used for cultural heritage collections (served through :term:`SAGE` or
      Spotlight) and for audio/video collections served through :term:`Avalon`.

   HOCR
      An HTML-based format for representing OCR output, including the position of recognized text on
      a page image. Used to align searchable text with page images in multi-page objects.

   HPRC
      Texas A&M High Performance Research Computing. The campus unit providing the computational
      infrastructure that supports our AI/ML initiatives.

   HTR
      Handwritten Text Recognition. Similar to OCR, but for transcribing handwritten materials such
      as manuscripts and correspondence.

   IDEA Document
      The proposal document a stakeholder submits to :term:`DPMT` to request a new digital project.
      It kicks off the DPMT intake and review process.

   IIIF
      International Image Interoperability Framework. A set of open standards for delivering
      high-resolution images and audio/video in an interoperable way, served here via
      :term:`Cantaloupe` and viewed via Mirador.

   irIIIFService
      An in-house IIIF Presentation API implementation designed to work with our DSpace and Fedora
      content models.

   MAGPIE
      Metadata Assignment GUI Providing Ingest and Export App. Our primary in-house tool for
      ingesting :term:`SAF`-modeled data into :term:`Fedora`.

   OAKTrust
      Texas A&M University's open access institutional repository, built on :term:`DSpace`, used to
      collect, preserve, and share the scholarly output of the University and its partners.

   OCR
      Optical Character Recognition. Automated extraction of machine-readable text from images of
      printed material.

   OJS
      Open Journal Systems. The platform (via our partnership with the :term:`TDL`) used to launch,
      host, and manage open-access journals published at Texas A&M.

   ORCID
      Open Researcher and Contributor ID. A persistent identifier for individual researchers, used
      to disambiguate authors and link them to their scholarly output.

   RAG
      Retrieval-Augmented Generation. A technique that combines a language model with a search/
      retrieval step over a document collection, used to support advanced querying of digital
      collections.

   ROR
      Research Organization Registry. A persistent identifier for research institutions, used in OJS
      to identify author affiliations.

   SAF
      Simple Archive Format. A DSpace-defined file/folder structure for batch importing items and
      their metadata, commonly generated with our SAF Creator tool.

   SAGE
      One of the delivery systems used to serve cultural heritage collections built on
      :term:`Fedora`.

   Spotlight
      A Blacklight-based tool used to build online exhibits from digital collections.

   Strawberry Field
      An Archipelago descriptive metadata field made up of several individual Archipelago fields
      combined together.

   TDL
      Texas Digital Library. A consortium the Libraries partner with to host and support open-access
      journal publishing.

   TWIG
      The template engine Archipelago uses to extract metadata from an ADO's JSON and render it for
      display.

   WCAG
      Web Content Accessibility Guidelines. The standard we design digital collections and exhibits
      against to meet ADA Title II accessibility requirements.
