#!/usr/bin/env python3
"""Annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a lambda"""
    return lambda x: x * multiplier
