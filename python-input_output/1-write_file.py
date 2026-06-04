#!/usr/bin/python3
"""File Writer"""


def write_file(filename="", text=""):
    """File Writer"""
    with open(filename, "w") as f:
        f.write(text)
