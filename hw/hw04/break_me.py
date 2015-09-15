import sys
import math


def exhibit_name_error():
    # replace tis line with smth that exibits
    # a name error
    lena()


def exhibit_attribute_error():
    math.lena


def exhibit_type_error():
    a = "Hello"
    b = 123
    c = a + b

try:
    exhibit_name_error()
except NameError:
    exc = sys.exc_info()
    print("NameError: ", exc[1])

try:
    exhibit_attribute_error()
except AttributeError:
    exc = sys.exc_info()
    print("AttributeError: ", exc[1])

try:
    exhibit_type_error()
except TypeError:
    exc = sys.exc_info()
    print("TypeError: ", exc[1])
