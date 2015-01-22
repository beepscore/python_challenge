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
        self.assertEqual(' ', puzzle1.increment_letter(' '))

    def test_increment_letter_by_two(self):
        self.assertEqual('c', puzzle1.increment_letter_by_two('a'))
        self.assertEqual('z', puzzle1.increment_letter_by_two('x'))
        self.assertEqual('a', puzzle1.increment_letter_by_two('y'))
        self.assertEqual('b', puzzle1.increment_letter_by_two('z'))
        self.assertEqual(' ', puzzle1.increment_letter_by_two(' '))

    def test_translate_message(self):
        message_original = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

        expected = """i hope you didnt translate it by hand. thats what computers are for.
doing it in by hand is inefficient and that's why this text is so long.
using string.maketrans() is recommended. now apply on the url.
"""
        self.assertEqual(expected, puzzle1.translate_message(message_original))


if __name__ == "__main__":
    unittest.main()
