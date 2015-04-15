#!/usr/bin/env python3

import puzzle5
import unittest


class TestPuzzle5(unittest.TestCase):

    def setUp(self):
        self.puzzle5 = puzzle5.Puzzle5()

    def test_get_banner_list(self):
        banner_list = self.puzzle5.get_banner_list()
        self.assertEqual(23, len(banner_list))

if __name__ == "__main__":
    unittest.main()
