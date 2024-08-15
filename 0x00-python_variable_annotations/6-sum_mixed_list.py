#!/usr/bin/env python3
"""sum mixed list Module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """return sum of mixed list int float"""
    return float(sum(mxd_lst))
