"""
Use the module operator (%) to check which of the following
numbers is even or odd: (1, 5, 20, 60/7).
Suggestion:
The remainder of x/2 is always zero when x is even.
"""

nums = [1, 5, 20, 60/7]

even_n = []
odd_n = []

for num in nums:
    if num % 2 == 0:
        even_n.append(num)
    else:
        odd_n.append(num)

print("Even numbers: ")
print("".join(str(even_n)))

print("Odd numbers: ")
print("".join(str(odd_n)))
