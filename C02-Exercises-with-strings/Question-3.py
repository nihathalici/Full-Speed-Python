'''
Starting from the string "aaa bbb ccc", what sequences of operations
do you need to arrive at the following strings?
You can find the "replace" function.

(a) "AAA BBB CCC"
(b) "AAA bbb CCC"

'''

s = "aaa bbb ccc"
print(s)

s = s.upper()
print("The string upper() method changes all lowercase to uppercase: ", s)

s = "aaa bbb ccc"
s = s.replace("a", "A")
s = s.replace("c", "C")

print(s)
