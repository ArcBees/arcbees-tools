# Google Code Wiki to GitHub Flavored Markdown
Convert documentation from Google Code to GitHub.

For example outputs, see the test folder (e.g. converting `to_convert/GettingStarted.wiki` will generate `expected/GettingStarted.md`).

## Usage

```
$ python googlecode_wiki_to_github_markdown.py -h
usage: googlecode_wiki_to_github_markdown.py [-h] [-p PROJECT_NAME] [-f] path

Outputs to path/output, or stdout if -f specified

positional arguments:
  path                  path to directory containing .wiki files, or to the file if -f specified

optional arguments:
  -h, --help            show this help message and exit
  -p PROJECT_NAME, --project-name PROJECT_NAME
                        used to remove internal wiki links cancellation
                        (see https://code.google.com/p/support/wiki/WikiSyntax#Internal_wiki_links)
                        will simply skip this step if not specified
  -f, --file            convert file instead of directory
```

Examples:
* Script in same folder than .wiki files:

```
$ python googlecode_wiki_to_github_markdown.py .
```

* In this project root file:

```
$ python googlecode_wiki_to_github_markdown.py -p GwtQuery test/to_convert/
```

* Single file:

```
$ python googlecode_wiki_to_github_markdown.py -p GwtQuery -f test/to_convert/GettingStarted.wiki
```

## Running tests
In the root folder, run any of these commands:

```
$ python -m test.file_tests
$ python -m unittest test.file_tests
```

Or you can add the root folder to your `PYTHONPATH` and run the test file directly.

## Python version
Works for both python2 and python3. You can run the tests to confirm.
