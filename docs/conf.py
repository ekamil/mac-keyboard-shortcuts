"""Sphinx configuration."""

project = "Mac Keyboard Shortcuts"
author = "Kamil E"
copyright = "2024, Kamil E"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
