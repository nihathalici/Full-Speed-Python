"""
3. Implement a function named "is_divisible" that receives two parameters (named "a" and "b")
and returns true if "a" can be divided by "b" or false otherwise.

A number is divisible by another when the remainder of the division is zero.
Use the modulo operator ("%").
"""

def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False

my_num_1 = int(input("Number 1: "))
my_num_2 = int(input("Number 2: "))

print(is_divisible(my_num_1, my_num_2))
