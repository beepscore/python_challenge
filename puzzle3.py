#!/usr/bin/env python3

import re


class Puzzle3:
    """
    Reference
    puzzle3 url
    http://www.pythonchallenge.com/pc/def/equality.html

    puzzle3 url comes from solution to puzzle2
    test_puzzle2.py

    One small letter, surrounded by
    EXACTLY three big bodyguards on each of its sides.

    In browser, view page source
    """

    def get_matches(self, a_string):
        """
        Assume bodyguard is an uppercase letter.
        Match pattern one lowercase letter surrounded by
        3 uppercase each side, surrounded by uppercase letter.
        Hint
        https://groups.google.com/forum/#!topic/python-challenge/H6QNsZevMnw
        Preclude possibility of >3 uppercase bodyguards
        """
        regex = r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}'
        matches = re.findall(regex, a_string)
        return matches

    def get_characters_inside_matches(self, a_string):
        matches = self.get_matches(a_string)
        small_letters = list(match[4] for match in matches)
        return ''.join(small_letters)
