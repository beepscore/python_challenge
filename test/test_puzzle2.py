#!/usr/bin/env python3

import puzzle2
import unittest
import file_utils


class TestPuzzle2(unittest.TestCase):

    def setUp(self):
        self.leader = "mess below:\n-->\n\n<!--\n"
        self.trailer = "\n-->"

    def test_get_response(self):
        actual = puzzle2.get_response(
            "http://www.pythonchallenge.com/pc/def/ocr.html")
        self.assertIsNotNone(actual)
        # printing response shows prefix b', indicating type is bytes
        # http://stackoverflow.com/questions/2592764/what-does-a-b-prefix-before-a-python-string-mean
        # http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python
        # print(actual)
        self.assertFalse(isinstance(actual, str))
        self.assertTrue(isinstance(actual, bytes))

    def test_bytes_to_string(self):
        test_file_utils = file_utils.FileUtils()
        expected = test_file_utils.get_file_string(
            "test/puzzle2_response_expected.txt")

        actual_bytes = puzzle2.get_response(
            "http://www.pythonchallenge.com/pc/def/ocr.html")
        actual_string = puzzle2.string_from_bytes(actual_bytes)
        self.assertEqual(99613, len(actual_string))
        self.assertEqual(expected, actual_string)

    def test_get_mess_and_trailer(self):
        test_file_utils = file_utils.FileUtils()
        content = test_file_utils.get_file_string(
            "test/puzzle2_response_expected.txt")
        actual = puzzle2.get_mess_and_trailer(content, self.leader)
        self.assertEqual("%%$@_$^__#)^", actual[:12])

    def test_get_mess(self):
        test_file_utils = file_utils.FileUtils()
        content = test_file_utils.get_file_string(
            "test/puzzle2_response_expected.txt")
        actual = puzzle2.get_mess(
            content, self.leader, self.trailer)
        self.assertEqual(98764, len(actual))
        # test start
        self.assertEqual("%%$@_$^__#)^", actual[:12])
        # test end
        self.assertEqual(")$!%{(}$^$}*", actual[len(actual)-12:])

    def test_get_character_counts(self):
        test_file_utils = file_utils.FileUtils()
        content = test_file_utils.get_file_string(
            "test/puzzle2_response_expected.txt")
        mess = puzzle2.get_mess(content, self.leader, self.trailer)
        character_counts = puzzle2.get_character_counts(mess)
        self.assertEqual(25, len(character_counts))

    def test_get_string_from_unique_chars(self):
        test_file_utils = file_utils.FileUtils()
        content = test_file_utils.get_file_string(
            "test/puzzle2_response_expected.txt")
        mess = puzzle2.get_mess(content, self.leader, self.trailer)
        # next puzzle puzzle3 url is at 'equality'
        # http://www.pythonchallenge.com/pc/def/equality.html
        self.assertEqual("equality", puzzle2.get_string_from_unique_chars(mess))


if __name__ == "__main__":
    unittest.main()
