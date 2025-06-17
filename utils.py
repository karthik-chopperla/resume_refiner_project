def text_diff(original, revised):
    import difflib
    d = difflib.HtmlDiff()
    return d.make_table(original.splitlines(), revised.splitlines(), fromdesc='Original', todesc='Refined')
