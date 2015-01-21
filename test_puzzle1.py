#!/usr/bin/env python3

import puzzle1
import unittest


class TestPuzzle1(unittest.TestCase):

    def setUp(self):
        pass

    def test_increment_letter(self):
            self.assertEqual('b', puzzle1.increment_letter('a'))
            self.assertEqual('z', puzzle1.increment_letter('y'))
            self.assertEqual('a', puzzle1.increment_letter('z'))

    def test_increment_letter_by_two(self):
            self.assertEqual('c', puzzle1.increment_letter_by_two('a'))
            self.assertEqual('z', puzzle1.increment_letter_by_two('x'))
            self.assertEqual('a', puzzle1.increment_letter_by_two('y'))
            self.assertEqual('b', puzzle1.increment_letter_by_two('z'))

if __name__ == "__main__":
    unittest.main()
