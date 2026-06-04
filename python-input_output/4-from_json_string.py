#!/usr/bin/python3
"""String to JSON"""

import json


def from_json_string(my_str):
    """JSON Dumper"""
    return json.loads(my_str)
