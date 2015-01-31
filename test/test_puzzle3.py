#!/usr/bin/env python3

import puzzle3
import unittest
import file_utils
import url_utils


class TestPuzzle3(unittest.TestCase):
    """ Use test file puzzle3_response_expected.txt in place of web response.
        This reduces test scope and makes tests faster.
    """

    def setUp(self):
        self.test_file_utils = file_utils.FileUtils()
        self.test_url_utils = url_utils.UrlUtils()
        self.leader = "<!--\n"
        self.trailer = "\n-->\n"
        self.puzzle3 = puzzle3.Puzzle3()

    def test_get_mess_and_trailer(self):
        content = self.test_file_utils.get_file_string(
            "test/puzzle3_response_expected.txt")
        actual = self.test_url_utils.get_mess_and_trailer(content, self.leader)
        self.assertEqual("kAewtloYgcFQ", actual[:12])

    def test_get_mess(self):
        content = self.test_file_utils.get_file_string(
            "test/puzzle3_response_expected.txt")
        actual = self.test_url_utils.get_mess(
            content, self.leader, self.trailer)
        self.assertEqual(101249, len(actual))
        # test start
        self.assertEqual("kAewtloYgcFQ", actual[:12])
        # test end
        self.assertEqual("JkKbtSipiqBd", actual[len(actual)-12:])

    def test_get_character_and_uppercase_bodyguards(self):
        content = self.test_file_utils.get_file_string(
            "test/puzzle3_response_expected.txt")
        mess = self.test_url_utils.get_mess(content, self.leader, self.trailer)
        actual = self.puzzle3.get_character_and_uppercase_bodyguards(mess)
        # character is j
        self.assertEqual("WDZjUZM", actual)
        # both these urls return 404 not found
        # http://www.pythonchallenge.com/pc/def/j.html
        # http://www.pythonchallenge.com/pc/def/WDZjUZM.html

if __name__ == "__main__":
    unittest.main()
