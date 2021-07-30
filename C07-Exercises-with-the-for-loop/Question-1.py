"""
For this section you may want to consult the python docs at
https://docs.python. org/3/tutorial/controlflow.html#for-statements.

1. Create a function "add" that receives a list as parameter and returns
the sum of all elements in the list.

Use the "for" loop to iterate over the elements of the list.
"""

def add(li):
    my_sum = 0
    for item in li:
        my_sum += item
    return my_sum

my_list = [1, 2, 3, 4, 5]

print(add(my_list))
