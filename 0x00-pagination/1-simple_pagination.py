#!/usr/bin/env python3
"""
This module contains
functions implementing
simple pagination
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "popular_Baby_Names.csv"

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
        """Get page
        """

        index_range = __import__('0-simple_helper_function').index_range
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        st_index, end_index = index_range(page, page_size)
        if st_index >= len(self.dataset()):
            return []
        return self.dataset()[st_index:end_index]
