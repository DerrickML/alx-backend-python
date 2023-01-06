#!/usr/bin/env python3
"""module element length"""
from typing import Any, Mapping, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[Any, None] = None) -> Union[Any, None]:
    """safely get value"""
    if key in dct:
        return dct[key]
    else:
        return default
