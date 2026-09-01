#!/usr/bin/env python3
"""Paging Module"""


def index_range(page: int, page_size: int) -> tuple:
	"""Function that returns indices of page"""
    return ((page - 1) * page_size, page * page_size)
