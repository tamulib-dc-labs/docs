# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TAMU Digital Collections Labs'
copyright = '2026, Texas A&M Libraries - Digital Collections Services'
author = 'Mark Baggett'
html_title = 'TAMU Digital Collections Labs'
html_short_title = 'DCLabs'

# -- TAMU Brand Colors -------------------------------------------------------
# Texas A&M University official brand colors
tamu_colors = {
    'aggie_blue': '#003D7B',
    'otto_red': '#B00026',
    'aggie_gold': '#FFB81C',
    'white': '#FFFFFF',
    'black': '#000000',
}

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinxcontrib.mermaid']

mermaid_output_format = 'raw'

templates_path = ['_templates']
exclude_patterns = []

warningiserror = True
keep_going = True



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = '_static/images/TAM-MaroonBox.png'
html_favicon = '_static/images/TAM-MaroonBox.png'

# Furo theme options — customize to match TAMU branding
html_theme_options = {
    'source_repository': 'https://github.com/TAMULib/dc-labs-docs/',
    'source_branch': 'main',
    'source_directory': 'docs/',
    'top_of_page_buttons': ['view', 'edit'],

    # Navigation sidebar settings
    # 'announcement': '',
}

# -- TAMU Footer Template ----------------------------------------------------
# Custom footer rendered via base.html template

mermaid_init_js = """
mermaid.initialize({
  flowchart: {
    useMaxWidth: false,
    htmlLabels: true,
    nodeSpacing: 50,
    rankSpacing: 60,
    wrappingWidth: 500
  }
});
"""
