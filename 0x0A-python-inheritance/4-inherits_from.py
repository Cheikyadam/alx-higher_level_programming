#!/usr/bin/python3
"""
is instance or not
"""


def inherits_from(obj, a_class):
    """ is instance or not """
    cl = type(obj)
    if issubclass(cl, a_class) and cl != a_class:
        return True
    return False
