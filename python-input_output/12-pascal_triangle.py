#!/usr/bin/python3
"""Pascal's Triangle

0            1
1           1 1
2          1 2 1
3         1 3 3 1
4        1 4 6 4 1

(a + b) ^ n ~ coefficients calculated with (n!) / (k! * (n - k)!)


"""


def pascal_triangle(n):
    """Prints Pascal's Triangle"""
    """Returns an empty list if n <= 0"""
    if n <= 0 or None:
        return []

    result = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            coefficient = factorial(i) // (factorial(j) * factorial(i - j))
            row.append(coefficient)
        result.append(row)
    return result


def factorial(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
