#!/usr/bin/python3
"""
Just to append in a file
"""


def append_write(filename="", text=""):
    """ the module

    Parameters:
        filename (str): the file name
        text (str): the text
    """
    with open(filename, 'a', encoding="utf-8") as f:
        nb = f.write(str(text))
    return nb
