# -*- coding: utf-8 -*-
""" ModelicaRes documentation build configuration file, created by
sphinx-quickstart on Mon Oct 15 09:06:21 2012.

This file is execfile()d with the current directory set to its containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out serve to
show the default.
"""

# Standard pylint settings for this project:
# pylint: disable=I0011, C0302, C0325, R0903, R0904, R0912, R0913, R0914, R0915,
# pylint: disable=I0011, W0141, W0142

# Other:
# pylint: disable=C0103

def skip(app, what, name, obj, skip, options):
    """Include otherwise hidden methods.
    """
    # pylint: disable=W0613
    if name in ["__call__", "__contains__", "__getitem__", "__len__"]:
        return False
    return skip

def setup(app):
    """Add roles and javascripts.
    """
    app.connect("autodoc-skip-member", skip)
    app.add_javascript('copybutton.js')
    app.add_javascript('analytics.js')

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.pngmath',
              'matplotlib.sphinxext.plot_directive'
             ]
# Note: sphinx.ext.autosummary produces a table, but I'd rather have a bulleted
# list.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'ModelicaRes'
copyright = ('2012-2014, Kevin Davies, Hawaii Natural Energy Institute, and '
             'Georgia Tech Research Corporation')

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import modelicares
version = modelicares.__version__
if not version:
    version = ''
# The full version, including alpha/beta/rc tags.
release = version

# List of documents that shouldn't be included in the build.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for a
# list of builtin themes.
html_theme = 'default'

html_theme_options = {
    'stickysidebar': True,
    'sidebarbgcolor': '#888888',
    'sidebartextcolor': 'white',
    'sidebarlinkcolor': 'white',
}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Analyze Modelica results in Python"

# A shorter title for the navigation bar.  Default is the same as html_title.
version_str = " v%s" % version if version else ''
html_short_title = project + version_str + " Documentation"

# The name of an image file (relative to this directory) to place at the top of
# the sidebar.
html_logo = '_static/logo.gif'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files, so
# a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_style = 'custom.css'

# List of paths that contain extra files not directly related to the
# documentation
html_extra_path = ['extra']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['globaltoc.html', 'searchbox.html', 'download.html']}

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = False

# Output file base name for HTML help builder.
htmlhelp_basename = 'ModelicaResDoc'

math_output = 'MathML'
