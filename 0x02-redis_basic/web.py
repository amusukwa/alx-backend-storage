#!/usr/bin/env python3
import requests
import redis
import time


def get_page(url: str) -> str:
    """
    Retrieve HTML content of URL and cache the result

    Args:
        url (str): The URL to retrieve the HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    # Connect to Redis
    r = redis.Redis()

    # Increment the count for the URL
    count_key = f"count:{url}"
    r.incr(count_key)

    # Get the cached content if available
    cached_content = r.get(url)
    if cached_content:
        return cached_content.decode()

    # Retrieve the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Cache the HTML content with an expiration time of 10 seconds
    r.setex(url, 10, html_content)

    return html_content

# Test the get_page function
if __name__ == "__main__":
    # Simulate accessing a slow URL multiple times
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://www.example.com"
    for i in range(5):
        print(f"Accessing {url}... (attempt {i + 1})")
        start_time = time.time()
        content = get_page(url)
        print(f"Content length: {len(content)}")
        end_time = time.time()
        print(f"Time taken: {end_time - start_time:.2f} seconds")

