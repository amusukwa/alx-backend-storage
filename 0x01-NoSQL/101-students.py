#!/usr/bin/env python3

"""
Returns all students sorted by average score.
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of student documents with average score included, sorted.
    """
    students = []

    # Iterate over each student document in the collection
    for student in mongo_collection.find():
        # Calculate the average score for the student
        scores = [topic['score'] for topic in student['topics']]
        average_score = sum(scores) / len(scores) if len(scores) > 0 else 0

        # Add the average score to the student document
        student['averageScore'] = average_score
        students.append(student)

    # Sort the students by average score in descending order
    sorted_students = sorted(students, key=lambda x: x['averageScore'], reverse=True)

    return sorted_students
