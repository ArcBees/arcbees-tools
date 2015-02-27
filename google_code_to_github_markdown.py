import re
import sys

# Used to remove internal wiki links cancellation :
# https://code.google.com/p/support/wiki/WikiSyntax#Internal_wiki_links
project_name = "GwtQuery"


def convert_to_md(wiki_file_name):
    with open(wiki_file_name) as f:
        wiki = f.read()

    wiki = remove_gplusone(wiki)
    wiki = remove_toc(wiki)
    wiki = remove_labels(wiki)
    wiki = remove_internal_link_cancellations(wiki)

    wiki = convert_internal_links(wiki)
    wiki = convert_http_links(wiki)
    wiki = convert_numbered_lists(wiki)
    wiki = convert_headers(wiki)
    wiki = convert_code_snippets_markers(wiki)
    wiki = convert_comments(wiki)

    wiki = remove_extra_spaces(wiki)
    wiki = remove_extra_empty_lines(wiki)

    return wiki


def remove_gplusone(wiki):
    return re.sub(r"<g:plusone.*</g:plusone>", "", wiki)


def remove_toc(wiki):
    return re.sub(r"<wiki:toc.*/>", "", wiki)


def remove_labels(wiki):
    return re.sub(r"#labels.*", "", wiki)


def remove_internal_link_cancellations(wiki):
    return wiki.replace("!" + project_name, project_name)


def convert_internal_links(wiki):
    for line in lines_not_in_code_snippets(wiki):
        # [Example] -> [Example](Example.md)
        replaced_line = re.sub(r"\[(?!http)([^ ]*)\]", r"[\1](\1.md)", line)
        # [Example#example() link description] -> [link description](Example.md#example)
        replaced_line = re.sub(r"\[(?!http)([^ #\(]*?)(|#[^\(]*?)(?:\(\))? +(.*?)\]", r"[\3](\1.md\2)", replaced_line)
        if line != replaced_line:
            wiki = wiki.replace(line, replaced_line)

    return wiki


def convert_http_links(wiki):
    # Link only between brackets (no spaces) -> Remove brackets and ensure space after
    wiki = re.sub(r"\[(http[^ ]*?)\] *", r"\1 ", wiki)
    # Link with description
    wiki = re.sub(r"\[(http.*?) +(.*?)\]", r"[\2](\1)", wiki)
    return wiki


def convert_code_snippets_markers(wiki):
    wiki = re.sub(r" *\{\{\{", "\n```", wiki)
    wiki = re.sub(r" *\}\}\}", "```\n", wiki)
    return wiki


def convert_comments(wiki):
    return wiki.replace("<wiki:comment>", "<!---").replace("</wiki:comment>", "-->")


def convert_numbered_lists(wiki):
    for line in lines_not_in_code_snippets(wiki):
        replaced_line = line.replace("# ", "1. ")
        if line != replaced_line:
            wiki = wiki.replace(line, replaced_line)

    return wiki


def convert_headers(wiki):
    wiki = re.sub(r"^====== ?(.*[^ ]) ?======", r"###### \1", wiki, flags=re.MULTILINE)
    wiki = re.sub(r"^===== ?(.*[^ ]) ?=====", r"##### \1", wiki, flags=re.MULTILINE)
    wiki = re.sub(r"^==== ?(.*[^ ]) ?====", r"#### \1", wiki, flags=re.MULTILINE)
    wiki = re.sub(r"^=== ?(.*[^ ]) ?===", r"### \1", wiki, flags=re.MULTILINE)
    wiki = re.sub(r"^== ?(.*[^ ]) ?==", r"## \1", wiki, flags=re.MULTILINE)
    wiki = re.sub(r"^= ?(.*[^ ]) ?=", r"# \1", wiki, flags=re.MULTILINE)

    wiki = replace_summary(wiki)

    return wiki


def replace_summary(wiki):
    """If there is a #summary tag, set all headers one level below (e.g. # -> ##) and set #summary as h1"""
    if "#summary" in wiki:
        wiki = wiki.replace("# ", "## ")
        wiki = wiki.replace("#summary", '#')
    return wiki


def remove_extra_spaces(wiki):
    return "\n".join(line.rstrip() for line in wiki.splitlines())


def remove_extra_empty_lines(wiki):
    wiki = re.sub("\n\n+", "\n\n", wiki)  # no more than 1 empty line
    wiki = re.sub("^\n*", "", wiki)  # remove empty lines at beginning of file
    wiki = re.sub("\n*$", "\n", wiki)  # only one line at end of file

    return wiki


def lines_not_in_code_snippets(wiki):
    in_snippets = False
    for line in wiki.splitlines():
        if "{{{" in line:
            in_snippets = True
            continue
        elif "}}}" in line:
            in_snippets = False
            continue

        if not in_snippets:
            yield line


if __name__ == '__main__':
    print(convert_to_md(sys.argv[1]))
