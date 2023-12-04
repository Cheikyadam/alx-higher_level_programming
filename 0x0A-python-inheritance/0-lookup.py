#!/usr/bin/python3

""""Module to return list of available \
        attributes and methods of an object"""


def lookup(obj):
    """The implementation of the module

    Parameters:
        obj (objet of any class): the object

    Returns:
        list of attributes and methods
    """
    return dir(obj)
