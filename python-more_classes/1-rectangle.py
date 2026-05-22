#!/usr/bin/python3
"""Module That Defines a Rectangle"""


class Rectangle:
    """A Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")
        if not width >= 0:
            raise ValueError("Width Must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("Height must be an integer")
        if not height >= 0:
            raise ValueError("Height Must be >= 0")
        self.__height = height
