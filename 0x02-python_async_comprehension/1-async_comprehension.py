#!/usr/bin/env python3
"""Task 1"""
from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """return 10 numbers generation"""

    values = [value async for value in async_generator()]
    return values