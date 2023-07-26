#!/usr/bin/env python3
"""Simple helper function for handling pagination"""
import math
import csv
from typing import Tuple , List , Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing the start_index index and end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters""" 
    start_index = page_size * (page - 1)
    end_index = start_index + page_size

    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets the items in a page of the dataset"""
        assert (type(page) is int and page > 0)
        assert (type(page_size) is int and page_size > 0)
        data = self.dataset()

        try:
            p = index_range(page, page_size)[0]
            size = index_range(page, page_size)[1]
            return data[p: size]
        except IndexError:
            return []
            

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dict of meta data"""
        all_data = self.dataset()
        data = self.get_page(page, page_size)
        ps = len(data)
        total_pages = math.ceil(len(all_data) / page_size)
        p, n = index_range(page, page_size)
        prev_page = page - 1
        next_page = page + 1

        if p <= 0:
            prev_page = None
        elif n > len(all_data):
            next_page = None

        return {'page_size': ps,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages}