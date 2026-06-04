#!/usr/bin/python3
"""File Reading"""


def read_file(filename=""):
    """File Reader"""
    with open(filename, "r") as f:
        print(f.read(), end="")
