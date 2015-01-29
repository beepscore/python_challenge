#!/usr/bin/env python3

import puzzle2
import unittest
import codecs


class TestPuzzle2(unittest.TestCase):

    def setUp(self):
        self.leader = "mess below:\n-->\n\n<!--\n"
        self.trailer = "\n-->"

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
        self.assertEqual(99613, len(actual_string))
        self.assertEqual(expected, actual_string)

    def test_get_mess_and_trailer(self):
        content = self.get_file_string("test/puzzle2_response_expected.txt")
        actual = puzzle2.get_mess_and_trailer(content, self.leader)
        self.assertEqual("%%$@_$^__#)^", actual[:12])

    def test_get_mess(self):
        content = self.get_file_string("test/puzzle2_response_expected.txt")
        actual = puzzle2.get_mess(
            content, self.leader, self.trailer)
        self.assertEqual(98764, len(actual))
        # test start
        self.assertEqual("%%$@_$^__#)^", actual[:12])
        # test end
        self.assertEqual(")$!%{(}$^$}*", actual[len(actual)-12:])

    def test_get_character_counts(self):
        content = self.get_file_string("test/puzzle2_response_expected.txt")
        mess = puzzle2.get_mess(content, self.leader, self.trailer)
        character_counts = puzzle2.get_character_counts(mess)
        self.assertEqual(25, len(character_counts))

    def test_get_string_from_unique_chars(self):
        content = self.get_file_string("test/puzzle2_response_expected.txt")
        mess = puzzle2.get_mess(content, self.leader, self.trailer)
        self.assertEqual("equality", puzzle2.get_string_from_unique_chars(mess))


if __name__ == "__main__":
    unittest.main()
