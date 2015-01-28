#!/usr/bin/env python3

import string

""" http://www.pythonchallenge.com/pc/def/0.html
warming up
Hint: try to change the url address.

I entered
http://www.pythonchallenge.com/pc/def/1.html
response
2*****38 is much bigger than that

Then used python interactive
➜  ~  python3
Python 3.4.2 (default, Oct 16 2014, 23:52:08)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.51)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2**38
274877906944

Then added puzzle0.py and test_puzzle0.py

http://www.pythonchallenge.com/pc/def/274877906944.html
solved!

url redirects to puzzle 1
"""


def base_to_power(base, power):
    if (base != 0) and (power == 0):
        return 1
    else:
        return base ** power
