#!/usr/bin/python3
"""A Square Module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """The Square Class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
