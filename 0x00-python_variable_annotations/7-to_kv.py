#!/usr/bin/env python3
""" to_kv Module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple key value, value is sqr of input"""
    return (k, float(v**2))
