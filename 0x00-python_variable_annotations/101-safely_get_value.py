#!/usr/bin/env python3

from typing import TypeVar, Mapping, Any, Optional

K = TypeVar('K')  # Key type
V = TypeVar('V')  # Value type

def safely_get_value(dct: Mapping[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    if key in dct:
        return dct[key]
    else:
        return default
