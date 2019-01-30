from docutils import nodes
from docutils.parsers.rst import Directive

class section_list(nodes.General, nodes.Element):
    pass

class SectionDirective(Directive):
    has_content = True

    def run(self):
        return [section_list('')]


def generate_section_list(app, doctree, docname):
    para = nodes.paragraph()
    for node in doctree.traverse(nodes.section):
        title = node.next_node(nodes.Titular)
        if title:
            para += nodes.Text(title.astext())
    node.replace_self([para])

def setup(app):
    app.add_node(section_list)
    app.add_directive('sections', SectionDirective)
    app.connect('doctree-resolved', generate_section_list)
