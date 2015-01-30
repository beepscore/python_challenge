#!/usr/bin/env python3

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


def get_character_counts(a_string):
    """ return a list of lists.
    This maintains character order
    http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value?rq=1
    http://stackoverflow.com/questions/15733558/python-ordereddict-not-keeping-element-order?rq=1
    """
    character_counts = []
    characters = []
    for char in a_string:
        # list comprehension
        characters = [item[0] for item in character_counts]
        if char not in characters:
            character_counts.append([char, 1])
        else:
            for item in character_counts:
                if item[0] == char:
                    item[1] += 1
                    break
    return character_counts


def get_string_from_unique_chars(a_string):
    character_counts = get_character_counts(a_string)
    unique_chars = list(char for char, count in character_counts if count == 1)
    return ''.join(unique_chars)
