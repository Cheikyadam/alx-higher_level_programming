#!/usr/bin/python3
"""
Just  from json in a file
"""
import json


def load_from_json_file(filename):
    """ the module

    Parameters:
        filename (str): the file name
    """
    with open(filename, encoding="utf-8") as f:
        x = json.load(f)
    return x
