#!/usr/bin/env python3

"""
Provides statistics about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient
from collections import Counter

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
    print("{} logs".format(total_logs))

    # Print the number of documents with each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("method {}: {}".format(method, count))

    count_status = collection.count_documents({"method": "GET", "path": "/status"})
    print("status check: {}".format(count_status))

    ip_counter = Counter(doc['ip'] for doc in collection.find({}, {'ip': 1}))
    top_ips = ip_counter.most_common(10)
    print("IPs:")
    for ip, count in top_ips:
        print("\t{}: {}".format(ip, count))

if __name__ == "__main__":
    nginx_logs_stats()
