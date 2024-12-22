#!/usr/bin/env python3
"""
Module that contains a function `make_multiplier` with type annotations.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier and returns a function that
    multiplies a float by the multiplier.

    Args:
    multiplier (float): The multiplier to be used in the returned function.

    Returns:
    Callable[[float], float]: A function that takes a float and returns
    the result of multiplying it by the multiplier.
    """
    def multiplier_function(n: float) -> float:
        return n * multiplier

    return multiplier_function
