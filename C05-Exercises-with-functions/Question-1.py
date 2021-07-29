"""
1. Implement the "add2" function that receives two numbers as arguments
and returns the sum of the numbers. Then implement the "add3" function
that receives and sums 3 parameters.
"""

def add2(num1, num2):
    return num1 + num2

print(add2(7, 3))

def add3(num1, num2, num3):
    return add2(num1, num2) + num3

print(add3(7, 3, 5))
