# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TAMU Digital Collections Labs'
copyright = '2025, Mark Baggett'
author = 'Mark Baggett'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinxcontrib.mermaid']

mermaid_output_format = 'raw'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']

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
