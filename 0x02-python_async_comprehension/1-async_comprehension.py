#!/usr/bin/env python3
"""
This module contains a coroutine function that collects 10 random numbers
using async comprehensions over the async_generator function.
"""

import asyncio
from typing import List

# Importing async_generator using __import__
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using async comprehension over async_generator.

    Returns:
        List[float]: A list of 10 random floating-point numbers.
    """
    return [i async for i in async_generator()]
