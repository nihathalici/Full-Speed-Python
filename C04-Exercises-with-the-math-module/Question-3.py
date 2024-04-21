"""
Use the python documentation about the math module
(https://docs.python.org/3/ library/math.html) to solve the following exercises:

3. Use the "input" function to ask the user for a number and show the result of
the sine, cosine and tangent of the number. Make sure that you convert the user input
from string to a number (use the int() or the float() function).

"""
from math import sin, cos, tan

num = float(input("A number please: "))

print("Sine of number {} is {}".format(num, sin(num)))
print("Cosine of number {} is {}".format(num, cos(num)))
print("Tangent of number {} is {}".format(num, tan(num)))
