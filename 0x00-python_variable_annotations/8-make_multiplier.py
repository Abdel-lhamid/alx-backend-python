#!/usr/bin/env python3
"""make multiplier Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """return a multiplier function"""
    return lambda x: x * multiplier
