#!/usr/bin/python3
"""
is instance or not
"""


def is_same_class(obj, a_class):
    """ is instance or not """
    return isinstance(obj, a_class) and type(obj) is a_class
