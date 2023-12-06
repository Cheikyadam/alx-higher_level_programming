#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Printing pascal triangle

    Parameters:
        n (int): the dim
    """
    triangle = list()
    if n <= 0:
        return triangle
    n = n + 1
    for i in range(1, n):
        row = []
        for j in range(i):
            row.append(1)
        triangle.append(row)
    n = n - 1
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle
