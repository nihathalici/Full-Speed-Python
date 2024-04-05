
* Initialize the string "abc" on a variable named "s":
(a) Use a function to get the length of the string.
(b) Write the necessary sequence of operations to transform the string "abc" in "aaabbbccc".

Suggestion: Use string concatenation and string indexes.
```python
s = "abc"

print(len(s))

s = s.replace("a", "aaa")
s = s.replace("b", "bbb")
s = s.replace("c", "ccc")

print(s)
```
