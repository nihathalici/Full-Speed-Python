"""
Create a list named "l" with the following values ([1, 4, 9, 10, 23]).
Using the Python documentation about lists
(https://docs.python.org/3.5/tutorial/introduction. html#lists)
solve the following exercises:

3. Calculate the average value of all values on the list.
You can use the "sum" and "len" functions.
"""

l = [1, 4, 9, 10, 23]

sum_l = sum(l)

print("The sum of the list l is: {}".format(sum_l))

avg_l = sum(l) / len(l)

print("The average for the list l is: {}".format(avg_l))
