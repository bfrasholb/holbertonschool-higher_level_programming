#!/usr/bin/python3


class CountedIterator:
    def __init__(self, iterable):
        self.__iterable = iter(iterable)
        self.__count = 0
        self.__len = len(iterable)

    def __next__(self):
        if self.__count == self.__len:
            raise StopIteration()
        self.__count += 1
        return self.__iterable.__next__()

    def get_count(self):
        return self.__count
