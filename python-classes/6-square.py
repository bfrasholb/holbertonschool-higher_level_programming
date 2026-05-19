#!/usr/bin/python3
"""This Module Defines a Class"""


class Square:
    """The Square Class"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif all(len(value) == 2 and num >= 0 for num in value):
            self.__position = value
