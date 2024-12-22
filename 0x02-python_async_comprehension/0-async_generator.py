#!/usr/bin/env python3
"""
This module contains an asynchronous generator function
that yields random floating-point numbers between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    An asynchronous generator that yields random numbers between 0 and 10.
    It sleeps for 1 second before yielding each number.

    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
