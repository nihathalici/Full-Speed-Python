"""
Initialize the string "aaabbbccc" on a variable named "s":

(a) Use a function that allows you to find the first occurence
of "b" in the string, and the first occurence of "ccc".

(b) Use a function that allows you to replace all occurences of "a" to "X",
and then use the same function to change only the first occurence of "a" to "X".
"""

s = "aaabbbccc"

first_b = s.find("b")
first_ccc = s.find("ccc")

print("'b' first appears at index:", first_b, "and 'ccc' first appears at index:", first_ccc)

s = s.replace("a", "X")
print("All 'a's changed to 'X': ", s)

s = "aaabbbccc"
s = s.replace("a", "X", 1)
print("Only the first occurence of 'a' changed to 'X': ", s)

