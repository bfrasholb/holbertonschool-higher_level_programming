#!/usr/bin/python3
"""Create Object from JSON"""

import json


def load_from_json_file(filename):
    """Create Object from JSON"""
    with open(filename) as f:
        return json.load(f)
