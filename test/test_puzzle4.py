#!/usr/bin/env python3

import puzzle4
import unittest
import url_utils


class TestPuzzle4(unittest.TestCase):

    def setUp(self):
        self.test_url_utils = url_utils.UrlUtils()
        self.puzzle4 = puzzle4.Puzzle4()

    def test_get_next_url(self):
        url1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
        url2 = self.puzzle4.get_next_url(url1)
        expected = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827"
        self.assertEqual(expected, url2)

        url3 = self.puzzle4.get_next_url(url2)
        expected = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=45439"
        self.assertEqual(expected, url3)

    def test_get_text_from_url(self):
        url1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
        expected = "and the next nothing is 44827"
        self.assertEqual(expected, self.puzzle4.get_text_from_url(url1))

    def test_get_nothing_digits_from_text(self):
        text = "and the next nothing is 44827"
        expected = "44827"
        self.assertEqual(expected, self.puzzle4.get_nothing_digits_from_text(text))

    def test_get_url_from_nothing_digits(self):
        nothing_digits = "44827"
        expected = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827"
        self.assertEqual(expected, self.puzzle4.get_url_from_nothing_digits(nothing_digits))


if __name__ == "__main__":
    unittest.main()
