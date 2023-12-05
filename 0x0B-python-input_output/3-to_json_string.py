#!/usr/bin/python3
""" Module that returns json rep of a str"""
import json


def to_json_string(my_obj):
    """
    converting in json

    Parameters:
        my_obj (any class): the object

    Returns:
        the json representation of my_obj
    """

    return json.dumps(my_obj)
