#!/usr/bin/python3
"""File Writer"""


def write_file(filename="", text=""):
    """File Writer"""
    with open(filename, "w") as f:
        return f.write(text)
