"""
Use the python documentation at https://docs.python.org/3/library/stdtypes. html#mapping-types-dict
to solve the following exercises.

Take the following python dictionary:

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

2. Implement a function that receives the "ages" dictionary as parameter and return the average age
of the students. Traverse all items on the dictionary using the "items" method as above.
"""
ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}

sum_ages = 0

for name, age in ages.items():
    sum_ages += age

avg_ages = sum_ages / len(ages)

print(round(avg_ages))
