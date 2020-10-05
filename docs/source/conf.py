# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import subprocess
sys.path.insert(0, os.path.abspath('../../scripts'))


# -- Project information -----------------------------------------------------
AUTHOR='Spano Amara, Devènes Steve'
VERSION = "0.1.0"  # subprocess.check_output(["git", "describe"]).decode('UTF-8')

project = 'M05 miniProject'
copyright = '2020'
author = 'Spano Amara, Devènes Steve'

author = AUTHOR

# The short X.Y version
version = VERSION
# The full version, including alpha/beta/rc tags
release = VERSION

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    #'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx'
]

intersphinx_mapping = dict(
    python=('https://docs.python.org/3', None),
    numpy=("https://numpy.org/doc/stable/", None),
    scipy=("https://docs.scipy.org/doc/scipy/reference", None)
)

# Also document special classes like __init__
autoclass_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'pastie'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
# html_favicon = '../../img/***.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------
#autodoc_mock_imports = ['pandas']

napoleon_google_docstring = True
napoleon_numpy_docstring = False

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    #'vcs_pageview_mode': 'blob',
    #'style_nav_header_background': '#da0066',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False,
}

# html_context = {
#     "display_gitlab": True,
#     "gitlab_user": "",
#     "gitlab_repo": "",
#     "gitlab_version": "master",
#     "conf_py_path": "/docs/source/",
#     "gitlab_host": "",
#      }

# html_logo = '../../img/****.svg'
html_title = 'M05 MiniProject docs'

# Option for linkcheck
linkcheck_anchors=False
