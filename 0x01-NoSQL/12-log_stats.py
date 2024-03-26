#!/usr/bin/env python3

"""
Provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def nginx_logs_stats():
    """
    Provides statistics about Nginx logs stored in MongoDB.
    """
    # Connect to MongoDB and select the 'logs' database and 'nginx' collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Count the number of documents in the collection
    total_logs = collection.count_documents({})

    # Print the total number of logs
    print("{} logs where {} is the number of documents in this collection".format(total_logs, total_logs))

    # Print the number of documents with each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\t{}: {}".format(method, count))

    # Print the number of documents with method=GET and path=/status
    count_status = collection.count_documents({"method": "GET", "path": "/status"})
    print("1: {}".format(count_status))
