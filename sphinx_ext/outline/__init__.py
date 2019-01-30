# -*- coding: utf-8 -*-
"""
    sphinx_ext.outline
    =========================

    Sphinx extension to output reST outline file.

    .. moduleauthor:: Freek Dijkstra <software@macfreek.nl>

    :copyright: Copyright 2012-2013 by Freek Dijkstra.
    :license: BSD, see LICENSE.txt for details.
"""

from __future__ import (print_function, unicode_literals, absolute_import)

from sphinx.builders import Builder
from sphinx.writers.text import STDINDENT
from .rstbuilder import RstBuilder
from .rstwriter import RstWriter



def setup(app):
    app.require_sphinx('1.0')
    app.add_builder(RstBuilder)
    app.add_config_value('rst_file_suffix', ".rst", False)
    """This is the file name suffix for reST files"""
    app.add_config_value('rst_link_suffix', None, False)
    """The is the suffix used in internal links. By default, takes the same value as rst_file_suffix"""
    app.add_config_value('rst_file_transform', None, False)
    """Function to translate a docname to a filename. By default, returns docname + rst_file_suffix."""
    app.add_config_value('rst_link_transform', None, False)
    """Function to translate a docname to a (partial) URI. By default, returns docname + rst_link_suffix."""
    app.add_config_value('rst_indent', STDINDENT, False)