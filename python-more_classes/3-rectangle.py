#!/usr/bin/python3
"""Module That Defines a Rectangle"""


class Rectangle:
    """A Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if not self.perimeter:
            return ""
        str = f"#" * self.width
        for i in range(1, self.height):
            str += f"\n" + str
        return str

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if not self.height or not self.width:
            return 0
        return 2 * (self.width + self.height)
