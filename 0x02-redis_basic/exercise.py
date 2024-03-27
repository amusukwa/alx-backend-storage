#!/usr/bin/env python3

"""
This module defines a Cache class for storing data in Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional

class Cache:
    """
    Cache class for storing data in Redis.

    Attributes:
        _redis: An instance of the Redis client.
    """

    def __init__(self) -> None:
        """
        Initializes the Cache class.

        Initializes instance of Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis and returns the generated key.

        Args:
            data: The data to store in Redis. Can be a str, bytes, int, or float.

        Returns:
            str: The key under which the data is stored in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        data from Redis using given key, applying optional conversion function.

        Args:
            key: The key to retrieve data from Redis.
            fn: An optional conversion function to apply to the retrieved data.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string value from Redis using the given key.

        Args:
            key: The key to retrieve the string value from Redis.

        Returns:
            Optional[str]: The retrieved string value, or None if the key does not exist.
        """
        return self.get(key, str.decode)

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer value from Redis using the given key.

        Args:
            key: The key to retrieve the integer value from Redis.

        Returns:
            Optional[int]: The retrieved integer value, or None if the key does not exist or the value is not an integer.
        """
        return self.get(key, int)
