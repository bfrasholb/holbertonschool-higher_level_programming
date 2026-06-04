#!/usr/bin/python3
"""Obj to Data"""

import json


def save_to_json_file(my_obj, filename):
    """Obj to Data"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
