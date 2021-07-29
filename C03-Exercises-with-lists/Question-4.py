"""
Create a list named "l" with the following values ([1, 4, 9, 10, 23]).
Using the Python documentation about lists
(https://docs.python.org/3.5/tutorial/introduction. html#lists)
solve the following exercises:

4. Remove the sublist [4, 9].
"""
# 1. remove method
l = [1, 4, 9, 10, 23]

l.remove(4)
l.remove(9)

print(l)

# 2. pop method
l = [1, 4, 9, 10, 23]

l.pop(1)
l.pop(1)

print(l)

# or 2. pop method / another way
l = [1, 4, 9, 10, 23]

l.pop(2) and l.pop(1)

print(l)

# 3. del method
l = [1, 4, 9, 10, 23]

del l[1]
del l[1]

print(l)

