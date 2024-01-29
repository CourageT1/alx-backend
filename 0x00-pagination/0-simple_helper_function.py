#!/usr/bin/env python3
"""
This module defines a function index_range that calculates the start and end
indexes for a given page and page size, facilitating pagination in a list.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for the given
    pagination parameters.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_inde
