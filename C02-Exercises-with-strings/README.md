
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

Another solution:
```python
s = "abc"

print(len(s))

new_s = ""

for ch in s:
    new_s += ch * 3

print(new_s)
```


* Initialize the string "aaabbbccc" on a variable named "s":

(a) Use a function that allows you to find the first occurence
of "b" in the string, and the first occurence of "ccc".

(b) Use a function that allows you to replace all occurences of "a" to "X",
and then use the same function to change only the first occurence of "a" to "X".

```python
s = "aaabbbccc"

first_b = s.find("b")
first_ccc = s.find("ccc")

print("'b' first appears at index:", first_b, "and 'ccc' first appears at index:", first_ccc)

s = s.replace("a", "X")
print("All 'a's changed to 'X': ", s)

s = "aaabbbccc"
s = s.replace("a", "X", 1)
print("Only the first occurence of 'a' changed to 'X': ", s)
```



* Starting from the string "aaa bbb ccc", what sequences of operations do you need to arrive at the following strings?
You can find the "replace" function.

(a) "AAA BBB CCC"
(b) "AAA bbb CCC"

```python
s = "aaa bbb ccc"
print(s)

s = s.upper()
print("The string upper() method changes all lowercase to uppercase: ", s)

s = "aaa bbb ccc"
s = s.replace("a", "A")
s = s.replace("c", "C")

print(s)
```
