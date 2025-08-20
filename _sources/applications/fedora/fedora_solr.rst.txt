===================================
Understanding Solr Config in Fedora
===================================

Solrization in Fedora is limited to the Marmotta configuration found in `Fedora in tldocker <https://github.com/TAMULib/tl_docker/blob/0afe641d4467bb0a359e6d3ac1de9aef994704c9/fedora/fedora/tamu-ldpath.txt#L87>`_.

This document explains what will be Solrized and what won't.

.. code-block:: txt

    @prefix fedora: <http://fedora.info/definitions/v4/repository#>
    @prefix ldp: <http://www.w3.org/ns/ldp#>
    @prefix acl : <http://www.w3.org/ns/auth/acl#>
    @prefix pcdm: <http://pcdm.org/models#>
    @prefix ore: <http://www.openarchives.org/ore/terms/>
    @prefix iana: <http://www.iana.org/assignments/relation/>
    @prefix dcterms: <http://purl.org/dc/terms/>
    @prefix ebucore: <http://www.ebu.ch/metadata/ontologies/ebucore/ebucore#>
    @prefix local: <http://digital.library.tamu.edu/schemas/local/>

    id                               = . :: xsd:string ;

    resource                         = ldp:contains[rdf:type is fedora:Binary] :: xsd:anyURI ;

    created                          = fedora:created :: xsd:dateTime ;
    createdBy                        = fedora:createdBy :: xsd:string ;
    hasParent                        = fedora:hasParent :: xsd:string ;
    hasVersions                      = fedora:hasVersions :: xsd:anyURI ;
    lastModified                     = fedora:lastModified :: xsd:dateTime ;
    lastModifiedBy                   = fedora:lastModifiedBy :: xsd:string ;
    numberOfChildren                 = fedora:numberOfChildren :: xsd:integer ;

    type                             = rdf:type :: xsd:anyURI ;
    label                            = rdfs:label :: xsd:string ;
    comment                          = rdfs:comment :: xsd:string ;
    sameAs                           = owl:sameAs :: xsd:anyURI ;

    fileOf                           = pcdm:fileOf :: xsd:anyURI ;
    hasFile                          = pcdm:hasFile :: xsd:anyURI ;
    hasMember                        = pcdm:hasMember :: xsd:anyURI ;
    hasRelatedObject                 = pcdm:hasRelatedObject :: xsd:anyURI ;
    memberOf                         = pcdm:memberOf :: xsd:anyURI ;
    relatedObjectOf                  = pcdm:relatedObjectOf :: xsd:anyURI ;

    aggregates                       = ore:aggregates :: xsd:anyURI ;
    isAggregatedBy                   = ore:isAggregatedBy :: xsd:anyURI ;
    proxyFor                         = ore:proxyFor :: xsd:anyURI ;
    proxyIn                          = ore:proxyIn :: xsd:anyURI ;

    first                            = iana:first :: xsd:anyURI ;
    last                             = iana:last :: xsd:anyURI ;
    next                             = iana:next :: xsd:anyURI ;
    prev                             = iana:prev :: xsd:anyURI ;
    describes                        = iana:describes :: xsd:anyURI ;
    describedBy                      = iana:describedBy :: xsd:anyURI ;

    accessControl                    = acl:accessControl :: xsd:anyURI ;
    accessTo                         = acl:accessTo :: xsd:anyURI ;
    accessToClass                    = acl:accessToClass :: xsd:anyURI ;
    agent                            = acl:agent :: xsd:string ;
    agentClass                       = acl:agentClass :: xsd:anyURI ;
    mode                             = acl:mode :: xsd:anyURI ;

    title                            = dc:title | dcterms:title :: xsd:string ;
    content_type_ss                  = dc:type | dcterms:type :: xsd:string ;
    digital_publisher_ss             = dc:publisher | dcterms:publisher :: xsd:string ;
    rights_access_ss                 = dc:rights | dcterms:rights | dcterms:accessRights :: xsd:string ;
    reformatting_ss                  = dc:format | dcterms:format :: xsd:string ;
    filename_ss                      = (ldp:contains[rdf:type is fedora:Binary] / ebucore:filename) | dc:identifier :: xsd:string ;

    subject_ss                       = dc:subject | dcterms:subject :: xsd:string ;
    creator_ss                       = dc:creator | dcterms:creator :: xsd:string ;
    date_published_s                 = dcterms:dateAccepted :: xsd:string ;
    date_created_s                   = dc:date | dcterms:date :: xsd:string ;
    date_issued                      = dcterms:issued :: xsd:string ;

    summary_abstract_ss              = dcterms:abstract | dc:description :: xsd:string ;
    language_ss                      = dc:language | dcterms:language :: xsd:string ;
    institution_department_ss        = dc:contributor | dcterms:contributor :: xsd:string ;
    standard_digital_identifier_ss   = dcterms:identifier | dc:identifier :: xsd:string ;
    local_digital_identifier_ss      = dcterms:identifier | dc:identifier :: xsd:string ;
    edition_revision_information_ss  = dcterms:hasVersion | dc:description :: xsd:string ;

    alternative_title_ss             = dcterms:alternative :: xsd:string ;
    genre_ss                         = dc:type :: xsd:string ;
    table_of_contents_ss             = dcterms:tableOfContents :: xsd:string ;
    contributor_ss                   = dc:contributor | dcterms:contributor :: xsd:string ;
    related_resource_ss              = dcterms:isPartOf :: xsd:string ;
    original_publisher_ss            = dc:publisher | dcterms:publisher :: xsd:string ;
    physical_extent_ss               = dcterms:extent :: xsd:string ;
    sponsor_ss                       = dc:contributor | dcterms:contributor :: xsd:string ;

    source_collection_ss             = dc:relation | dcterms:relation :: xsd:string ;
    original_resource_ss             = dc:source | dcterms:source :: xsd:string ;
    notes_ss                         = skos:note | skos:editorialNote | skos:historyNote | skos:scopeNote | dc:description :: xsd:string ;
    origin_ss                        = dc:description :: xsd:string ;
    audience_level_ss                = dc:audience | dcterms:audience :: xsd:string ;
    classification_ss                = dc:description :: xsd:string ;
    physical_item_identifier_ss      = dc:identifier :: xsd:string ;
    physical_item_location_ss        = dc:description :: xsd:string ;
    details_ss                       = local:details :: xsd:string ;
    spatial_ss                       = dcterms:spatial :: xsd:string ;
    created_ss                       = dcterms:created :: xsd:string ;
    medium_ss                        = dcterms:medium :: xsd:string ;
    provenance_ss                    = dcterms:provenance :: xsd:string ;
    temporal_ss                      = dcterms:temporal :: xsd:string ;
    local_coordinates                = local:coordinates :: xsd:string ;