#!/usr/bin/env python3

import unittest
import file_utils
import url_utils


class TestUrlUtils(unittest.TestCase):

    def setUp(self):
        self.test_file_utils = file_utils.FileUtils()
        self.test_url_utils = url_utils.UrlUtils()
        self.leader = "mess below:\n-->\n\n<!--\n"
        self.trailer = "\n-->"

    def test_get_response(self):
        actual = self.test_url_utils.get_response(
            "http://www.pythonchallenge.com/pc/def/ocr.html")
        self.assertIsNotNone(actual)
        # printing response shows prefix b', indicating type is bytes
        # http://stackoverflow.com/questions/2592764/what-does-a-b-prefix-before-a-python-string-mean
        # http://stackoverflow.com/questions/1549801/differences-between-isinstance-and-type-in-python
        # print(actual)
        self.assertFalse(isinstance(actual, str))
        self.assertTrue(isinstance(actual, bytes))

    def test_bytes_to_string(self):
        """ Get url response, convert bytes to string,
        and compare to puzzle2_response_expected.txt
        """
        expected = self.test_file_utils.get_file_string(
            "test/puzzle2_response_expected.txt")

        actual_bytes = self.test_url_utils.get_response(
            "http://www.pythonchallenge.com/pc/def/ocr.html")
        actual_string = self.test_url_utils.string_from_bytes(actual_bytes)
        self.assertEqual(99613, len(actual_string))
        self.assertEqual(expected, actual_string)

    def test_get_mess_and_trailer(self):
        content = self.test_file_utils.get_file_string(
            "test/puzzle2_response_expected.txt")
        actual = self.test_url_utils.get_mess_and_trailer(content, self.leader)
        self.assertEqual("%%$@_$^__#)^", actual[:12])

    def test_get_mess(self):
        content = self.test_file_utils.get_file_string(
            "test/puzzle2_response_expected.txt")
        actual = self.test_url_utils.get_mess(
            content, self.leader, self.trailer)
        self.assertEqual(98764, len(actual))
        # test start
        self.assertEqual("%%$@_$^__#)^", actual[:12])
        # test end
        self.assertEqual(")$!%{(}$^$}*", actual[len(actual)-12:])


if __name__ == "__main__":
    unittest.main()
