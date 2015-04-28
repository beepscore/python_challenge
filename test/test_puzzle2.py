#!/usr/bin/env python3

import puzzle2
import unittest
import file_utils
import url_utils


class TestPuzzle2(unittest.TestCase):
    """ Use test file puzzle2_response_expected.txt in place of web response.
        This reduces test scope and makes tests faster.
    """

    def setUp(self):
        self.leader = "mess below:\n-->\n\n<!--\n"
        self.trailer = "\n-->"
        self.puzzle2 = puzzle2.Puzzle2()

    def test_get_character_counts(self):
        content = file_utils.FileUtils.get_file_string(
            "test/puzzle2_response_expected.txt")
        mess = url_utils.UrlUtils.get_mess(content, self.leader, self.trailer)
        character_counts = self.puzzle2.get_character_counts(mess)
        self.assertEqual(25, len(character_counts))

    def test_get_string_from_unique_chars(self):
        content = file_utils.FileUtils.get_file_string(
            "test/puzzle2_response_expected.txt")
        mess = url_utils.UrlUtils.get_mess(content, self.leader, self.trailer)
        # next puzzle puzzle3 url is at 'equality'
        # http://www.pythonchallenge.com/pc/def/equality.html
        self.assertEqual("equality",
                         self.puzzle2.get_string_from_unique_chars(mess))


if __name__ == "__main__":
    unittest.main()
