"""
For this section you may want to consult the python docs at
https://docs.python. org/3/tutorial/controlflow.html#for-statements.

3. Modify the previous function such that it returns a list
with the first element being the maximum value and the second
being the index of the maximum value in the list.
Besides keep the last maximum value found so far,
you need to keep also the position where it occured.
"""

def max(li):
    max_val_l = []
    max_item = 0
    for i, item in enumerate(li):
        if item > max_item:
            max_item = item
    max_val_l.append( [max_item, i] )
    return max_val_l

my_list = [1, 2, 3, 4, 5]

print("Maximum value of the list is {} and is on the index {}".format(max(my_list)[0][0], max(my_list)[0][1]))



