#!/usr/bin/python3
"""Module for Add Integers"""


def add_integer(a, b=98):
    """ "Return Addition of Two Integers"""
    res = 0
    try:
        res = int(a) + int(b)
    except Exception:
        if type(a) not in (int, float):
            res = "a must be an integer"
        elif type(b) not in (int, float):
            res = "b must be an integer"
    return res
