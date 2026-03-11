import datetime

project = "Lihzahrd"
author = "Stefano Pigozzi"
project_copyright = f"{datetime.date.today().year} {author} -"

language = "en"

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.14", None),
    "numpy": ("https://numpy.org/doc/2.4", None),
    "bs4": ("https://www.crummy.com/software/BeautifulSoup/bs4/doc", None),
}
manpages_url = "https://man.archlinux.org/"


def skip(app, what, name: str, obj, would_skip, options):
    if name == "__init__" or name == "__getitem__" or name == "__getattr__":
        return not bool(obj.__doc__)
    return would_skip


todo_include_todos = True
todo_emit_warnings = True
todo_link_only = False

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_title = f"{project}"
html_short_title = f"{project}"
html_static_path = [
    "_static",
]
html_css_files = ["custom.css"]
html_extra_path = [
    "_extra",
]
html_domain_indices = False
html_context = {}
html_permalinks_icon = "<span>¶</span>"
html_theme = "furo"
html_theme_options = dict(
    footer_icons=[
        dict(
            name="Leave a tip",
            html="""
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2024 Fonticons, Inc. --><path fill="currentColor" d="M128 144a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm120.8-32.6c.6-.9 1.8-2.1 4.2-3.4c5.1-2.7 12.5-4.1 18.7-4c8.2 .1 17.1 1.8 26.4 4.1c8.6 2.1 17.3-3.1 19.4-11.7s-3.1-17.3-11.7-19.4c-5.6-1.4-11.6-2.7-17.9-3.7l0-9.4c0-8.8-7.2-16-16-16s-16 7.2-16 16l0 9.5c-6.1 1.2-12.3 3.2-18 6.3c-11.8 6.3-23 18.4-21.8 37.2c1 16 11.7 25.3 21.6 30.7c8.8 4.7 19.7 7.8 28.6 10.3l1.8 .5c10.3 2.9 17.9 5.2 23.2 8.3c4.5 2.7 4.7 4.2 4.7 5.6c.1 2.4-.5 3.7-1 4.5c-.6 1-1.8 2.2-4 3.3c-4.7 2.5-11.8 3.8-18.5 3.6c-9.5-.3-18.5-3.1-29.9-6.8c-1.9-.6-3.8-1.2-5.8-1.8c-8.4-2.6-17.4 2.1-20 10.5s2.1 17.4 10.5 20c1.6 .5 3.3 1 5 1.6c0 0 0 0 0 0s0 0 0 0c7.1 2.3 15.1 4.9 23.7 6.6l0 11.4c0 8.8 7.2 16 16 16s16-7.2 16-16l0-10.8c6.2-1.1 12.5-3.1 18.3-6.2c12.1-6.5 22.3-18.7 21.7-36.9c-.5-16.2-10.3-26.3-20.5-32.3c-9.4-5.6-21.2-8.9-30.5-11.5l-.2 0c-10.4-2.9-18.3-5.2-23.9-8.2c-4.8-2.6-4.8-4-4.8-4.5c0 0 0 0 0-.1c-.1-1.9 .3-2.9 .8-3.6zM568.2 336.3c13.1 17.8 9.3 42.8-8.5 55.9L433.1 485.5c-23.4 17.2-51.6 26.5-80.7 26.5L192 512 32 512c-17.7 0-32-14.3-32-32l0-64c0-17.7 14.3-32 32-32l36.8 0 44.9-36c22.7-18.2 50.9-28 80-28l78.3 0 16 0 64 0c17.7 0 32 14.3 32 32s-14.3 32-32 32l-64 0-16 0c-8.8 0-16 7.2-16 16s7.2 16 16 16l120.6 0 119.7-88.2c17.8-13.1 42.8-9.3 55.9 8.5zM193.6 384c0 0 0 0 0 0l-.9 0c.3 0 .6 0 .9 0z"/></svg>
            """,
            url="https://ko-fi.com/steffo",
        ),
        dict(
            name="Source code",
            html="""
            <svg height="16px" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2024 Fonticons, Inc. --><path fill="currentColor" d="M80 104a24 24 0 1 0 0-48 24 24 0 1 0 0 48zm80-24c0 32.8-19.7 61-48 73.3l0 87.8c18.8-10.9 40.7-17.1 64-17.1l96 0c35.3 0 64-28.7 64-64l0-6.7C307.7 141 288 112.8 288 80c0-44.2 35.8-80 80-80s80 35.8 80 80c0 32.8-19.7 61-48 73.3l0 6.7c0 70.7-57.3 128-128 128l-96 0c-35.3 0-64 28.7-64 64l0 6.7c28.3 12.3 48 40.5 48 73.3c0 44.2-35.8 80-80 80s-80-35.8-80-80c0-32.8 19.7-61 48-73.3l0-6.7 0-198.7C19.7 141 0 112.8 0 80C0 35.8 35.8 0 80 0s80 35.8 80 80zm232 0a24 24 0 1 0 -48 0 24 24 0 1 0 48 0zM80 456a24 24 0 1 0 0-48 24 24 0 1 0 0 48z"/></svg>
            """,
            url="https://forge.steffo.eu/steffo/lihzahrd",
        ),
        dict(
            name="PyPI",
            html="""
            <svg height="16px" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2024 Fonticons, Inc. --><path fill="currentColor" d="M50.7 58.5L0 160l208 0 0-128L93.7 32C75.5 32 58.9 42.3 50.7 58.5zM240 160l208 0L397.3 58.5C389.1 42.3 372.5 32 354.3 32L240 32l0 128zm208 32L0 192 0 416c0 35.3 28.7 64 64 64l320 0c35.3 0 64-28.7 64-64l0-224z"/></svg>
            """,
            url="https://pypi.org/project/lihzahrd/",
        ),
    ]
)

pygments_style = "default"
pygments_dark_style = "monokai"

autodoc_default_options = {
    "members": True,
    "special-members": "__str__, __bool__, __iter__, __eq__, __ne__",
    "member-order": "bysource",
}
autodoc_inherit_docstrings = False
