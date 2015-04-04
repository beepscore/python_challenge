#!/usr/bin/env python3

import url_utils
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

    def __init__(self):
        self.url_utils = url_utils.UrlUtils()
        self.puzzle_url = "http://www.pythonchallenge.com/pc/def/equality.html"
        self.leader = "<!--\n"
        self.trailer = "\n-->\n"

    def get_answer_url(self):
        response_bytes = self.url_utils.get_response(self.puzzle_url)
        response_string = self.url_utils.string_from_bytes(response_bytes)
        mess = self.url_utils.get_mess(response_string,
                                       self.leader, self.trailer)
        characters = self.get_characters_inside_matches(mess)
        return self.url_utils.get_url_from_answer_string(characters)

    def get_characters_inside_matches(self, a_string):
        matches = self.get_matches(a_string)
        small_letters = list(self.get_character_inside_match(match)
                             for match in matches)
        return ''.join(small_letters)

    def get_matches(self, a_string):
        """
        Assume bodyguard is an uppercase letter.
        Match pattern one lowercase letter surrounded by 3 uppercase each side.
        Preclude possibility of >3 uppercase bodyguards
        by requiring letter before leading bodyguards
        and after trailing bodyguards is lowercase.
        Hint
        https://groups.google.com/forum/#!topic/python-challenge/H6QNsZevMnw
        """
        regex = r'[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}'
        matches = re.findall(regex, a_string)
        return matches

    def get_character_inside_match(self, match):
        len_leading_lowercase_and_leading_bodyguards = 4
        return match[len_leading_lowercase_and_leading_bodyguards]
