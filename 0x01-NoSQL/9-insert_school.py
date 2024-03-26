#!/usr/bin/env python3

"""
Inserts a new document in a collection based on kwargs.
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object.
        **kwargs: keyword arguments representing the fields and values of the document to be inserted.

    Returns:
        The _id of the newly inserted document.
    """
    # Insert the document using insert_one() and return the _id
    return mongo_collection.insert_one(kwargs).inserted_id
