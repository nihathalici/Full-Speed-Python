"""
1. Implement the "add2" function that receives two numbers as arguments
and returns the sum of the numbers. Then implement the "add3" function
that receives and sums 3 parameters.
"""

def add2(num1, num2):
    print("Function add2 got value", num1, "and", num2)
    return num1 + num2

my_num_1 = int(input("Number 1: "))
my_num_2 = int(input("Number 2: "))

print(add2(my_num_1, my_num_2))

def add3(num1, num2, num3):
    print("Function add3 got value",num1,"," ,num2, "and", num3)
    return num1 + num2 + num3

my_num_3 = int(input("Number 3: "))

print(add3(my_num_1, my_num_2, my_num_3))
