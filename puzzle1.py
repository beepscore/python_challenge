#!/usr/bin/env python3


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
    'a' -> 'b'
    'y' -> 'z'
    'z' -> 'a'
    http://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
    """
    if letter == 'z':
        return 'a'
    else:
        # use ascii arithmetic
        # http://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python
        return chr(ord(letter) + 1)
