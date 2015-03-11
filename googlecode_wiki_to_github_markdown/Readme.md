# Google Code Wiki to GitHub Flavored Markdown
Convert documentation from Google Code to GitHub.

For example outputs, see the test folder (e.g. converting `to_convert/GettingStarted.wiki` will generate `expected/GettingStarted.md`).

## Usage

```
$ python googlecode_wiki_to_github_markdown.py -h
usage: googlecode_wiki_to_github_markdown.py [-h] [--file FILE | dir]

positional arguments:
  dir          path to directory containing .wiki files
               defaults to current directory
               outputs to dir/output/

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  convert file instead of directory, result printed to stdout
```

Examples:
* In folder containing .wiki files : `$ python googlecode_wiki_to_github_markdown.py`
* In this project root file : `$ python googlecode_wiki_to_github_markdown.py test/to_convert/`
* Single file : `$ python googlecode_wiki_to_github_markdown.py --file test/to_convert/GettingStarted.wiki`

_(Optional)_
Update the `project_name` constant (used to remove internal wiki links cancellation:
https://code.google.com/p/support/wiki/WikiSyntax#Internal_wiki_links).

## Running tests
In the root folder, run any of these commands:

```
$ python -m test.file_tests
$ python -m unittest test.file_tests
```

Or you can add the root folder to your `PYTHONPATH` and run the test file directly.

## Python version
Works for both python2 and python3. You can run the tests to confirm.
