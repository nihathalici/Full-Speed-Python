"""
Initialize the string "abc" on a variable named "s":

(a) Use a function to get the length of the string.
(b) Write the necessary sequence of operations to transform the string "abc" in "aaabbbccc".

Suggestion: Use string concatenation and string indexes.
"""

s = "abc"

print(len(s))

new_s = ""

for ch in s:
    new_s += ch * 3

print(new_s)
