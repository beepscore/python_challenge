#!/usr/bin/env python3

import file_utils
import unittest


class TestFileUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_file_string(self):
        test_file_utils = file_utils.FileUtils()
        actual = test_file_utils.get_file_string(
            "test/puzzle2_response_expected.txt")
        self.assertIsNotNone(actual)
        self.assertEqual(99613, len(actual))

        self.assertEqual("<html>\n<he", actual[:10])

    def test_write_bytes_to_filename(self):
        test_bytes = "foo".encode('utf-8')
        filename = "./test/junk.zip"
        file_utils.FileUtils().write_bytes_to_filename(test_bytes, filename)

        # data_file is a file object
        data_file = open(filename)
        self.assertIsNotNone(data_file)
        data_file.close()

if __name__ == "__main__":
    unittest.main()
