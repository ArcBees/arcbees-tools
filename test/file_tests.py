import difflib
from unittest import TestCase

import gcode2md


class FileTests(TestCase):
    def test_contributionFAQ(self):
        self.assert_convert("to_convert/ContributionFAQ.wiki", "expected/ContributionFAQ.md")

    def assert_convert(self, file_to_convert, file_expected):
        with open(file_expected) as f:
            expected = f.read()

        converted = gcode2md.convert_to_md(file_to_convert)

        self.assertMultiLineEqual(converted, expected, "\n\nDiff :\n\n" + self.diff(converted, expected))

    def diff(self, s1, s2):
        # split on newlines but keep them
        s1_arr = [line + '\n' for line in s1.split('\n')]
        s2_arr = [line + '\n' for line in s2.split('\n')]

        return "".join(difflib.unified_diff(s1_arr, s2_arr))
