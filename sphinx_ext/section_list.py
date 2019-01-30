def setup(app):
    app.add_node(section_list)
    app.add_directive('section_list',WordcountDirective)
    app.connect('doctree-resolved', process_section_list_nodes)

from docutils import nodes

class section_list(nodes.General, nodes.Element):
    pass

from docutils.parsers.rst import Directive

class WordcountDirective(Directive):
    has_content = True

    def run(self):
        return [section_list('')]

def process_section_list_nodes(app, doctree, fromdocname):
    env = app.builder.env
    para = nodes.paragraph()
    for node in doctree.traverse(nodes.section):
        title = node.next_node(nodes.Titular)
        if title:
            para += nodes.Text(title.astext())

    node.replace_self([para])
        
        

