#!/usr/bin/python3
"""A Rectangle Module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangular Class"""

    def __init__(self, width, height):
        if self.integer_validator("name", width) and self.integer_validator(
            "name", height
        ):
            self.__width = width
            self.__height = height
