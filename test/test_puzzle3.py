#!/usr/bin/env python3

import puzzle3
import unittest
import file_utils
import url_utils


class TestPuzzle3(unittest.TestCase):
    """ Several unit tests using a local test file named
        puzzle3_response_expected.txt.
        This avoids dependence on web request and response,
        reduces test scope and makes tests faster.
    """

    def setUp(self):
        self.test_url_utils = url_utils.UrlUtils()
        self.leader = "<!--\n"
        self.trailer = "\n-->\n"
        self.puzzle3 = puzzle3.Puzzle3()

    def test_get_mess_and_trailer(self):
        content = file_utils.FileUtils.get_file_string(
            "test/puzzle3_response_expected.txt")
        actual = url_utils.UrlUtils.get_mess_and_trailer(content, self.leader)
        self.assertEqual("kAewtloYgcFQ", actual[:12])

    def test_get_mess(self):
        """ Test read from test file.
        """
        content = file_utils.FileUtils.get_file_string(
            "test/puzzle3_response_expected.txt")
        actual = self.test_url_utils.get_mess(
            content, self.leader, self.trailer)
        self.assertEqual(101249, len(actual))
        expectedFileStringStart = "kAewtloYgcFQ"
        self.assertEqual(expectedFileStringStart,
                         actual[:len(expectedFileStringStart)])
        expectedFileStringEnd = "JkKbtSipiqBd"
        self.assertEqual(expectedFileStringEnd,
                         actual[(len(actual) - len(expectedFileStringStart)):])

    def test_get_matches(self):
        content = file_utils.FileUtils.get_file_string(
            "test/puzzle3_response_expected.txt")
        mess = self.test_url_utils.get_mess(content, self.leader, self.trailer)
        actual_matches = self.puzzle3.get_matches(mess)
        self.assertEqual(10, len(actual_matches))
        expectedFirstMatch = 'qIQNlQSLi'
        self.assertEqual(expectedFirstMatch, actual_matches[0])
        expectedLastMatch = 'qKWGtIDCj'
        self.assertEqual(expectedLastMatch, actual_matches[-1])

    def test_get_character_inside_match(self):
        actual = self.puzzle3.get_character_inside_match('qIQNlQSLi')
        self.assertEqual("l", actual)
        actual = self.puzzle3.get_character_inside_match('qKWGtIDCj')
        self.assertEqual("t", actual)

    def test_get_characters_inside_matches(self):
        content = file_utils.FileUtils.get_file_string(
            "test/puzzle3_response_expected.txt")
        mess = self.test_url_utils.get_mess(content, self.leader, self.trailer)
        actual = self.puzzle3.get_characters_inside_matches(mess)
        self.assertEqual("linkedlist", actual)

    def test_get_answer_url(self):
        """ This test makes a web request, doesn't use local test file
        """
        actual = self.puzzle3.get_answer_url()
        self.assertEqual(
            "http://www.pythonchallenge.com/pc/def/linkedlist.html", actual)

        # url http://www.pythonchallenge.com/pc/def/linkedlist.html
        # just says linkedlist.php
        # puzzle4 is at
        # http://www.pythonchallenge.com/pc/def/linkedlist.php
        # puzzle3 solution is listed at
        # http://www.pythonchallenge.com/pcc/def/linkedlist.php


if __name__ == "__main__":
    unittest.main()
