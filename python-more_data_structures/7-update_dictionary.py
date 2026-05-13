#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    for keys in a_dictionary:
        if key == keys:
            a_dictionary[keys] = value
    a_dictionary |= {key: value}
