import difflib
import unittest
import os

import googlecode_wiki_to_github_markdown


def get_to_convert_path(filename):
    return os.path.join(os.path.dirname(__file__), "to_convert", filename)


def get_expected_path(filename):
    return os.path.join(os.path.dirname(__file__), "expected", filename)


class FileTests(unittest.TestCase):
    def test_ajax(self):
        self.assert_convert("Ajax.wiki", "Ajax.md")

    def test_contents(self):
        self.assert_convert("Contents.wiki", "Contents.md")

    def test_cssGuide(self):
        self.assert_convert("CssGuide.wiki", "CssGuide.md")

    def test_contributionFAQ(self):
        self.assert_convert("ContributionFAQ.wiki", "ContributionFAQ.md")

    def test_creatingNewApplications(self):
        self.assert_convert("CreatingNewApplications.wiki", "CreatingNewApplications.md")

    def test_dataBinding(self):
        self.assert_convert("DataBinding.wiki", "DataBinding.md")

    def test_developerCookbook(self):
        self.assert_convert("DeveloperCookbook.wiki", "DeveloperCookbook.md")

    def test_downloads(self):
        self.assert_convert("Downloads.wiki", "Downloads.md")

    def test_gettingStarted(self):
        self.assert_convert("GettingStarted.wiki", "GettingStarted.md")

    def test_gsocIdeas(self):
        self.assert_convert("GSOC_Ideas.wiki", "GSOC_Ideas.md")

    def test_homePageDraft(self):
        self.assert_convert("HomePageDraft.wiki", "HomePageDraft.md")

    def test_issues(self):
        self.assert_convert("Issues.wiki", "Issues.md")

    def test_jsQuery(self):
        self.assert_convert("JsQuery.wiki", "JsQuery.md")

    def test_promises(self):
        self.assert_convert("Promises.wiki", "Promises.md")

    def test_roadmap(self):
        self.assert_convert("Roadmap.wiki", "Roadmap.md")

    def test_sources(self):
        self.assert_convert("Sources.wiki", "Sources.md")

    def test_usingLatestSnapshot(self):
        self.assert_convert("UsingLatestSnapshot.wiki", "UsingLatestSnapshot.md")

    def test_writingPlugins(self):
        self.assert_convert("WritingPlugins.wiki", "WritingPlugins.md")

    def assert_convert(self, file_to_convert, file_expected):
        with open(get_expected_path(file_expected)) as f:
            expected = f.read()

        converted = googlecode_wiki_to_github_markdown.convert_to_md(get_to_convert_path(file_to_convert))

        self.assertMultiLineEqual(converted, expected, "\n\nDiff :\n\n" + self.diff(converted, expected))

    def diff(self, s1, s2):
        s1_arr = s1.splitlines(True)
        s2_arr = s2.splitlines(True)

        return "".join(difflib.unified_diff(s1_arr, s2_arr))


if __name__ == '__main__':
    unittest.main()
