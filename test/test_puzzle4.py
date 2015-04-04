#!/usr/bin/env python3

import puzzle4
import unittest
import url_utils


class TestPuzzle4(unittest.TestCase):

    def setUp(self):
        self.test_url_utils = url_utils.UrlUtils()
        self.puzzle4 = puzzle4.Puzzle4()

    def test_text_from_text_value_divided_by_2(self):
        expected = "8022"
        actual = self.puzzle4.text_from_text_value_divided_by_2("16044")
        self.assertEqual(expected, actual)

        expected = "4"
        actual = self.puzzle4.text_from_text_value_divided_by_2("9")
        self.assertEqual(expected, actual)

    def test_get_next_url(self):
        url1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
        url2 = self.puzzle4.get_next_url(url1)
        expected = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827"
        self.assertEqual(expected, url2)

        url3 = self.puzzle4.get_next_url(url2)
        expected = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=45439"
        self.assertEqual(expected, url3)

    def test_get_next_url_from_16044(self):
        url1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044"
        url2 = self.puzzle4.get_next_url(url1)
        expected = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"
        self.assertEqual(expected, url2)

    def test_get_text_from_url(self):
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
        expected = "and the next nothing is 44827"
        self.assertEqual(expected, self.puzzle4.get_text_from_url(url))

    def test_get_text_from_url_tired(self):
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=45439"
        expected = "<font color=red>Your hands are getting tired </font>and the next nothing is 94485"
        self.assertEqual(expected, self.puzzle4.get_text_from_url(url))

    def test_get_text_from_url_divide(self):
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044"
        expected = "Yes. Divide by two and keep going."
        self.assertEqual(expected, self.puzzle4.get_text_from_url(url))

    def test_get_text_from_url_peak(self):
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831"
        expected = "peak.html"
        self.assertEqual(expected, self.puzzle4.get_text_from_url(url))

    def test_get_next_url_from_text(self):
        text = "and the next nothing is 44827"
        expected = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827"
        self.assertEqual(expected, self.puzzle4.get_next_url_from_text(text))

    def test_get_next_url_from_text_tired(self):
        text  = "<font color=red>Your hands are getting tired </font>and the next nothing is 94485"
        expected = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=94485"
        self.assertEqual(expected, self.puzzle4.get_next_url_from_text(text))

    def test_get_next_url_from_text_peak(self):
        text = "peak.html"
        expected = "http://www.pythonchallenge.com/pc/def/peak.html"
        self.assertEqual(expected, self.puzzle4.get_next_url_from_text(text))

    def test_get_next_url_from_text_no_digits(self):
        text = "foo not percent escaped"
        expected = "http://www.pythonchallenge.com/pc/def/foo not percent escaped"
        self.assertEqual(expected, self.puzzle4.get_next_url_from_text(text))

    def test_get_url_digits_from_text_tired(self):
        text  = "<font color=red>Your hands are getting tired </font>and the next nothing is 94485"
        expected = "94485"
        self.assertEqual(expected, self.puzzle4.get_url_digits_from_text(text))

    def test_get_url_digits_from_text_peak(self):
        text = "peak.html"
        expected = ""
        self.assertEqual(expected, self.puzzle4.get_url_digits_from_text(text))

    def test_get_url_digits_from_text_no_digits_at_end(self):
        text = "123 not at end of string"
        expected = ""
        self.assertEqual(expected, self.puzzle4.get_url_digits_from_text(text))

    def test_get_url_for_url_start_count_max_2(self):
        url1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
        url_end = self.puzzle4.get_url_for_url_start_count_max(url1, 2)
        expected = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=45439"
        self.assertEqual(expected, url_end)

    def test_get_url_for_url_start_count_max_400(self):
        url1 = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
        url_end = self.puzzle4.get_url_for_url_start_count_max(url1, 400)
        expected = "http://www.pythonchallenge.com/pc/def/peak.html"
        self.assertEqual(expected, url_end)

if __name__ == "__main__":
    unittest.main()
