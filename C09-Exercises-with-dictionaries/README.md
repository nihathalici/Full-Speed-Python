* Use the python documentation at https://docs.python.org/3/library/stdtypes.html#mapping-types-dict to solve the following exercises.

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

* 1. How many students are in the dictionary? Search for the "len" function.

```python
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

print(len(ages))
```

* 2. Implement a function that receives the "ages" dictionary as parameter and return the average age
of the students. Traverse all items on the dictionary using the "items" method as above.

```python
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
```

* 3. Implement a function that receives the "ages" dictionary as parameter and returns the name
of the oldest student.
```python
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
```
