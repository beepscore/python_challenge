#!/usr/bin/env python3

import pickle
import url_utils


class Puzzle5:
    """
    Reference
    Puzzle5 is at
    http://www.pythonchallenge.com/pc/def/peak.html
    body says "peak hell", says pronounce it
    I searched for a hint
    http://python3solutions.blogspot.com/2011/04/python-challenge-005-peak.html
    Python serialization is called pickle.
    https://docs.python.org/3.4/library/pickle.html#module-pickle

    Manually navigated to page
    http://www.pythonchallenge.com/pc/def/pickle.html
    Says
    yes! pickle!

    Went back to
    http://www.pythonchallenge.com/pc/def/peak.html
    Page source shows banner.p, apparently a text file
    Unpickle banner.p
    """

    def __init__(self):
        self.url_utils = url_utils.UrlUtils()

    def get_banner_list(self):
        banner_url = "http://www.pythonchallenge.com/pc/def/banner.p"
        response_bytes = self.url_utils.get_response(banner_url)
        banner_list = pickle.loads(response_bytes)
        return banner_list

    def print_banner_list(self, banner_list):
        """
        for banner_list from "http://www.pythonchallenge.com/pc/def/banner.p"
        prints an "ascii-art" banner
        of space and '#' characters that spells channel
        puzzle6 is at
        http://www.pythonchallenge.com/pc/def/channel.html
        """
        character_index = 0
        repeat_index = 1

        for line in banner_list:
            line_string = ""
            for character_tuple in line:
                # * operator repeats the character repeat_index number of times
                tuple_string = character_tuple[character_index] * character_tuple[repeat_index]
                line_string += tuple_string
            print(line_string)
