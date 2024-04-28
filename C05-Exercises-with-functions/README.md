* 1. Implement the "add2" function that receives two numbers as arguments
and returns the sum of the numbers. Then implement the "add3" function
that receives and sums 3 parameters.

```python
def add2(num1, num2):
    return num1 + num2

print(add2(7, 3))

def add3(num1, num2, num3):
    return add2(num1, num2) + num3

print(add3(7, 3, 5))
```

* Another solution

```python
def add2(num1, num2):
    print("Function add2 got value", num1, "and", num2)
    return num1 + num2

my_num_1 = int(input("Number 1: "))
my_num_2 = int(input("Number 2: "))

print(add2(my_num_1, my_num_2))

def add3(num1, num2, num3):
    print("Function add3 got value",num1,"," ,num2, "and", num3)
    return num1 + num2 + num3

my_num_3 = int(input("Number 3: "))

print(add3(my_num_1, my_num_2, my_num_3))
```


* 2. Implement a function that returns the greatest of two numbers given as parameters.
Use the "if" statement to compare both numbers:
https://docs.python.org/3/ tutorial/controlflow.html#if-statements.

```python
def comp(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

my_num_1 = int(input("Number 1: "))
my_num_2 = int(input("Number 2: "))

print(comp(my_num_1, my_num_2))
```
