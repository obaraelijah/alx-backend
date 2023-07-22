#!/usr/bin/env python3
""" simple helper function for handling pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing the start index and end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters"""
    
    start = page_size * (page - 1)
    stop = start + page_size

    return (start, stop)