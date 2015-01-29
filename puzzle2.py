#!/usr/bin/env python3

import urllib.request

"""
Reference
puzzle2 url
http://www.pythonchallenge.com/pc/def/ocr.html

puzzle2 url comes from solution to puzzle1
test_puzzle1.py

In browser, view page source
find rare characters in the mess below:

I put the string in a test file.
"""

# TODO
# add another method to count occurrences and return rare characters


def get_response(url):
    # response type is bytes
    # https://docs.python.org/3/library/urllib.request.html
    response = urllib.request.urlopen(url).read()
    return response


def string_from_bytes(a_bytes):
    # http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
    return a_bytes.decode("utf-8")


def get_mess_and_trailer(content, leader):
    components_split_at_leader = content.split(leader)
    mess_and_trailer = components_split_at_leader[-1]
    return mess_and_trailer


def get_mess(content, leader, trailer):
    mess_and_trailer = get_mess_and_trailer(content, leader)
    components_split_at_trailer = mess_and_trailer.split(trailer)
    mess = components_split_at_trailer[-2]
    return mess

def get_character_counts(a_string):
    character_counts = {}
    for char in a_string:
        if char not in character_counts:
            character_counts[char] = 1
        else:
            character_counts[char] += 1
    return character_counts
