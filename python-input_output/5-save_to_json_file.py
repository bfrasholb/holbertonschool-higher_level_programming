#!/usr/bin/python3
"""Obj to Data"""

import json


def save_to_json_file(my_obj, filename):
    """Obj to Data"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
