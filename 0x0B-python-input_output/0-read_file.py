#!/usr/bin/python3
"""
Just to read file contain
"""


def read_file(filename=""):
    """ the module

    Parameters:
        filename (str): the file name
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
