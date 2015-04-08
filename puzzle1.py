#!/usr/bin/env python3

import string

"""
http://www.pythonchallenge.com/pc/def/map.html

image shows
k -> m
o -> q
e -> g

title: everybody thinks twice before solving this.

g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

Procedure
Preserve newline, but assume it is not important

Seems to be shifting each letter to 2 letters later.
Consistent with "thinks twice"?
Try map ahead 2

"""


def increment_letter(letter):
    """Return letter incremented by one

    Keyword arguments:
        letter -- ascii, case insensitive

    Wrap z back to a
    Don't increment non-letters such as space ' ' or newline.
    'a' -> 'b'
    'y' -> 'z'
    'z' -> 'a'
    ' ' -> ' '
    http://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
    """

    if letter not in string.ascii_letters:
        return letter
    if letter == 'z':
        return 'a'
    else:
        # use ascii arithmetic
        # http://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
        return chr(ord(letter) + 1)


def increment_letter_by_two(letter):
    """Return letter incremented by two

    Keyword arguments:
        letter -- ascii, case insensitive

    Wrap y back to a
    Don't increment non-letters such as space ' ' or newline.
    'a' -> 'c'
    'x' -> 'z'
    'y' -> 'a'
    'z' -> 'b'
    http://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
    """

    return increment_letter(increment_letter(letter))


def increment_message(message):
    """ Return message with letters incremented by two.

    Keyword arguments:
        message -- string of ascii. Case insensitive.

    Uses list comprehension
    """

    message_incremented = [increment_letter_by_two(letter) for letter in message]
    return ''.join(message_incremented)


def map_message(message):
    """Return message with letters incremented by two.

    Keyword arguments:
        message -- string of ascii. Case insensitive.

    Uses map. (Alternative to using list comprehension.)
    """

    # map is lazy and won't generate / evaluate until and unless it has to
    message_mapped = map(lambda letter: increment_letter_by_two(letter),
                         message)
    return ''.join(message_mapped)


def translate_message(message):
    """ Use maketrans suggested by decoded puzzle string.
    Works with Unicode, solution is more general than "ascii arithmetic".
    Python 2 used string.maketrans with byte arguments
    Python 3 deprecated string.maketrans and uses str.maketrans
    """
    translation_table = str.maketrans(
        "yzabcdefghijklmnopqrstuvwxYZABCDEFGHIJKLMNOPQRSTUVWX",
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return message.translate(translation_table)
