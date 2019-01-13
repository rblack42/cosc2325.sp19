# gitinclude - literalinclude from specific tag
from docutils import nodes
from git import Repo

#
#   .. gitinclude::
#       :repo: cpusim
#       :tag: v01
#       :lines: 
class GitDirectiveBase(Directive):

    def _find_repo(self):
        document = self.state.document
        env = document.settings.env
        repo_dir = self.options.get('repo-dir', env.srcdir)
        repo = Repo(repo_dir, search_parent_directories=True)
        return repo

class GitInclude(GitDirectiveBase):
    option_spec = {
        'repo-dir': six.text_type
    }

    def run(self):
        self.repo = self._find_repo()
        try:
            location = self.state.machine.get_source_and_line(self.lineno)
            rel_filename, filename = env.relfn2path(self.arguments[0])
            
            retnode = nodes.literal_block(text, test, source=filename)
        html = 'Repo: %s' % repo

def setup(app):
    app.add_config_value('git_root','/Users/rblack/_acc/_github')
    app.add_config_value('git_repo',
    app.add_directive('gitinclude', GitInclude)

