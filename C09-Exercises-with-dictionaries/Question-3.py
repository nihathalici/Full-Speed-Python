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

3. Implement a function that receives the "ages" dictionary as parameter and returns the name
of the oldest student.
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

def oldest_std(di):
    oldest = 0
    for k, v in di.items():
        if v > oldest:
            oldest = v
    return "Oldest student is {} and is {} years old".format(k, oldest)
          

print(oldest_std(ages))

    
