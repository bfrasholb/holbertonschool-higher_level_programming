#!/usr/bin/python3
"""Add Elements"""

import json
from sys import argv

to_json = __import__("5-save_to_json_file").save_to_json_file
from_json = __import__("6-load_from_json_file").load_from_json_file


to_json(argv[1:], "add_item")
