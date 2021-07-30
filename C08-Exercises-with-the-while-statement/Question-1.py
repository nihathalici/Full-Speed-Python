"""
Implement a function that receives a number as parameter and prints, in decreasing order,
which numbers are even and which are odd, until it reaches 0.
"""

def even_odd():
    n = int(input('Please enter a number: '))

    while (n >= 1):
        if n % 2 == 0:
            print("Even number: ", n)
        else:
            print("Odd number: ", n)
        n -= 1

even_odd()
