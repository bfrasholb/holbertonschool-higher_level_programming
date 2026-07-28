#!/usr/bin/env python3
"""Annotated function Sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns a float sum from a list of floats"""
    total = sum([entry for entry in input_list])
    return total
