#!/usr/bin/python3
"""Student Class"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs: list = ["age", "last_name", "first_name"]):
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            filtered_dict = {
                key: value for key, value
                in self.__dict__.items() if key in attrs
            }
            return filtered_dict
