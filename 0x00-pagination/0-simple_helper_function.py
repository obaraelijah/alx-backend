#!/usr/bin/env python3
"""Simple helper function for handling pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing the start_index index and end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters"""
    start_index = 0
    end_index = 0

    for i in range(1, page + 1):
        if i == page:
            start_index = page_size * (i - 1)
            end_index = start_index + page_size
    return (start_index, end_index)