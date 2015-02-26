from unittest import TestCase

import gcode2md


class FileTests(TestCase):
    def test_contributionFAQ(self):
        self.assert_convert("to_convert/ContributionFAQ.wiki", "expected/ContributionFAQ.md")

    def assert_convert(self, file_to_convert, file_expected):
        with open(file_expected) as f:
            expected = f.read()

        self.assertEqual(gcode2md.convert_to_md(file_to_convert), expected)
