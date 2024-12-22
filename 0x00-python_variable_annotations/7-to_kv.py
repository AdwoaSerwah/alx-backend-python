#!/usr/bin/env python3
"""
Module that contains a function `to_kv` with type annotations.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that returns a tuple where the first element is the string `k` and
    the second element is the square of `v`.

    Args:
    k (str): The string key.
    v (Union[int, float]): The value to be squared.

    Returns:
    Tuple[str, float]: A tuple containing the string and the square of value.
    """
    return (k, float(v ** 2))
