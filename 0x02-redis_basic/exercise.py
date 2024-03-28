#!/usr/bin/env python3

"""
This module defines a Cache class for storing data in Redis.
"""

import redis
import uuid
from typing import Union, Callable, Optional
import functools


def count_calls(method):
    @functools.wraps(method)
    def wrapper(self: object, *args: tuple, **kwargs: dict) -> str:
        # Get the qualified name of the method
        method_name = method.__qualname__

        # Increment the call count for the method
        self._redis.incr(method_name)

        # Call the original method and return its result
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs

    Args:
        method: The original function to be decorated.

    Returns:
        Callable: The wrapped function with history logging.
    """
    @functools.wraps(method)
    def wrapper(*args: tuple, **kwargs: dict) -> str:
        # Connect to Redis
        r = redis.Redis()

        # Create keys for input and output lists
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        # Append input arguments to the input list
        r.rpush(input_key, str(args))

        # Execute the original function and store its output
        output = method(*args, **kwargs)

        # Append the output to the output list
        r.rpush(output_key, str(output))

        # Return the output
        return output

    return wrapper


class Cache:
    """
    Cache class for storing data in Redis.

    Attributes:
        _redis: An instance of the Redis client.
    """

    def __init__(self) -> None:
        """
        Initializes the Cache class.

        Initializes an instance of Redis client and flushes the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis and returns the generated key.

        Args:
            data: The data to store in Redis. Can be str, bytes, int, float.

        Returns:
            str: The key under which the data is stored in Redis.
        """

        key = str(uuid.uuid4())

        self._redis.set(key, data)

        # Return the key
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis using the given key

        Args:
            key: The key to retrieve data from Redis.
            fn: An optional conversion function to apply to the retrieved data.

        Returns:
            Union[str, bytes, int, float, None]: data.
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
            Optional[str]: The retrieved string value, or None if no key.
        """
        return self.get(key, str.decode)

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer value from Redis using the given key.

        Args:
            key: The key to retrieve the integer value from Redis.

        Returns:
            Optional[int]: The retrieved integer value, or None if no key 
      """
        return self.get(key, int)

    def replay(method: Callable) -> None:
        """
        Display the history of calls of a particular function.

        Args:
        method: The function to display the history for.
        """
        # Get the qualified name of the method
        method_name = method.__qualname__

        # Connect to Redis
        r = redis.Redis()
        input_key = method_name + ":inputs"
        output_key = method_name + ":outputs"

        inputs = r.lrange(input_key, 0, -1)
        outputs = r.lrange(output_key, 0, -1)
        print(f"{method_name} was called {len(inputs)} times:")
        for input_data, output_data in zip(inputs, outputs):
            input_str = ", ".join(eval(input_data.decode()))
            print(f"{method_name}(*({input_str},)) -> {output_data.decode()}")
