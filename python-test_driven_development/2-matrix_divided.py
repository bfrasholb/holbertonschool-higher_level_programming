#!/usr/bin/python3
"""Module for Matrix Division"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and rounds to 2 decimals"""
    if not isinstance(div, (int, float)):
        a = "div must be a number"
        raise TypeError(a)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or matrix == []:
        b = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(b)

    row_size = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list) or row == []:
            c = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(c)
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            d = "Each row of the matrix must have the same size"
            raise TypeError(d)

        new_row = []
        e = "matrix must be a matrix (list of lists) of integers/floats"
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(e)
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
