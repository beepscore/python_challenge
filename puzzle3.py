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

    def get_character_and_uppercase_bodyguards(self, a_string):
        """
        match pattern one lowercase letter surrounded by
        3 uppercase each side.
        """
        match_object = re.search(r'([A-Z]){3}([a-z]){1}([A-Z]){3}', a_string)
        return match_object.group(0)
