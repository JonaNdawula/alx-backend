#!/usr/bin/env python3
"""
This module contains
a function to return
a tuple of size two containing
a start index and an end index
"""


def index_range(page, page_size):
    """
    Function to return a tuple of size two containing
    a start index and an end
    index corresponding to the range of indexes to
    return in a list for those
    particular pagination parameters.
    """
    st_index = (page - 1) * page_size
    end_index = page * page_size
    return st_index, end_index
