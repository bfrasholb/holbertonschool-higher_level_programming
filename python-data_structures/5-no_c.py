#!/usr/bin/python3


def no_c(my_string):
    new_str = ""
    for i in range(0, len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            new_str += my_string[i]
    print("{}".format(new_str, end=""))
