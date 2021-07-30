"""
For this section you may want to consult the python docs at
https://docs.python. org/3/tutorial/controlflow.html#for-statements.

3. Modify the previous function such that it returns a list
with the first element being the maximum value and the second
being the index of the maximum value in the list.
Besides keep the last maximum value found so far,
you need to keep also the position where it occured.
"""

my_list = [1, 2, 3, 4, 5]
max_value = max(my_list)
max_index = my_list.index(max_value)

print("Maximum value of the list is {} and is on the index {}".format(max_value, max_index))
