#!/usr/bin/env python

"""
code that tests the circle class defined in circle.py

can be run with py.test
"""

import pytest  # used for the exception testing

import math


from circle import Circle
# from circle_solution1 import Circle


def Assert(x1, x2):
    """ Py.test assert does not work with Python 3.5. I have to define
         my own assert as workaround. See discussion here:
         https://github.com/pytest-dev/pytest/issues/744"""
    if x1 != x2:
        raise Exception('Assert')


def test_create():
    c = Circle(4)

    Assert(c.radius, 4)


def test_change_radius():
    c = Circle(3)
    c.radius = 4

    Assert(c.radius, 4)


def test_diameter():
    c = Circle(4)

    Assert(c.diameter, 8)


def test_change_diameter():
    c = Circle(2)

    Assert(c.radius, 2)
    Assert(c.diameter, 4)

    c.diameter = 6
    Assert(c.radius, 3)
    Assert(c.diameter, 6)


def test_area():
    c = Circle(4)

    Assert(c.area, math.pi*16)


def test_set_area():
    c = Circle(4)

    with pytest.raises(AttributeError):
        c.area = 44


# the extra credit: class method:

def test_alternate_constructor():
    c = Circle.from_diameter(8)

    Assert(c.diameter, 8)
    Assert(c.radius, 4)
