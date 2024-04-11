* Create a list named "l" with the following values ([1, 4, 9, 10, 23]). Using the Python documentation about lists
( https://docs.python.org/3.5/tutorial/introduction.html#lists ) solve the following exercises:

1. Using list slicing get the sublists [4, 9] and [10, 23].

```python
l = [1, 4, 9, 10, 23]

sub_l_1 = l[1:3]
print(sub_l_1)

sub_l_2 = l[-2:]
print(sub_l_2)

# or
sub_l_2 = l[3:5]
print(sub_l_2)

# or
sub_l_2 = l[3:]
print(sub_l_2)
```

* Create a list named "l" with the following values ([1, 4, 9, 10, 23]). Using the Python documentation about lists
( https://docs.python.org/3.5/tutorial/introduction.html#lists ) solve the following exercises:

Append the value 90 to the end of the list "l".

Check the difference between list concatenation and the "append" method.

```python
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
```
