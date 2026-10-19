# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import importlib.metadata

_python_project_name = "lrctoolbox"
version = importlib.metadata.version(_python_project_name)
project = "LRCToolbox"
copyright = "2023-%Y, Dr-Blank"
author = "Dr-Blank"
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # to generate the docs from the docstrings
    "sphinx.ext.autosectionlabel",  # to reference sections by title
    "sphinx.ext.intersphinx",  # to link to the Python docs
    "sphinx.ext.napoleon",  # to support the Google and NumPy docstrings
    "sphinx.ext.todo",  # to document the todos
    "sphinx.ext.viewcode",  # to generate the source code
    "myst_nb",  # to support Markdown and Jupyter notebooks
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
autosectionlabel_prefix_document = True
autodoc_typehints = "description"
autodoc_member_order = "bysource"
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

# notebooks are rendered with their saved outputs, never executed
nb_execution_mode = "off"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = f"{project} {release}"
html_theme_options = {
    "source_repository": "https://github.com/Dr-Blank/lrctoolbox/",
    "source_branch": "main",
    "source_directory": "docs/",
}
