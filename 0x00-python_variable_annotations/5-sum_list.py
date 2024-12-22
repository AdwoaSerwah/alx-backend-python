#!/usr/bin/env python3
"""
Module that contains a function `sum_list` with type annotations.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that calculates the sum of a list of floats.

    Args:
    input_list (List[float]): The list of floats to sum.

    Returns:
    float: The sum of the floats in the list.
    """
    return sum(input_list)
