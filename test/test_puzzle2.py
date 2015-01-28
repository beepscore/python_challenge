#!/usr/bin/env python3

import puzzle2
import unittest
import codecs

class TestPuzzle2(unittest.TestCase):

    def setUp(self):
        pass

    def get_file_string(self, filename):
        """ read contents of file and return a string
        If can't read file or file is empty return None
        """
        # note text_file is a file object, not a string
        text_file = open(filename)
        file_string = text_file.read()
        text_file.close()
        # http://stackoverflow.com/questions/4020539/process-escape-sequences-in-a-string-in-python
        decoded_string = codecs.decode(file_string, 'unicode_escape')
        return decoded_string

    def test_get_file_string(self):
        """ Test the test method
        """
        actual = self.get_file_string("test/puzzle2_response_expected.txt")
        self.assertIsNotNone(actual)
        self.assertEqual(99613, len(actual))

        self.assertEqual("<html>\n<he", actual[:10])

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
        expected = self.get_file_string("test/puzzle2_response_expected.txt")

        actual_bytes = puzzle2.get_response(
            "http://www.pythonchallenge.com/pc/def/ocr.html")
        actual_string = puzzle2.string_from_bytes(actual_bytes)
        self.assertEqual(expected, actual_string)

    def test_trimmed_content(self):
        #actual = puzzle2.trimmed_content(self.response_expected)
        pass


if __name__ == "__main__":
    unittest.main()
