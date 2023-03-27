"""
Configuration file for the Sphinx documentation builder:

https://www.sphinx-doc.org/

"""
import sys

extensions = [
    "notfound.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = "webcolors"
copyright = "2008, James Bennett"
version = "1.13"
release = "1.13"
exclude_trees = ["_build"]
pygments_style = "sphinx"
htmlhelp_basename = "webcolorsdoc"
latex_documents = [
    ("index", "webcolors.tex", "webcolors Documentation", "James Bennett", "manual"),
]
html_theme = "furo"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Spelling check needs an additional module that is not installed by default.
# Add it only if spelling check is requested so docs can be generated without it.
if "spelling" in sys.argv:
    extensions.append("sphinxcontrib.spelling")

# Spelling language.
spelling_lang = "en_US"

# Location of word list.
spelling_word_list_filename = "spelling_wordlist.txt"

# Doctest configuration.
doctest_global_setup = "from webcolors import *"

# OGP metadata configuration.
ogp_enable_meta_description = True
ogp_site_url = "https://webcolors.readthedocs.io/"
