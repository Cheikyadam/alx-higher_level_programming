#!/usr/bin/python3
"""
Just write json in a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ the module

    Parameters:
        filename (str): the file name
        my_obj (the object): the object
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
