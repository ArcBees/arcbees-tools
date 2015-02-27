import difflib
from unittest import TestCase

import gcode2md


class FileTests(TestCase):
    def test_ajax(self):
        self.assert_convert("to_convert/Ajax.wiki", "expected/Ajax.md")

    def test_contents(self):
        self.assert_convert("to_convert/Contents.wiki", "expected/Contents.md")

    def test_cssGuide(self):
        self.assert_convert("to_convert/CssGuide.wiki", "expected/CssGuide.md")

    def test_contributionFAQ(self):
        self.assert_convert("to_convert/ContributionFAQ.wiki", "expected/ContributionFAQ.md")

    def test_creatingNewApplications(self):
        self.assert_convert("to_convert/CreatingNewApplications.wiki", "expected/CreatingNewApplications.md")

    def test_dataBinding(self):
        self.assert_convert("to_convert/DataBinding.wiki", "expected/DataBinding.md")

    def test_developerCookbook(self):
        self.assert_convert("to_convert/DeveloperCookbook.wiki", "expected/DeveloperCookbook.md")

    def test_downloads(self):
        self.assert_convert("to_convert/Downloads.wiki", "expected/Downloads.md")

    def test_gettingStarted(self):
        self.assert_convert("to_convert/GettingStarted.wiki", "expected/GettingStarted.md")

    def test_gsocIdeas(self):
        self.assert_convert("to_convert/GSOC_Ideas.wiki", "expected/GSOC_Ideas.md")

    def test_homePageDraft(self):
        self.assert_convert("to_convert/HomePageDraft.wiki", "expected/HomePageDraft.md")

    def test_issues(self):
        self.assert_convert("to_convert/Issues.wiki", "expected/Issues.md")

    def test_jsQuery(self):
        self.assert_convert("to_convert/JsQuery.wiki", "expected/JsQuery.md")

    def test_promises(self):
        self.assert_convert("to_convert/Promises.wiki", "expected/Promises.md")

    def test_roadmap(self):
        self.assert_convert("to_convert/Roadmap.wiki", "expected/Roadmap.md")

    def test_sources(self):
        self.assert_convert("to_convert/Sources.wiki", "expected/Sources.md")

    def test_usingLatestSnapshot(self):
        self.assert_convert("to_convert/UsingLatestSnapshot.wiki", "expected/UsingLatestSnapshot.md")

    def test_writingPlugins(self):
        self.assert_convert("to_convert/WritingPlugins.wiki", "expected/WritingPlugins.md")

    def assert_convert(self, file_to_convert, file_expected):
        with open(file_expected) as f:
            expected = f.read()

        converted = gcode2md.convert_to_md(file_to_convert)

        self.assertMultiLineEqual(converted, expected, "\n\nDiff :\n\n" + self.diff(converted, expected))

    def diff(self, s1, s2):
        s1_arr = s1.splitlines(True)
        s2_arr = s2.splitlines(True)

        return "".join(difflib.unified_diff(s1_arr, s2_arr))
