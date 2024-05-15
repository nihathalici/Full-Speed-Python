"""
Take the following dictionary:

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

3. Implement a function that receives the students dict and an address, and returns a list
with the name of all students which address matches the address in the argument.
For instance, invoking "find_students(students, ’Lisbon’)" should return Peter and Anna.
"""

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}


def addr_search(li):
    adr_li = []
    adr_val = str(input("Address?"))

    for k, v in li.items():
        if v["address"] == adr_val:
            adr_li.append(k)
    return ", ".join(adr_li)

print(addr_search(students))
