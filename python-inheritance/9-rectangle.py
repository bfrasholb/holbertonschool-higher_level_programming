#!/usr/bin/python3
"""A Rectangle Module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangular Class"""

    def __init__(self, width, height):
        if self.integer_validator("width", width) and self.integer_validator(
            "height", height
        ):
            self.__width = width
            self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
