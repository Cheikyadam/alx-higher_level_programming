#!/usr/bin/python3
""" Module that returns decodes json"""
import json


def from_json_string(my_str):
    """
    converting from json

    Parameters:
        my_str (str): the string

    Returns:
        the string representations of json
    """

    return json.loads(my_str)
