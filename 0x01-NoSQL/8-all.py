#!/usr/bin/env python3

"""
This module provides a function to list all documents in a MongoDB collection.
"""

import pymongo

def list_all(mongo_collection):
    """
    Retrieve all documents from the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
        list: A list containing all documents in the collection.
    """
    # Use find() to retrieve all documents in the collection
    cursor = mongo_collection.find({})
    
    # Initialize an empty list to store the documents
    all_documents = []

    for document in cursor:
        all_documents.append(document)
    
    return all_documents
