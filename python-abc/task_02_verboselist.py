#!/usr/bin/python3


class VerboseList(list):
    def append(self, element):
        print(f"Added [{element}] to the list.")
        super().append(element)

    def extend(self, items):
        print(f"Extended the list with [{len(items)}].")
        super().extend(items)

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        print(f"Popped [{self[index]}] from the list.")
        super().pop(index)
