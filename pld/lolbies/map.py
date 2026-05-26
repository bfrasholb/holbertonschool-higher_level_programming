#!/usr/bin/env python3


Summoner = __import__("summoner").Summoner


class Map:
    __COUNT = 0
    ALLOWED_TEAMS = ("blue", "red")

    def __init__(self, name, blue=[], red=[]):
        if Map.__COUNT >= 1:
            raise ValueError("Only One Map is Allowed")
        Map.__COUNT += 1
        self.name = name
        if blue is not None:
            self.blue = blue
        if red is not None:
            self.red = red
        print(f"Welcome to {self.name}!")

    def __del__(self):
        Map.__COUNT = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, summoners):
        if not isinstance(summoners, list):
            raise TypeError("Summoners Must be a List.")
        if not len(summoners) == 5:
            raise ValueError("Red Team Must Have 5 Players.")
        if any(type(summoner) is not Summoner for summoner in summoners):
            raise TypeError("All Players must be Summoners.")
        self.__red = []
        for summoner in summoners:
            self.add_summoner(summoner, "red")

    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, summoners):
        if not isinstance(summoners, list):
            raise TypeError("Summoners Must be a List.")
        if not len(summoners) == 5:
            raise ValueError("blue Team Must Have 5 Players.")
        if any(type(summoner) is not Summoner for summoner in summoners):
            raise TypeError("All Players must be Summoners.")
        self.__blue = []
        for summoner in summoners:
            self.add_summoner(summoner, "blue")

    def add_summoner(self, summoner, team):
        if team not in Map.ALLOWED_TEAMS:
            raise ValueError("Team must be either blue or red.")
        if team is "red":
            if len(self.red) >= 5:
                raise ValueError("Red Team Must Have 5 Players.")
            summoner.team = "red"
            self.red.append(summoner)
        if team is "blue":
            if len(self.blue) >= 5:
                raise ValueError("Blue Team Must Have 5 Players.")
            summoner.team = "blue"
            self.blue.append(summoner)

    def __str__(self):
        map_name = f"Map Name: {self.name}"
        border = f"*" * len(map_name)
        str = border + "\n" + map_name + "\n"
        str += f"\tBlue Team:" + "\n"
        for summoner in self.blue:
            str += "\t" * 2 + f"{summoner}" + "\n"
        str += f"\tRed Team:" + "\n"
        for summoner in self.red:
            str += "\t" * 2 + f"{summoner}" + "\n"
        str += border + "\n"
        return str
