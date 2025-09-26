
=================
How to Write Documentation on this website
=================

Make sure you name your file something that makes the topic clear to yourself and others. Keep in mind that all pages will be arranged alphabetically by filename in the side menu.

The proper extension for a file on this website is .rst. (example.rst)

-----------------
Headings
-----------------
Your document must begin with a heading. The heading will appear as the page's name in the side menu.

* Headings appear with equal signs (=) in the rows immediately above and below the text of the heading. Both rows of equal signs must be the same length.
* Subheadings appear with hyphens (-) in the rows immediately above and below the text of the subheading. Both rows of hyphens must be the same length.
* Third-level headings appear with equal signs (=) in the row immediately below the text of the third-level heading.

Below are the three heading styles. Feel free to copy and paste the format into your document.

=================
This is the format for a heading.
=================

-----------------
This is the format for a subheading.
-----------------


This is the format for a third-level heading.
=========================


-----------------
Body Text
-----------------

The body text does not need any modifications. Just type normally. Text will wrap automatically when it goes online so do not worry about line breaks. To keep text in one paragraph, continue typing on the same line in this .rst file.

If you want to start a new paragraph, press enter twice.

-----------------
Bold Text
-----------------

To bold something, add two asterisks (**) at the start and end of the text you want to be bolded.

**Here is an example of bolded text.**

-----------------
Bullets and Numbering
-----------------

1. Use numbers followed by a period. 
2. Start a new line with every new number.
3. This will create a numbered list.

* Use astrisks (*) to add bullets.
* Start a new line with every new bullet point.
* This will create a bulleted list.


-----------------
Adding a website
-----------------

To add a link, use the following format: `text you want the clickable link to contain <Website url>`_. Do not forget the underscore (_) at the end.

Here is an example to copy and paste: 
`tamu-id-minter <https://github.com/tamulib-dc-labs/tamu-id-minter>`_


-----------------
Adding a line of code
-----------------

To add a line of code, type "":code:" followed by two backticks. Backtick looks like this: `

The backtick may be found in the upper left corner of the keyboard, sharing a key with the tilde (~).

Type the code between the two backticks.

Here is an example. Feel free to copy the formatting.

:code:`This text is formatted as code.`


-----------------
Adding a block of code
-----------------

To add a block of code, type :code:`.. code:: {coding language here}`. Then copy and paste the code. Make sure indentation of each row is correct. The text in the code block will appear in different colors for readability.

Here is an example. Feel free to copy and paste.

.. code:: python
    from csv import DictReader
    import os
    import json
    import shutil


-----------------
Adding a file from Google Workspace
-----------------

Similar to a code block, you will write the line :code:`.. raw:: html"`. In the next line, with a single indentation, type :code:`<iframe src="{link to document or spreadsheet}" height="400" width="1200" frameborder="0" allowfullscreen></iframe>`. 
    
Here is an example. Feel free to copy and paste.

.. raw:: html

    <iframe src="{link}" height="400" width="1200" frameborder="0" allowfullscreen></iframe>


-----------------
Creating a Table
-----------------

Copy and paste the following format. Make sure everything is aligned exactly.


+---------------------------+-----------------------------------------------------------------------+------------------+
| Column A                  | Column B                                                              | Column C         |
+===========================+=======================================================================+==================+
| Row 2                     | Cell 2B                                                               |     cell 3C      |                      
+---------------------------+-----------------------------------------------------------------------+------------------+
| Row 3                     | Cells can be two lines tall but you have to press enter and start a   |                  |                                   
|                           | new line. Text will not wrap automatically.                           |       cell 3C    |              
+---------------------------+-----------------------------------------------------------------------+------------------+


-----------------
Adding an Image
-----------------

To add an image, the image must first be added to the docs/source/_static/images/ folder. Then enter :code:`.. image:: {filepath}`. 

Press return and on the next line, after adding an indentation enter :code:`:alt: {Alt text}`.

.. image:: ../../_static/images/TAM-MaroonBox.png
    :alt: Texas A&M Logo

