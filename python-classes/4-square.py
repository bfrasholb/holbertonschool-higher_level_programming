#!/usr/bin/python3
"""This Module Defines a Class"""


class Square:
    """The Square Class"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size
    @size.setter
        def size(self, value):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
