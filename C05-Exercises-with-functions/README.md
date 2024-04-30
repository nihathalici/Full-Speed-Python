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


* 3. Implement a function named "is_divisible" that receives two parameters (named "a" and "b")
and returns true if "a" can be divided by "b" or false otherwise.

A number is divisible by another when the remainder of the division is zero.
Use the modulo operator ("%").

```python
def is_divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False

my_num_1 = int(input("Number 1: "))
my_num_2 = int(input("Number 2: "))

print(is_divisible(my_num_1, my_num_2))
```


* 4. Create a function named "average" that computes the average value of a list passed as parameter to the function.
Use the "sum" and "len" functions.

```python
def avg(li):
    return sum(li) / len(li)

my_list = [1, 2, 3, 4, 5]

print(avg(my_list))
```
