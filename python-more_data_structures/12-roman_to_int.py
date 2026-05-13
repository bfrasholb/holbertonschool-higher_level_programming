#!/usr/bin/python3

def detect_illegal(roman_string):
    banned_seq = ["VV", "LL", "DD", "IIII", "XXXX", "CCCC"]
    for string in banned_seq:
        if roman_string.find(string) != -1:
            return True
    return False

def roman_to_int(roman_string):
    if not roman_string or \
       not isinstance(roman_string, str) or \
       detect_illegal(roman_string) is True:
        return 0
    roman_values = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}
    total, prev_sym, sub = 0, "", False

    for char in reversed(roman_string):
        value = roman_values[char]

        if prev_sym != "" and value < roman_values[prev_sym]:
            if sub:
                return 0
            total -= value
            sub = True
        else:
            total += value
            sub = False
        prev_sym = char
    return total
