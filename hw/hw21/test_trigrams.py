#!/usr/bin/env python
"""code that tests the circle class defined in circle.py

This version adds more tests

can be run with py.test
"""

from trigrams import *
import pytest  # used for the exception testing


def Assert(x1, x2):
    """ Py.test assert does not work with Python 3.5. I have to define
         my own assert as workaround. See discussion here:
         https://github.com/pytest-dev/pytest/issues/744"""
    if x1 != x2:
        raise Exception('Assert')


def test_clean_line1():
    line1 = "The rain in Spain is always on the plane."
    line2 = clean_line(line1)
    Assert(line1, line2)


def test_clean_line2():
    line1 = "The rain in Spain) is always on the ]plane?!"
    line2 = clean_line(line1)
    line3 = "The rain in Spain  is always on the  plane  "
    Assert(line2, line3)


def test_empty_line1():
    line1 = ""
    line2 = clean_line(line1)
    line3 = ""
    Assert(line2, line3)


def test_empty_line2():
    line1 = "??-!):_"
    line2 = clean_line(line1)
    line3 = "       "
    Assert(line2, line3)
