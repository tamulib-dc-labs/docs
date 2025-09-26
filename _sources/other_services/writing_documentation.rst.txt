
=================
How to Write Documentation on this website
=================

Make sure you name your file something that makes the topic clear to yourself and others. Keep in mind that all pages will be arranged alphabetically by filename in the side menu.

The proper extension for a file on this website is .rst. This file is named writing_documentation.rst

Feel free to copy and paste any of the formatting on this file.

-----------------
Headings
-----------------
Your document must begin with a heading. The heading will appear as the page's name in the side menu.

* Headings appear with equal signs (=) in the rows immediately above and below the text of the heading. Both rows of equal signs must be the same length.
* Subheadings appear with hyphens (-) in the rows immediately above and below the text of the subheading. Both rows of hyphens must be the same length.
* Third-level headings appear with equal signs (=) in the row immediately below the text of the third-level heading.

.. image:: ../../_static/images/headings.png
    :alt: Screenshot of heading formatting


-----------------
Body Text
-----------------

The body text does not need any modifications. Just type normally. Text will wrap automatically when it goes online so do not worry about line breaks. To keep text in one paragraph, continue typing on the same line.

If you want to start a new paragraph, press enter twice.

-----------------
Bold Text
-----------------

To bold something, add two asterisks (**) at the start and end of the text you want to be bolded.

**Here is an example of bolded text.**

.. image:: ../../_static/images/bolded-text.png
    :alt: Screenshot of bolded text


-----------------
Bullets and Numbering
-----------------

1. To add a number, type the number followed by a period at the start of the line. 
2. Start a new line with every new number.
3. This will create a numbered list.

* To add a bullet, type an astrisk (*) at the start of the line.
* Start a new line with every new bullet point.
* This will create a bulleted list.

.. image:: ../../_static/images/numbers-bullets.png
    :alt: Screenshot of numbering and bullet format


-----------------
Hyperlinks
-----------------

To add a link, use the following format: 

`Home page for TAMU Digital Collections Labs <https://tamulib-dc-labs.github.io/docs/index.html>`_

.. image:: ../../_static/images/link.png
    :alt: Screenshot of hyperlink format

Do not forget the underscore (_) at the end.

-----------------
Images
-----------------

To add an image, the image must first be added to the docs/source/_static/images/ folder. Then enter :code:`.. image:: {filepath}`. 

Press return and on the next line, after adding an indentation enter :code:`:alt: {Alt text}`.

.. image:: ../../_static/images/TAM-MaroonBox.png
    :alt: Texas A&M Logo

.. image:: ../../_static/images/image.png
    :alt: Screenshot of code to add an image of Texas A&M Logo.

-----------------
Creating a Table
-----------------

Use the following format. Make sure everything is aligned exactly.


+---------------------------+-----------------------------------------------------------------------+------------------+
| Column A                  | Column B                                                              | Column C         |
+===========================+=======================================================================+==================+
| Row 2                     | Cell 2B                                                               |     cell 2C      |                      
+---------------------------+-----------------------------------------------------------------------+------------------+
| Row 3                     | Cell 3B                                                               |     cell 3C      |                                                
+---------------------------+-----------------------------------------------------------------------+------------------+

.. image:: ../../_static/images/table.png
    :alt: Screenshot of code to add a table.

-----------------
Adding a line of code
-----------------

To add a line of code, type ":code:" followed by two backticks. Backtick looks like this: `

The backtick may be found in the upper left corner of the keyboard, sharing a key with the tilde (~).

Type the code between the two backticks.

:code:`This text is formatted as code.`

.. image:: ../../_static/images/code.png
    :alt: Screenshot of code format

-----------------
Adding a block of code
-----------------

To add a block of code, type :code:`.. code:: {coding language here}`. Then copy and paste the code. Make sure indentation of each row is correct. The text in the code block will appear in different colors for readability.

.. code:: python
    from csv import DictReader
    import os
    import json
    import shutil

.. image:: ../../_static/images/code-block.png
    :alt: Screenshot of code block format

-----------------
Adding a file from Google Workspace
-----------------

Similar to a code block, you will write the line :code:`.. raw:: html"`. In the next line, with a single indentation, type :code:`<iframe src="{link to document or spreadsheet}" height="{height}" width="{width}" frameborder="0" allowfullscreen></iframe>`. 

.. raw:: html

    <iframe src="https://docs.google.com/document/d/1bRT2R4hQJ_ZaYumq_TRGQtc0dUDIA_2CK8FM2Hp7Xqg/edit?usp=sharing" height="400" width="800" frameborder="0" allowfullscreen></iframe>



.. image:: ../../_static/images/google-doc.png
    :alt: Screenshot of code to add a google doc
    