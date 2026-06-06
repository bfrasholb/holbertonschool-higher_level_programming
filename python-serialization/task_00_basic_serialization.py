#!/usr/bin/python3


import json


def serialize_and_save_to_file(data, filename):
    # Data: python Dictionary with data, filename: output JSON file name mode : w
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    # filename: filename of input JSON file, returns Python Dictionary with deserialised JSON data
    with open(filename, "r") as f:
        return json.load(f)
