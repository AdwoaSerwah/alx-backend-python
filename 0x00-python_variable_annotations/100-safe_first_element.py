#!/usr/bin/env python3
"""
Module that contains a function to safely
retrieve the first element of a sequence.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function that safely returns the first element of a sequence or
    None if the sequence is empty.

    Args:
    lst (Sequence[Any]): The sequence from which to get the first element.

    Returns:
    Union[Any, None]: The first element of the sequence or
    None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
