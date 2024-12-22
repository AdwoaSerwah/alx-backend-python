#!/usr/bin/env python3
"""
This module contains a coroutine that measures the total runtime of four
parallel executions of async_comprehension using asyncio.gather.
"""

import asyncio
import time
from typing import List

# Import async_comprehension using __import__
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime for executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime of the parallel executions.
    """
    start_time = time.time()

    # Running four async_comprehension tasks concurrently
    # Using * to unpack the list of tasks
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)  # Unpacking the list of tasks

    end_time = time.time()
    return end_time - start_time
