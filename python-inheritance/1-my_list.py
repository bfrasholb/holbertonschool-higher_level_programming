#!/usr/bin/python3
"""Module inherits from list"""


class MyList(list):
    """Inherits from list"""

    def print_sorted(self):
        print(sorted(self))
