# -*- coding: utf-8 -*-
#
# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import cloud_sptheme as csp

project = 'COSC2325'
copyright = '2018, Roie R. Black'
author = 'Roie R. Black'

version = ''
release = 'fall2018'

extensions = [
    'sphinx.ext.imgmath',
    'sphinx_ext.wordcount',
    'sphinx_ext.pylit_oz',
    'sphinxcontrib.spelling',
    'sphinxcontrib.bibtex',
    'sphinx_ext.circuits',
    'sphinx_ext.programoutput',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None

exclude_patterns = [
        '_build', 
        'Thumbs.db', 
        '.DS_Store',
        '_unpublished',
        'code/WireParser/_venv']

pygments_style = 'sphinx'

# -- Options for HTML output -----------------------------------------

html_theme = 'cloud'
html_theme_path = [csp.get_theme_dir()]
html_theme_options = { "roottarget": "index" }
html_static_path = ['_static']
html_logo = '_static/images/ACClogo.png'
html_favicon = '_static/images/favicon.ico'
# html_theme_options = {}
html_static_path = ['_static']
# html_sidebars = {}

# -- Options for LaTeX output ----------------------------------------

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '12pt',
    'preamble': '',
    'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'COSC1315.tex', 'COSC1315.FA18',
     'Roie R. Black', 'manual'),
]
