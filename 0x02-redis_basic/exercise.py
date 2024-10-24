#!/usr/bin/env python3
"""
Contains the class definition for redis cache
"""
import uuid
from typing import Union

import redis


class Cache:
    """
    Defines methods to handle redis cache operations
    """
    def __init__(self):
        """
        Initialize redis client
        Attributes:
            self._redis (redis.Redis): redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
