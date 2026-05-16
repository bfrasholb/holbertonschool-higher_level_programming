#!/usr/bin/python3
"""Module for Matrix division"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div"""

    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_matrix.append([round(x / div, 2) for x in row])
    return new_matrix
