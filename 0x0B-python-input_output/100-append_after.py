#!/usr/bin/python3
"""
To append after a word"""


def append_after(filename="", search_string="", new_string=""):
    """"
    Append after a string

    Parameters:
        fiename (str): the nameoffile
        search_string (str): to append after this string
        new_string (str): the string to be appended
    """
    with open(filename, encoding="utf-8") as f:
        cont = f.read()
    cont_list = cont.split('\n')
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(cont_list[0])
    checker = 1
    new_line = 1
    with open(filename, 'a', encoding="utf-8") as f:
        for line in cont_list:
            if "Python" in line:
                if checker == 1:
                    f.write("\n"+new_string)
                else:
                    f.write("\n"+line)
                    f.write("\n"+new_string)
                new_line = 0
            else:
                if checker != 1:
                    if new_line == 0:
                        f.write(line)
                    else:
                        f.write("\n"+line)
                new_line = 1
            checker = 0
