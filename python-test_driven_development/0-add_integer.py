#!/usr/bin/python3
"""Module for Add Integers"""


def add_integer(a, b=98):
    """ "Return Addition of Two Integers"""
    if type(a) not in (int, float):
        return "a must be an integer"
    elif type(b) not in (int, float):
        return "b must be an integer"
    return int(a) + int(b)
