#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_s = []
    for row in matrix:
        row_n = []
        for col in row:
            row_n.append(col*col)
        new_s.append(row_n)
    return new_s
