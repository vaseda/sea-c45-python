#!/usr/bin/env python
"""circle class --

fill this in so it will pass all the tests.
"""
import math


class Circle(object):
    def __init__(self, radius):
        """
        Initialize a circle with a given radius.
        """

        self._radius = radius

    def from_diameter(diameter):
        return Circle(float(diameter)/2)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        self._radius = float(value) / 2

    @property
    def area(self):
        return math.pi * (self._radius ** 2)

    def __str__(self):
        return "Circle with radius: %s" % format(self.radius, '.6f')

    def __repr__(self):
        return "Circle(%s)" % self.radius

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __sub__(self, other):
        return Circle(self.radius - other.radius)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __eq__(self, other):
        return self.radius == other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius < other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius
