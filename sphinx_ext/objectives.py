# -*- coding: utf-8 -*-
"""
    sphinx.ext.objective
    ~~~~~~~~~~~~~~~~~~~~

    Allow objectives to be inserted into your documentation.  Inclusion of LOs can
    be switched of by a configuration variable.  The objectivelist directive collects
    all objectives of your project and lists them along with a backlink to the
    original location.

    :copyright: Copyright 2007-2018 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.admonitions import BaseAdmonition

import sphinx
from sphinx.environment import NoUri
from sphinx.locale import _, __
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import set_source_info
from sphinx.util.texescape import tex_escape_map

if False:
    # For type annotation
    from typing import Any, Dict, Iterable, List  # NOQA
    from sphinx.application import Sphinx  # NOQA
    from sphinx.environment import BuildEnvironment  # NOQA

logger = logging.getLogger(__name__)


class objective_node(nodes.Admonition, nodes.Element):
    pass


class objectivelist(nodes.General, nodes.Element):
    pass


class Objective(BaseAdmonition, SphinxDirective):
    """
    A objective entry, displayed (if configured) in the form of an admonition.
    """

    node_class = objective_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }

    def run(self):
        # type: () -> List[nodes.Node]
        if not self.options.get('class'):
            self.options['class'] = ['admonition-objective']

        (objective,) = super(Objective, self).run()
        if isinstance(objective, nodes.system_message):
            return [objective]

        objective.insert(0, nodes.title(text=_('Objective')))
        set_source_info(self, objective)

        targetid = 'index-%s' % self.env.new_serialno('index')
        # Stash the target to be retrieved later in latex_visit_objective_node.
        objective['targetref'] = '%s:%s' % (self.env.docname, targetid)
        targetnode = nodes.target('', '', ids=[targetid])
        return [targetnode, objective]


def process_objectives(app, doctree):
    # type: (Sphinx, nodes.Node) -> None
    # collect all objectives in the environment
    # this is not done in the directive itself because it some transformations
    # must have already been run, e.g. substitutions
    env = app.builder.env
    if not hasattr(env, 'objective_all_objectives'):
        env.objective_all_objectives = []  # type: ignore
    for node in doctree.traverse(objective_node):
        app.emit('objective-defined', node)

        try:
            targetnode = node.parent[node.parent.index(node) - 1]
            if not isinstance(targetnode, nodes.target):
                raise IndexError
        except IndexError:
            targetnode = None
        newnode = node.deepcopy()
        del newnode['ids']
        env.objective_all_objectives.append({  # type: ignore
            'docname': env.docname,
            'source': node.source or env.doc2path(env.docname),
            'lineno': node.line,
            'objective': newnode,
            'target': targetnode,
        })

        if env.config.objective_emit_warnings:
            logger.warning(__("Objective entry found: %s"), node[1].astext(),
                           location=node)


class ObjectiveList(SphinxDirective):
    """
    A list of all objective entries.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}  # type: Dict

    def run(self):
        # type: () -> List[objectivelist]
        # Simply insert an empty objectivelist node which will be replaced later
        # when process_objective_nodes is called
        return [objectivelist('')]


def process_objective_nodes(app, doctree, fromdocname):
    # type: (Sphinx, nodes.Node, unicode) -> None
    if not app.config['objective_include_objectives']:
        for node in doctree.traverse(objective_node):
            node.parent.remove(node)

    # Replace all objectivelist nodes with a list of the collected objectives.
    # Augment each objective with a backlink to the original location.
    env = app.builder.env

    if not hasattr(env, 'objective_all_objectives'):
        env.objective_all_objectives = []  # type: ignore

    for node in doctree.traverse(objectivelist):
        if node.get('ids'):
            content = [nodes.target()]
        else:
            content = []

        for objective_info in env.objective_all_objectives:  # type: ignore
            para = nodes.paragraph(classes=['objective-source'])
            description = _('<<original entry>>')
            desc1 = description[:description.find('<<')]
            desc2 = description[description.find('>>') + 2:]
            para += nodes.Text(desc1, desc1)

            # Create a reference
            newnode = nodes.reference('', '', internal=True)
            innernode = nodes.emphasis(_('original entry'), _('original entry'))
            try:
                newnode['refuri'] = app.builder.get_relative_uri(
                    fromdocname, objective_info['docname'])
                newnode['refuri'] += '#' + objective_info['target']['refid']
            except NoUri:
                # ignore if no URI can be determined, e.g. for LaTeX output
                pass
            newnode.append(innernode)
            para += newnode
            para += nodes.Text(desc2, desc2)

            objective_entry = objective_info['objective']
            # Remove targetref from the (copied) node to avoid emitting a
            # duplicate label of the original entry when we walk this node.
            if 'targetref' in objective_entry:
                del objective_entry['targetref']

            # (Recursively) resolve references in the LO content
            env.resolve_references(objective_entry, objective_info['docname'],
                                   app.builder)

            # Insert into the objectivelist
            content.append(objective_entry)
            content.append(para)

        node.replace_self(content)


def purge_objectives(app, env, docname):
    # type: (Sphinx, BuildEnvironment, unicode) -> None
    if not hasattr(env, 'objective_all_objectives'):
        return
    env.objective_all_objectives = [objective for objective in env.objective_all_objectives  # type: ignore
                          if objective['docname'] != docname]


def merge_info(app, env, docnames, other):
    # type: (Sphinx, BuildEnvironment, Iterable[unicode], BuildEnvironment) -> None
    if not hasattr(other, 'objective_all_objectives'):
        return
    if not hasattr(env, 'objective_all_objectives'):
        env.objective_all_objectives = []  # type: ignore
    env.objective_all_objectives.extend(other.objective_all_objectives)  # type: ignore


def visit_objective_node(self, node):
    # type: (nodes.NodeVisitor, objective_node) -> None
    self.visit_admonition(node)
    # self.visit_admonition(node, 'objective')


def depart_objective_node(self, node):
    # type: (nodes.NodeVisitor, objective_node) -> None
    self.depart_admonition(node)


def latex_visit_objective_node(self, node):
    # type: (nodes.NodeVisitor, objective_node) -> None
    title = node.pop(0).astext().translate(tex_escape_map)
    self.body.append(u'\n\\begin{sphinxadmonition}{note}{')
    # If this is the original objective node, emit a label that will be referenced by
    # a hyperref in the objectivelist.
    target = node.get('targetref')
    if target is not None:
        self.body.append(u'\\label{%s}' % target)
    self.body.append('%s:}' % title)


def latex_depart_objective_node(self, node):
    # type: (nodes.NodeVisitor, objective_node) -> None
    self.body.append('\\end{sphinxadmonition}\n')


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_event('objective-defined')
    app.add_config_value('objective_include_objectives', False, 'html')
    app.add_config_value('objective_link_only', False, 'html')
    app.add_config_value('objective_emit_warnings', False, 'html')

    app.add_node(objectivelist)
    app.add_node(objective_node,
                 html=(visit_objective_node, depart_objective_node),
                 latex=(latex_visit_objective_node, latex_depart_objective_node),
                 text=(visit_objective_node, depart_objective_node),
                 man=(visit_objective_node, depart_objective_node),
                 texinfo=(visit_objective_node, depart_objective_node))

    app.add_directive('objective', Objective)
    app.add_directive('objectivelist', ObjectiveList)
    app.connect('doctree-read', process_objectives)
    app.connect('doctree-resolved', process_objective_nodes)
    app.connect('env-purge-doc', purge_objectives)
    app.connect('env-merge-info', merge_info)
    return {
        'version': sphinx.__display_version__,
        'env_version': 1,
        'parallel_read_safe': True
    }
