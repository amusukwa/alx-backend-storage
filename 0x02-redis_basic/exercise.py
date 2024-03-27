#!/usr/bin/env python3

"""
This module defines a Cache class for storing data in Redis.
"""

import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class for storing data in Redis.

    Attributes:
        _redis: An instance of the Redis client.
    """

    def __init__(self) -> None:
        """
        Initializes the Cache class.

        Initializes an instance of the Redis client and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush the Redis database on initialization

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
