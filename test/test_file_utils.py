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


if __name__ == "__main__":
    unittest.main()
