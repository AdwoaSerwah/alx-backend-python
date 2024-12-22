#!/usr/bin/env python3
"""
Module that contains a function to safely get a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

# Define a TypeVar to represent the type of the values in the dictionary
T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any,
    default: Union[T, None] = None
) -> Union[T, None]:
    """
    Function to safely retrieve a value from a dictionary using a key.
    If the key exists, return the value; otherwise, return the default value.

    Args:
    dct (Mapping[Any, T]): The dictionary to search in.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None], optional): The default value to return if
    the key is not found. Defaults to None.

    Returns:
    Union[T, None]: The value associated with the key if found,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
