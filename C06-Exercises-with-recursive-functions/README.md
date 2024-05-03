* 1. Implement the factorial function and test it with several different values.
Cross-check with a calculator.

```python
from math import factorial
from random import randint

count = 1

while count != 6:
    x = randint(0, 7)
    print("Test " + str(count) + " for number " + str(x) + ":", factorial(x))
    count += 1
```



* 2. Implement a recursive function to compute the sum of the n first integer numbers (where n is a function parameter). Start by thinking about the base case
(the sum of the first 0 integers is?) and then think about the recursive case.

```python
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
```


* 3. The Fibonnaci sequence is a sequence of numbers in which each number of the sequence matches the sum of the previous two terms.
Given the following recursive definition implement fib(n).
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Check your results for the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

```python
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)

n = int(input())

val = [str(f(x)) for x in range(0, n + 1)]

print(",".join(val))
```
