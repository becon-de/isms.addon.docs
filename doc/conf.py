from __future__ import division, print_function, unicode_literals

from datetime import datetime

# -- Customized ---------------------------------------------------

html_title = "i-doit ISMS Add-on Dokumentation"
master_doc = 'index'
project = u'ISMS'
#html_short_title = None
html_logo = 'img/Logo_ISMS.png'
html_favicon = 'img/favicon32x32.png'
numpydoc_show_class_members = False
class_members_toctree = False
file_insertion_enabled = False
extensions = ['sphinx.ext.intersphinx']

source_suffix = ['.rst','.md']
copyright = str(datetime.now().year)
version = 'latest'
release = 'latest'
exclude_patterns = ['_build']
htmlhelp_basename = 'ISMS'
html_theme = 'sphinx_rtd_theme'
highlight_language ='none'

def setup(app):
    app.add_stylesheet('css/custom.css')