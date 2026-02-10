=====================
Modifying the Webform
=====================

AMI spreadsheet imports allow the admin to set whatever metadata fields they want, but this is not reflected in the default webform. If the admin wants to include a custom metadata field in an ADO upload using the webform, they can't.

This also raises issues when editing existing ADOs. There are three ways to edit an existing ADO:

* AMI batch update

* JSON edit

* Edit Descriptive Metadata webform

The webform is the most user-friendly option. However, if the ADO has metadata not in the default webform, the admin is unable to edit those fields. 

--------------------
How to start editing
--------------------

1. Go to :code:`/admin/structure/webform`.

2. From the list, locate the webform you wish to edit. Click "Build" at the right hand of the table.

3. You should now see a list of all fields included in that webform.

--------------------------------------------------------
Changes made to the Default Descriptive Metadata webform
--------------------------------------------------------

The Default Descriptive Metadata webform is the one used when creating a new ADO of any worktype except Collection and CreativeWorkSeries.

Media Type
----------

Click "Edit". Scroll to "Element Options". Change "Options" to :code:`Custom options...`. Add all worktypes to the list.


Interview Details
-----------------

Click "Visible". Change the conditionals so that it is :code:`Visible` when :code:`Any` of the following is met: 
    * :code:`MediaType` :code:`Value is` :code:`AudioObject` 
    * :code:`MediaType` :code:`Value is` :code:`Videobject`

Interviewee
-----------

Click "Visible". Change the conditionals so that it is :code:`Visible` when :code:`Any` of the following is met: 
    * :code:`MediaType` :code:`Value is` :code:`AudioObject` 
    * :code:`MediaType` :code:`Value is` :code:`Videobject`

Interviewer
-----------

Click "Visible". Change the conditionals so that it is :code:`Visible` when :code:`Any` of the following is met: 
    * :code:`MediaType` :code:`Value is` :code:`AudioObject` 
    * :code:`MediaType` :code:`Value is` :code:`Videobject`

Duration
--------

Click "Visible". Change the conditionals so that it is :code:`Visible` when :code:`Any` of the following is met: 
    * :code:`MediaType` :code:`Value is` :code:`AudioObject` 
    * :code:`MediaType` :code:`Value is` :code:`Videobject`

URL of the original Website
---------------------------

Click "Visible". Change the conditionals so that it is :code:`Visible` when :code:`Any` of the following is met: 
    * :code:`MediaType` :code:`Value is` :code:`AudioObject` 
    * :code:`MediaType` :code:`Value is` :code:`Videobject`
    * :code:`MediaType` :code:`Value is` :code:`WebPage`
    * :code:`MediaType` :code:`Value is` :code:`MetadataOnly`

Description
-----------

Change "allowed number of values" to "Unlimited".

Publisher
---------

Change "allowed number of values" to "Unlimited".

General Note
------------

Change "allowed number of values" to "Unlimited".

Physical Description Extent
---------------------------

Change "allowed number of values" to "Unlimited".

Upload Document Files
---------------------

Click "Visible". Get rid of all conditionals.

Map Details
-----------

This is a new element. 

1. At the top beside "Basic Descriptive Metadata", click "Add element". 
2. Select "Fieldset" for type. Name the element "Map Details".
3. Go to "Conditions" tab and create a conditional so that it is :code:`Visible` when :code:`All` of the following is met: 
    * :code:`MediaType` :code:`Value is` :code:`Map` 

Projection
----------

This is a new element. 

1. Beside "Map Details", click "Add element".  
2. Select "Text field" for type. Name the element "Projection".
3. Go to "Conditions" tab and create a conditional so that it is :code:`Visible` when :code:`All` of the following is met: 
    * :code:`MediaType` :code:`Value is` :code:`Map` 

State/Edition of Map
--------------------

This is a new element. 

1. Beside "Map Details", click "Add element". 
2. Select "Fieldset" for type. Name the element "State/Edition of Map".
3. Go to "Conditions" tab and create a conditional so that it is :code:`Visible` when :code:`All` of the following is met: 
    * :code:`MediaType` :code:`Value is` :code:`Map` 

-------------------------------------------------------------
Changes made to the Default Digital Object Collection webform
-------------------------------------------------------------

The Default Digital Object Collection webform is used when creating/editing a Collection or CreativeWorkSeries.


Description
-----------

Change "allowed number of values" to "Unlimited".

General Note
------------

Change "allowed number of values" to "Unlimited".

Physical Description Extent
---------------------------

Change "allowed number of values" to "Unlimited".

Building Information
--------------------

This is a new element. 

1. At the top beside "Basic Descriptive Metadata", click "Add element". 
2. Select "Fieldset" for type. Name the element "Building Information".
3. Go to "Conditions" tab and create a conditional so that it is :code:`Visible` when :code:`All` of the following is met: 
    * :code:`Collection/Compound Type` :code:`Value is` :code:`CreativeWorkSeries` 

Building History
----------------

This is a new element. 

1. Beside "Building Information", click "Add element". 
2. Select "Textarea" for type. Name the element "Building History".
3. Go to "Conditions" tab and create a conditional so that it is :code:`Visible` when :code:`All` of the following is met: 
    * :code:`Collection/Compound Type` :code:`Value is` :code:`CreativeWorkSeries` 

Date Built
----------

This is a new element. 

1. Beside "Building Information", click "Add element". 
2. Select "Text field" for type. Name the element "Date Built".
3. Go to "Conditions" tab and create a conditional so that it is :code:`Visible` when :code:`All` of the following is met: 
    * :code:`Collection/Compound Type` :code:`Value is` :code:`CreativeWorkSeries` 

Date Razed
----------

This is a new element. 

1. Beside "Building Information", click "Add element". 
2. Select "Text field" for type. Name the element "Date Razed".
3. Go to "Conditions" tab and create a conditional so that it is :code:`Visible` when :code:`All` of the following is met: 
    * :code:`Collection/Compound Type` :code:`Value is` :code:`CreativeWorkSeries` 
