"""Sphinx configuration for the ReguSync documentation."""

project = "ReguSync"
copyright = "2026, ReguSync authors"
author = "ReguSync authors"
release = "latest"

extensions = []
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_title = "ReguSync Documentation"
html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
}

html_context = {
    "display_github": True,
    "github_user": "ChrisOliver2345",
    "github_repo": "ReguSync-tutorial",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

epub_show_urls = "footnote"
