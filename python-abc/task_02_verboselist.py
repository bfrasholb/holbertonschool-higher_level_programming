#!/usr/bin/python3


class VerboseList(list):
    def append(self, element):
        print(f"Added {element} to the list.")

    def extend(self):
        print(f"Extended the list with ")

    def remove(self):
        pass

    def pop(self):
        pass
