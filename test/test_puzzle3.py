#!/usr/bin/env python3

import puzzle3
import unittest
import file_utils
import url_utils


class TestPuzzle3(unittest.TestCase):
    """ Most tests use file puzzle3_response_expected.txt in place of web response.
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

    def test_get_matches(self):
        content = self.test_file_utils.get_file_string(
            "test/puzzle3_response_expected.txt")
        mess = self.test_url_utils.get_mess(content, self.leader, self.trailer)
        actual = self.puzzle3.get_matches(mess)
        self.assertEqual(10, len(actual))
        self.assertEqual('qIQNlQSLi', actual[0])

    def test_get_characters_inside_matches(self):
        content = self.test_file_utils.get_file_string(
            "test/puzzle3_response_expected.txt")
        mess = self.test_url_utils.get_mess(content, self.leader, self.trailer)
        actual = self.puzzle3.get_characters_inside_matches(mess)
        self.assertEqual("linkedlist", actual)
        # http://www.pythonchallenge.com/pc/def/linkedlist.html
        # says linkedlist.php
        # go to http://www.pythonchallenge.com/pc/def/linkedlist.php

    def test_get_answer_url(self):
        """ This test makes a web request instead of using test file
        """
        actual = self.puzzle3.get_answer_url()
        self.assertEqual(
            "http://www.pythonchallenge.com/pc/def/linkedlist.html", actual)


if __name__ == "__main__":
    unittest.main()
