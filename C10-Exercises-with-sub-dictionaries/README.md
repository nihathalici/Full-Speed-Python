Take the following dictionary:

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

* 1. How many students are in the "students" dict? Use the appropriate function.

```python
students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

print(len(students))
```

* 2. Implement a function that receives the students dict and returns the average age.

```python
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
```

* 3. Implement a function that receives the students dict and an address, and returns a list
with the name of all students which address matches the address in the argument.
For instance, invoking "find_students(students, ’Lisbon’)" should return Peter and Anna.

```python
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
```
