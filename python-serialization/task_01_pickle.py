#!/usr/bin/python3


import pickle


class CustomObject:
    """
    Object With Methods:
    Display
    Serialise
    Deserialise
    """

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the Current Instance"""
        attrs = ["name", "age", "is_student"]
        for i, attr in enumerate(attrs):
            attr_name = attr
            attr_name = attr_name[0].upper() + attr_name[1:]
            if attr[i] in "_- ":
                attr_name = attr_name[:i] + f" " + attr_name[i + 1 :]
                if attr_name[i + 1]:
                    attr_name = (
                        attr_name[: i + 1]
                        + attr_name[i + 1].upper()
                        + attr_name[i + 2 :]
                    )
            print(f"{attr_name}: {getattr(self, attr)}")

    def serialize(self, filename):
        """Serialise the Current Instance"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Deserialise Instance from Filename"""
        with open(filename, "rb") as f:
            return pickle.load(f)
