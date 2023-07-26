#!/usr/bin/env python3
"""Simple helper function for handling pagination"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing the start index and end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters""" 
    start = 0
    stop = 0

    for i in range(1, page + 1):
        if i == page:
            start = page_size * (i - 1)
            stop = start + page_size
    return (start, stop)