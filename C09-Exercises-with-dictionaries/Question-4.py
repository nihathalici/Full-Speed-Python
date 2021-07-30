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

4. Implement a function that receives the "ages" dictionary and a number "n" and returns a new dict
where each student is n years older. For instance, new_ages(ages, 10) returns a copy of "ages"
where each student is 10 years older.
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

def new_ages(di):
    new_di = {}
    n = int(input("How many years older? "))

    for k, v in di.items():
        new_di[k] = v + n
    return new_di

print(new_ages(ages))

    
