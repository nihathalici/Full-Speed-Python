"""
Take the following dictionary:

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

2. Implement a function that receives the students dict and returns the average age.
"""

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

def avg_std(di):
    ages_sum = 0
    for sub in di.values():
        ages_sum += sub["age"]
    avg_age = ages_sum / len(di)
    return int(avg_age)

print(avg_std(students))
