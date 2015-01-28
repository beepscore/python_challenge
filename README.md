Steve Baker Beepscore LLC

# Purpose
Record info about Python challenge game.

# References
http://www.pythonchallenge.com/

## project structure info
http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application
http://as.ynchrono.us/2007/12/filesystem-structure-of-python-project_21.html

## unit tests
http://stackoverflow.com/questions/1732438/how-to-run-all-python-unit-tests-in-a-directory
http://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure#1897665

# Results
Click on button "Click here to get challenged.
Navigates to puzzle 0.

## puzzle 0
http://www.pythonchallenge.com/pc/def/0.html
warming up
Hint: try to change the url address.

I entered
http://www.pythonchallenge.com/pc/def/1.html
response
2*****38 is much bigger than that

➜  ~  python3
Python 3.4.2 (default, Oct 16 2014, 23:52:08)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.51)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2**38
274877906944

http://www.pythonchallenge.com/pc/def/274877906944.html
solved!

url redirects to puzzle 1

## puzzle 1
See puzzle1.py and test_puzzle1.py

## Run unit tests

To run tests in terminal, cd to top level directory that contains subdirectory test

    ➜  python_challenge git:(master) ✗ python3 -m unittest discover test
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.001s
    OK
