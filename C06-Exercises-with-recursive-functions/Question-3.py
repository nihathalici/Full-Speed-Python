"""
3. The Fibonnaci sequence is a sequence of numbers in which each number of the sequence
matches the sum of the previous two terms.
Given the following recursive definition implement fib(n).
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Check your results for the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
"""

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
