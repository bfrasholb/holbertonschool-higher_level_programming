#!/usr/bin/python3
"""Module That Defines a Rectangle"""


class Rectangle:
    """A Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        return print("Bye rectangle...")

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __str__(self):
        if not self.height or not self.width:
            return ""
        rows = f"{self.print_symbol}" * self.width
        str = (rows + "\n") * (self.height - 1) + rows
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
