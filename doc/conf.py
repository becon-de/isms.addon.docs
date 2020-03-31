from __future__ import division, print_function, unicode_literals

from datetime import datetime

# -- Customized ---------------------------------------------------

html_title = "i-doit VIVA2 AddOn Dokumentation"
master_doc = 'index'
project = u'VIVA2'
#html_short_title = None
html_logo = 'img/Logo_VIVA2.png'
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
htmlhelp_basename = 'viva2'
html_theme = 'sphinx_rtd_theme'