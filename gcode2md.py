import re
import sys


def convert_to_md(wiki_file):
    with open(wiki_file) as f:
        wiki = f.read()

    wiki = remove_gplusone(wiki)
    wiki = replace_code_snippets(wiki)

    return wiki


def remove_gplusone(wiki):
    return re.sub(r"<g:plusone.*</g:plusone>", "", wiki)


def replace_code_snippets(wiki):
    return wiki.replace("{{{", "\n```").replace("}}}", "```\n")


if __name__ == '__main__':
    print(convert_to_md(sys.argv[1]))
