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
