#!/usr/bin/env python3
"""
Module that contains a function `sum_mixed_list` with type annotations.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that calculates the sum of a list of integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): The list containing integers and floats.

    Returns:
    float: The sum of the integers and floats in the list.
    """
    return sum(mxd_lst)
