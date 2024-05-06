"""
For this section you may want to consult the python docs at
https://docs.python. org/3/tutorial/controlflow.html#for-statements.

2. Create a function that receives a list as parameter and returns
the maximum value in the list. As you iterate over the list you may
want to keep the maximum value found so far in order to keep
comparing it with the next elements of the list.
"""

def max(li):
    max_val = 0
    for item in li:
        if item > max_val:
            max_val = item
    return max_val

my_list = [1, 2, 3, 4, 5]

print(max(my_list))
