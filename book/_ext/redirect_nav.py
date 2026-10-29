"""Skip redirect-only pages in the previous page link.

The next page link is left untouched, so it follows the table of contents and
the redirect takes the reader to the first real page of the section.
"""


def _skip_redirects(app, pagename, templatename, context, doctree):
    redirects = getattr(app.config, "redirects", None) or {}
    env = app.env

    target = context.get("prev")
    if not target:
        return
    original = docname = _docname(app, pagename, target)
    while docname in redirects:
        docname = app.builder.relations.get(docname, (None, None, None))[1]
    if docname is None:
        context["prev"] = None
        return

    relations = app.builder.relations
    parent = relations.get(docname, (None, None, None))[0]
    current_parent = relations.get(pagename, (None, None, None))[0]
    title = app.builder.render_partial(env.titles[docname])["title"]
    prefixed = parent in redirects and parent != current_parent and parent != pagename
    if prefixed:
        parent_title = app.builder.render_partial(env.titles[parent])["title"]
        title = f"{parent_title} - {title}"

    if prefixed or docname != original:
        context["prev"] = {
            "link": app.builder.get_relative_uri(pagename, docname),
            "title": title,
        }


def _docname(app, pagename, target):
    for docname in app.env.found_docs:
        if app.builder.get_relative_uri(pagename, docname) == target["link"]:
            return docname
    return None


def setup(app):
    app.connect("html-page-context", _skip_redirects)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
