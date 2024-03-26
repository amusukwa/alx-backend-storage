#!/usr/bin/env python3

"""
Retrieves all schools that cover a specific topic.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Retrieves all schools that cover a specific topic.

    Args:
        mongo_collection: pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of school documents that cover the specified topic.
    """
    # Query the collection to find documents that contain the specified topic in their 'topics' field
    schools = mongo_collection.find({"topics": topic})

    # Convert the cursor to a list and return it
    return list(schools)
