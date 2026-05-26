#!/usr/bin/python3
"""Inherited but not Exact"""


def inherits_from(obj, a_class):
    """Inheritance but not Exact"""
    return isinstance(obj, a_class) and not type(obj) is a_class
