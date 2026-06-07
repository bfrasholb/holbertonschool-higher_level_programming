#!/usr/bin/python3
"""XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Takes Python dict + filename
    serialize dict to XML
    save to filename
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = Et.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Takes filename as its parameter
    Reads the XML data from file
    Return deserialized python dict
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
