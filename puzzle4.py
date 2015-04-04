#!/usr/bin/env python3

import url_utils
import pickle
import re


class Puzzle4:
    """
    Reference
    test_puzzle3.py explains puzzle4 starting url
    http://www.pythonchallenge.com/pc/def/linkedlist.php

    html has comment and image with link
    <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never
    end. 400 times is more than enough. -->
    <a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg" border="0"/></a>

    follow links
    click on image, navigates to
    http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
    says "and the next nothing is 44827"
    http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=44827
    says "and the next nothing is 45439"

    Eventually goes to peak.html
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
    Unpickle it.
    """

    def __init__(self):
        self.url_utils = url_utils.UrlUtils()
        self.puzzle_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

    def get_url_for_url_start_count_max(self, url_start, count_max):
        print()
        print("url_start: " + url_start + " count_max: " + str(count_max))
        url = url_start
        for i in range(count_max):
            url = self.get_next_url(url)
            print("i: {0:d} url: {1}".format(i, url))
            if url == "http://www.pythonchallenge.com/pc/def/peak.html":
                break

        return url

    def get_next_url(self, url):
        text = self.get_text_from_url(url)

        if text == "Yes. Divide by two and keep going.":
            # NOTE: sic. divide digits in url
            url_digits = self.get_url_digits_from_text(url)
            next_url_digits = self.text_from_text_value_divided_by_2(url_digits)
            return self.get_next_url_from_text(next_url_digits)
        else:
            return self.get_next_url_from_text(text)

    def text_from_text_value_divided_by_2(self, digits_text):
            value = int(digits_text)
            value_divided_by_2 = value // 2
            return str(value_divided_by_2)

    def get_text_from_url(self, url):
        response_bytes = self.url_utils.get_response(url)
        text = self.url_utils.string_from_bytes(response_bytes)
        return text

    def get_next_url_from_text(self, text):
        next_url_digits = self.get_url_digits_from_text(text)
        if next_url_digits == "":
            # TODO: consider percent escaping text to make method more general
            return "http://www.pythonchallenge.com/pc/def/" + text
        else:
            url_start = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
            return url_start + next_url_digits

    def get_url_digits_from_text(self, text):
        # one or more digits followed by end of line
        regex = r'\d+$'
        matches = re.findall(regex, text)
        if len(matches) > 0:
            return matches[0]
        else:
            return ""

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
        puzzle5 is at
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
