Use the python documentation about the math module
( https://docs.python.org/3/library/math.html ) to solve the following exercises:


* 1. Find the greatest common divisor of the following pairs of numbers:

(15, 21), (152, 200), (1988, 9765).

```python
from math import gcd

print("GCD of 15 and 21 is:", gcd(15, 21))
print("GCD of 152 and 200 is:", gcd(152, 200))
print("GCD of 1988 and 9765 is:", gcd(1988, 9765))
```



* 2. Compute the base-2 logarithm of the following numbers: 0, 1, 2, 6, 9, 15.

```python
from math import log2

# 0 causes a ValueError
nums = [ 1, 2, 6, 9, 15 ]

for num in nums:
    print("Base-2 logarithm of {} is {}".format(num, log2(num)))
```



* 3. Use the "input" function to ask the user for a number and show the result of
the sine, cosine and tangent of the number. Make sure that you convert the user input
from string to a number (use the int() or the float() function).

```python
from math import sin, cos, tan

num = float(input("A number please: "))

print("Sine of number {} is {}".format(num, sin(num)))
print("Cosine of number {} is {}".format(num, cos(num)))
print("Tangent of number {} is {}".format(num, tan(num)))
```
