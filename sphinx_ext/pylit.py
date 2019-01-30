import os
import sys
import docutils
from docutils import frontend, writers, nodes
from sphinx.builders import Builder
from sphinx.util.osutil import ensuredir, os_path, SEP
from docutils.io import StringOutput
import codecs

class PylitBuilder(Builder):
    name='pylit'
    format = 'pylit'
    file_suffix = '.rst'
    link_suffix = None

    def init(self):
        self.file_suffix = '.rst'
        self.link_suffix = self.file_suffix
 
        def file_transform(docname):
            return docname + self.file_suffix

        # Function to convert the docname to a relative URI.
        def link_transform(docname):
            return docname + self.link_suffix

        self.file_transform = file_transform
        self.link_transform = link_transform

    def get_outdated_docs(self):
        for docname in self.env.found_docs:
            sourcename = os.path.join(self.env.srcdir, docname + self.file_suffix)
            targetname = os.path.join(self.outdir, sourcename)
            print("Processing:",sourcename, " -> ",  targetname)
            yield docname
    
    def get_target_uri(self, docname, typ=None):
        return self.link_transform(docname)

    def prepare_writing(self, docnames):
        self.writer = PylitWriter(self)

    def write_doc(self, docname, doctree):
        # This method is taken from TextBuilder.write_doc()
        # with minor changes to support :confval:`rst_file_transform`.
        destination = StringOutput(encoding='utf-8')
        print("write(%s,%s)" % (type(doctree), type(destination)))

        self.writer.write(doctree, destination)
        outfilename = os.path.join(self.outdir, self.file_transform(docname))
        print("write(%s,%s) -> %s" % (type(doctree), type(destination), outfilename))
        ensuredir(os.path.dirname(outfilename))
        try:
            f = codecs.open(outfilename, 'w', 'utf-8')
            try:
                f.write(self.writer.output)
            finally:
                f.close()
        except (IOError, OSError) as err:
            self.warn("error writing file %s: %s" % (outfilename, err))

    def finish(self):
        pass     

class PylitWriter(writers.Writer) :
    supported = ('pylit',)
    output = None

    def __init__(self, builder):
        writers.Writer.__init__(self)
        self.builder = builder
        self.translator_class = PylitTranslator

    def translate(self):
        self.visitor = visitor = self.translator_class(self.document)
        self.document.walkabout(visitor)
        self.output = ''.join(visitor.output)

class PylitTranslator(nodes.GenericNodeVisitor):

    def __init__(self, document):
        nodes.NodeVisitor.__init__(self, document)
        self.warn = self.document.reporter.warning
        self.error = self.document.reporter.error

        self.settings = settings = document.settings
        self.output = []

    simple_nodes = (
            nodes.TextElement,
            nodes.image, 
            nodes.colspec, 
            nodes.transition)

    def default_visit(self, node):
        pass

    def default_departure(self, node):
        pass

    def visit_Text(self, node):
        text = node.astext()
        self.output.append(text)

    def depart_Text(self, node):
        pass

    def visit_raw(self, node):
        self.default_visit(node)
        raise nodes.SkipNode

def setup(app):
    app.add_builder(PylitBuilder)

