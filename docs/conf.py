import datetime

project = "lihzahrd"
author = "Stefano Pigozzi"
project_copyright = f'{datetime.date.today().year}, {author}'

language = "en"

html_theme_options = {
    # Set this to the main color of your project
    "style_nav_header_background": "#7FA23E",
}
html_context = {}

extensions = [
    "sphinx.ext.napoleon", 
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.13", None),
}
manpages_url = "https://man.archlinux.org/"

napoleon_use_param = True

def skip(app, what, name: str, obj, would_skip, options):
    if name == "__init__" or name == "__getitem__" or name == "__getattr__":
        return not bool(obj.__doc__)
    return would_skip

todo_include_todos = True
todo_emit_warnings = True
todo_link_only = False

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = 'sphinx_rtd_theme'
html_title = f"{project}"
html_short_title = f"{project}"
html_static_path = [
    "_static",
]
html_extra_path = [
    "_extra",
]
html_domain_indices = False
