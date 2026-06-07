#!/usr/bin/python3
"""CSV2JSON"""

import csv
import json


def convert_csv_to_json(filename: str):
    """
    1. open with csv
    2. dict.append([row for row in csv.DictReader])
    3. serialise + output data to data.json
    Return: True on Success else False
    Handle Exceptions
    """
    try:
        with open(filename, "r", newline="") as f:
            data_json = list(csv.DictReader(f))
        with open("data.json", "w") as f:
            json.dump(data_json, f)
        return True
    except Exception as err:
        print(err)
        return False
