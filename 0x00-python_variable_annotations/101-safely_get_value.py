#!/usr/bin/env python3
""" safely_get_value Module"""
from typing import Any, Mapping, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None] = None
                     ) -> Union[Any, TypeVar('T')]:
    """ returns a value from a dict using a given key"""
    if key in dct:
        return dct[key]
    else:
        return default
