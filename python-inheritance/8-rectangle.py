#!/usr/bin/python3
"""A Rectangle Module"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if self.integer_validator(width) and self.integer_validator(height):
            self.__width = width
            self.__height = height
