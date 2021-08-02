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
