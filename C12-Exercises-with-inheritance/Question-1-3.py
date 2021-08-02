"""
Use the "Rectangle" class as implemented above for the following exercises: 
1. Create a "Square" class as subclass of "Rectangle".
2. Implement the "Square" constructor. The constructor should have only the x1, y1 coordinates and the size of the square. 
Notice which arguments you’ll have to use when you invoce the "Rectangle" constructor when you use "super".
3. Instantiate two objects of "Square", invoke the area method and print the objects. 
Make sure that all calculations are returning correct numbers and that the coordinates of the squares 
are consistent with the size of the square used as argument.
"""

# inherits Question-1-6-alternative-solution.py at 
# https://github.com/nihathalici/Full-Speed-Python/blob/main/C11-Exercises-with-classes/Question-1-6-alternative-solution.py

class Square(Rectangle):
    def __init__(self,x1,y1,size):
        super().__init__(x1,y1,x1+size,y1+size)

my_sq = Square(1,2,2)

print(my_sq.area()) # outputs: 4

print(my_sq.width()) # outputs: 2

print(my_sq.height()) # outputs: 2

print(my_sq.circumference()) # outputs: 8
