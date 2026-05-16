#!/usr/bin/python3
"""Module for Matrix Division"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and rounds to 2 decimals"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix\
        (list of lists) of integers/floats")

    row_size = None
    new_matrix = []

    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
