#!/usr/bin/python3


# def no_c(my_string):
#    new_str = ""
#    for i in range(0, len(my_string)):
#        if my_string[i] != "c" and my_string[i] != "C":
#            new_str += my_string[i]
#    return new_str


def no_c(my_string):
    return "".join(
        [
            "" if my_string[i] == "c" or my_string[i] == "C" else my_string[i]
            for i in range(0, len(my_string))
        ]
    )
