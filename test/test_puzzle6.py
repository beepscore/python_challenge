#!/usr/bin/env python3

import os
import puzzle6
import unittest


class TestPuzzle6(unittest.TestCase):

    def setUp(self):
        self.puzzle6 = puzzle6.Puzzle6()

    def test_download_url_and_write_to_filename(self):
        filename = "./test/channel.zip"
        self.puzzle6.download_url_and_write_to_filename(self.puzzle6.zip_url,
                                                        filename)

        # data_file is a file object
        data_file = open(filename)
        # assert file exists
        self.assertIsNotNone(data_file)
        data_file.close()
        os.remove(filename)


if __name__ == "__main__":
    unittest.main()
