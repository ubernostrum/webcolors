import os
import sys

on_rtd = os.environ.get("READTHEDOCS", None) == "True"

extensions = ["sphinx.ext.intersphinx"]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = "webcolors"
copyright = "2008-2022, James Bennett"
version = "1.12"
release = "1.12"
exclude_trees = ["_build"]
pygments_style = "sphinx"
htmlhelp_basename = "webcolorsdoc"
latex_documents = [
    ("index", "webcolors.tex", "webcolors Documentation", "James Bennett", "manual"),
]
if not on_rtd:
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

if not on_rtd:
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Spelling check needs an additional module that is not installed by default.
# Add it only if spelling check is requested so docs can be generated without it.
if "spelling" in sys.argv:
    extensions.append("sphinxcontrib.spelling")

# Spelling language.
spelling_lang = "en_US"

# Location of word list.
spelling_word_list_filename = "spelling_wordlist.txt"
