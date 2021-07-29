"""
Use the python documentation about the math module
(https://docs.python.org/3/ library/math.html) to solve the following exercises:

2. Compute the base-2 logarithm of the following numbers: 0, 1, 2, 6, 9, 15.
"""
from math import log2

# 0 causes a ValueError
nums = [ 1, 2, 6, 9, 15 ]

for num in nums:
    print("Base-2 logarithm of {} is {}".format(num, log2(num)))


