"""
2. Implement a function that returns the greatest of two numbers given as parameters.
Use the "if" statement to compare both numbers:
https://docs.python.org/3/ tutorial/controlflow.html#if-statements.
"""

def comp(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

my_num_1 = int(input("Number 1: "))
my_num_2 = int(input("Number 2: "))

print(comp(my_num_1, my_num_2))






    
