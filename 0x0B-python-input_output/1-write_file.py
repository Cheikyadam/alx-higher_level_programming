#!/usr/bin/python3
"""
Just to file write in a file
"""


def write_file(filename="", text=""):
    """ the module

    Parameters:
        filename (str): the file name
        text (str): the text
    """
    with open(filename, 'w', encoding="utf-8") as f:
        nb = f.write(str(text))
    return nb
