"""
4. Create a function named "average" that computes the average value of a list
passed as parameter to the function.
Use the "sum" and "len" functions.
"""
import random

def get_avg(li):
    return sum(li)/len(li)

count = 0
my_li = []

while count < 10:
    my_li.append(random.randint(0, 1000))
    count += 1
print("List:", my_li)

print("Average:", get_avg(my_li))




    
