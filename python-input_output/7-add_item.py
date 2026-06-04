#!/usr/bin/python3
"""Add Elements"""

from sys import argv

to_json = __import__("5-save_to_json_file").save_to_json_file
from_json = __import__("6-load_from_json_file").load_from_json_file
stored_data = "add_item.json"
try:
    my_list = from_json(stored_data)
    my_list += argv[1:]
except BaseException:
    my_list = argv[1:]
to_json(my_list, stored_data)
