#!/usr/bin/python3


class RSPCA:
    def __init__(self):
        self.animals_saved = []

    @property
    def animals_saved(self):
        return self.__animals_saved

    @animals_saved.setter
    def animals_saved(self, animals):
        if not isinstance(animals, list):
            raise TypeError("RSPCA may only accept a non-empty list of animals.")
        self.__animals_saved = animals

    def save_animals(self, animals):
        print("Animals Saved:")
        for index, animal in enumerate(animals):
            print(f"Animal #{index}: {animal}")
        self.animals_saved = animals


rspca = RSPCA()


class Animal:
    __VALID_SPECIES = ("dog", "cat", "bird")
    __SPECIES_SOUNDS = ("woof ", "meow ", "tweet ")

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __add__(self, animal):
        return Daycare([self, animal])

    def __str__(self):
        sentence = f"My name is {self.name}"
        if not self.species in Animal.__VALID_SPECIES:
            raise TypeError("Species not recognised, sound unknown")
        for index, animal in enumerate(Animal.__VALID_SPECIES):
            if animal == self.species:
                str = f"{Animal.__SPECIES_SOUNDS[index]}" * 2
        str += sentence
        return str

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a str")
        elif name == "":
            raise ValueError("Name must not be empty")
        self.__name = name

    @species.setter
    def species(self, species):
        if not isinstance(species, str):
            raise TypeError("Species must be a str")

        if species == "" or species not in Animal.__VALID_SPECIES:
            raise ValueError("Species allowed: {}".format(Animal.__VALID_SPECIES))

        self.__species = species


class Daycare:
    def __init__(self, visitors):
        self.animals = visitors

    def __str__(self):
        title = "Who's in There?\n"
        border = "=" * 2 * len(title) + "\n"
        str = border + title
        row = "Animal #"

        for index, animal in enumerate(self.animals):
            str += row + f"{index + 1}: {animal}\n"
        str += border
        return str

    def __del__(self):
        try:
            if type(rspca) is RSPCA:
                rspca.save_animals(self.animals)
            else:
                raise NameError()
        except NameError:
            print("Bye Bye Animals.")

    @property
    def animals(self):
        return self.__animals

    @animals.setter
    def animals(self, visitors):
        if (
            not isinstance(visitors, list)
            or not visitors
            or not all(type(animal) is Animal for animal in visitors)
        ):
            raise TypeError("Animals must be provided as a List of Animals")
        self.__animals = visitors


class Neighbourhood:
    count = 0

    def __init__(self, visitors):
        if Neighbourhood.count:
            raise BaseException("There can only be one Neighbourhood")
        else:
            Neighbourhood.count += 1
        if not visitors or not isinstance(visitors, list):
            raise TypeError("Neighbourhood may only accept non-empty list.")
        self.daycare = visitors

    def __del__(self):
        print("Neighbourhood Destroyed.")
        Neighbourhood.count -= 1
        for d in self.daycare:
            del d

    @property
    def daycare(self):
        return self.__daycare

    @daycare.setter
    def daycare(self, visitors):
        self.__daycare = visitors


dog = Animal("Bentley", "dog")
cat = Animal("Luna", "cat")
bird = Animal("Nero", "bird")
res = dog + cat
hood1 = Neighbourhood([res])

# print("Animals:")
# print("{}: {}".format(dog.species, dog.name))
# print("{}: {}".format(cat.species, cat.name))
# print("{}: {}".format(bird.species, bird.name))
# print(res)
