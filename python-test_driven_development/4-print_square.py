#!/usr/bin/python3
"""Module Prints Squares"""


def print_square(size):
    """Prints a square using #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
