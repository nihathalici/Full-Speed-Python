For this section you may want to consult the python docs at https://docs.python.org/3/tutorial/controlflow.html#for-statements

* 1. Create a function "add" that receives a list as parameter and returns the sum of all elements in the list.

Use the "for" loop to iterate over the elements of the list.

```python
def add(li):
    my_sum = 0
    for item in li:
        my_sum += item
    return my_sum

my_list = [1, 2, 3, 4, 5]

print(add(my_list))
```

* 2. Create a function that receives a list as parameter and returns
the maximum value in the list. As you iterate over the list you may
want to keep the maximum value found so far in order to keep
comparing it with the next elements of the list.

```python
def max(li):
    max_val = 0
    for item in li:
        if item > max_val:
            max_val = item
    return max_val

my_list = [1, 2, 3, 4, 5]

print(max(my_list))
```




* 3. Modify the previous function such that it returns a list
with the first element being the maximum value and the second
being the index of the maximum value in the list.
Besides keep the last maximum value found so far,
you need to keep also the position where it occured.

```python
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
```


* Alternative solution:

```python
my_list = [1, 2, 3, 4, 5]
max_value = max(my_list)
max_index = my_list.index(max_value)

print("Maximum value of the list is {} and is on the index {}".format(max_value, max_index))
```
