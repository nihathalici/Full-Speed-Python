"""
4. Create a function named "average" that computes the average value of a list
passed as parameter to the function.
Use the "sum" and "len" functions.
"""

def avg(li):
    return sum(li) / len(li)

my_list = [1, 2, 3, 4, 5]

print(avg(my_list))
