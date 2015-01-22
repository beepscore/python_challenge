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

message_original = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""


def increment_letter(letter):
    """ Argument letter is ascii, case insensitive.
    Increment letter by one
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
    """ Argument letter is ascii, case insensitive.
    Increment letter by two
    Wrap y back to a
    Don't increment non-letters such as space ' ' or newline.
    'a' -> 'c'
    'x' -> 'z'
    'y' -> 'a'
    'z' -> 'b'
    http://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
    """
    return increment_letter(increment_letter(letter))


def translate_message(message):
    message_translated = [increment_letter_by_two(letter) for letter in message]
    return ''.join(message_translated)


"""
# TODO: Alternative solution. Fix or delete it
def map_message(message):
    message_mapped = map(lambda letter: increment_letter_by_two(letter), message)
    print(message_mapped)
    return message_mapped
"""
