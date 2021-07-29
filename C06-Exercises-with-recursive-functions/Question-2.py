"""
2. Implement a recursive function to compute the sum of the n first integer numbers
(where n is a function parameter). Start by thinking about the base case
(the sum of the first 0 integers is?) and then think about the recursive case.
"""

li = [1, 1, 3, 3, 6, 6, 7, 51, 75]

while True:
    try:
        print(li)
        print('Get item 1:', li[0], 'and added to item 2:', li[1])
        first_second_item = li.pop(0) + li.pop(0)
        li.insert(0, first_second_item)
        print(first_second_item)
    except:
        print("No more items")
        break

