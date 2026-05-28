#!/usr/bin/env python3

from sys import argv, exit


class Map:
    queens = 0
    print_symbol = "#"
    queen_symbol = "Q"

    def __init__(self, size=0, queens=0):
        self.size = size
        self.queens = queens

        self.__squares = []

        for y in range(self.size):
            for x in range(self.size):
                self.__squares.append(square(x, y, self.size))

        print(self)

    def __str__(self):
        out = ""

        for y in range(self.size):
            for x in range(self.size):

                sq = None
                for s in self.__squares:
                    if s.coordinates[0] == x and s.coordinates[1] == y:
                        sq = s
                        break

                if sq and sq.queen:
                    out += Map.queen_symbol
                else:
                    out += Map.print_symbol

            if y != self.size - 1:
                out += "\n"

        return out

    @property
    def squares(self):
        return self.__squares

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size


class square:
    def __init__(self, x, y, size=4):
        self.coordinates = [x, y, size]
        self.queen = 0

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, y):
        if y > self.size:
            raise ValueError("there is no space for your space!")
        self.__row = y

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, x):
        if x > self.size:
            raise ValueError("there is no space for your space!")
        self.__column = x

    @property
    def queen(self):
        return self.__queen

    @queen.setter
    def queen(self, boolean):
        if boolean < 0 or boolean > 1:
            raise ValueError("boolean must be boolean")
        self.__queen = boolean


def main():
    current_map = Map(2)


if __name__ == "__main__":
    main()
