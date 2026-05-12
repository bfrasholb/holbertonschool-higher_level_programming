#!/usr/bin/python3


def uniq_add(my_list=[]):
    used, res = set(), 0

    for number in my_list:
        if number not in used:
            res += number
            used.add(number)
    return res
