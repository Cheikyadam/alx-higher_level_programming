#!/usr/bin/python3
""" Module that returns json rep of a str"""


def class_to_json(obj):
    """
    converting in json

    Parameters:
        my_obj (any class): the object

    Returns:
        the json representation of my_obj
    """

    return obj.__dict__
