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
            reader = csv.reader(f)
            data_json = []
            for row in reader:
                data_json.append([row for row in reader])
        with open("data.json", "w", data_json) as f:
            f.dump(data_json, f)
        return True
    except Exception:
        return False
