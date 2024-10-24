#!/usr/bin/env python3
"""
Contains the class definition for redis cache
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the given data in Redis using a randomly generated key."""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Union[str, int, bytes]]:
        """
        Retrieve the value stored in Redis under 'key'.
        Optionally convert it using the 'fn' callable.

        Args:
            key (str): The key of the stored data.
            fn (Callable, optional): A callable to convert the retrieved data.

        Returns:
            Optional[Union[str, int, bytes]]: The retrieved data.
        """
        value = self._redis.get(key)

        if value is None:
            return None

        if fn is not None:
            return fn(value)

        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve the value stored under 'key' and convert it to a string.
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve the value stored under 'key' and convert it to an integer.
        """
        return self.get(key, lambda x: int(x.decode('utf-8')))
