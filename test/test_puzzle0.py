#!/usr/bin/env python3

import puzzle0
import unittest


class TestPuzzle0(unittest.TestCase):

    def setUp(self):
        pass

    def test_base_to_power_0(self):
        self.assertEqual(1, puzzle0.base_to_power(5, 0))

    def test_base_to_power_integers(self):
        self.assertEqual(8, puzzle0.base_to_power(2, 3))

    def test_integer_base_to_real_power(self):
        self.assertAlmostEqual(3, puzzle0.base_to_power(9, 0.5), 4)

    def test_2_to_38(self):
        # run test with guess for expected, then revise expected to match actual
        expected = 274877906944
        self.assertEqual(expected, puzzle0.base_to_power(2, 38))

if __name__ == "__main__":
    unittest.main()
