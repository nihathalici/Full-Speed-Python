C01 / Exercises with numbers
========================================================
* Try the following mathematical calculations and guess what is happening:
(3/2),(3//2),(3%2),(3∗∗2).
Suggestion:
Check the python library reference at
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex.

```python
print("Division:", 3 / 2)
print("Floor Division", 3 // 2)
print("Finding the remainder:", 3 % 2)
print("Multiplying to the power of 2:", 3 ** 2)
```


* Calculate the average of the following sequences of numbers:
(2, 4), (4, 8, 9), (12,14/6, 15)

```python
x = [2, 4]
y = [4, 8, 9]
z = [12, 14 / 6, 15]

print("Average of list x is:", sum(x) / len(x))
print("Average of list y is:", sum(y) / len(y))
print("Average of list z is:", sum(z) / len(z))
```


* The volume of a sphere is given by 4/3πr. Calculate the volume of a sphere of radius 5.
Suggestion:
Create a variable named "pi" with the value of 3.1415

```python
pi = 3.1415
my_rad = 5
my_vol = (4 / 3 * pi * my_rad)
print(my_vol)
```
