"""
Create a list named "l" with the following values ([1, 4, 9, 10, 23]).
Using the Python documentation about lists
(https://docs.python.org/3.5/tutorial/introduction. html#lists)
solve the following exercises:

2. Append the value 90 to the end of the list "l".
Check the difference between list concatenation and the "append" method.
"""
# 1. method: append

l = [1, 4, 9, 10, 23]

l.append(90)

print(l)

# 2. method: concatenate a list with an integer

l = [1, 4, 9, 10, 23]

# In order to perform concatenation you must have two lists

concat_l = [90]

new_l = l + concat_l

print(new_l)
