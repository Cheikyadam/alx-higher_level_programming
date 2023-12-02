#!/usr/bin/python3
"""
Divide a matrix by an integer
"""


def matrix_divided(matrix, div):
    """
    The function

    Parameters:
        matrix (list): the matrix
        div (int): the int
    """
    if matrix is None or type(matrix) is not list:
        raise TypeError("""matrix must be a matrix \
(list of lists) of integers/floats""")
        if div == 0:
            raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    new = []
    for row in matrix:
        new.append(len(row))
    lon = new[0]
    for leng in new:
        if leng != lon:
            raise TypeError("Each row of the matrix must have the same size")
    new_m = []
    for row in matrix:
        line = []
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("""matrix must be a matrix \
(list of lists) of integers/floats""")
            line.append(round(col/div, 2))
        new_m.append(line)
    return new_m
