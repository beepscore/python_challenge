#!/usr/bin/env python3

import url_utils


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
            print("url: " + url)
        return url

    def get_next_url(self, url):
        text = self.get_text_from_url(url)
        nothing_digits = self.get_nothing_digits_from_text(text)
        next_url = self.get_url_from_nothing_digits(nothing_digits)
        return next_url

    def get_text_from_url(self, url):
        response_bytes = self.url_utils.get_response(url)
        text = self.url_utils.string_from_bytes(response_bytes)
        return text

    def get_nothing_digits_from_text(self, text):
        text_start = "and the next nothing is "
        nothing_digits = text[len(text_start):]
        return nothing_digits

    def get_url_from_nothing_digits(self, nothing_digits):
        url_start = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
        url = url_start + nothing_digits
        return url
