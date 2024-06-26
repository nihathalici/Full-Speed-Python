Use the python documentation on classes at https://docs.python.org/3/tutorial/classes.html to solve the following exercises.

* 1. Implement a class named "Rectangle" to store the coordinates of a rectangle
given the top-left corner (x1, y1) and the bottom-right corner (x2, y2).

* 2. Implement the class constructor with the parameters (x1, y1, x2, y2)
and store them in the class instances using the "self" keyword.

* 3. Implement the "width()" and "height()" methods which return,
respectively, the width and height of a rectangle.
Create two objects, instances of "Rectangle" to test the calculations.

* 4. Implement the method "area" to return the area of the rectangle (width*height).

* 5. Implement the method "circumference" to return the perimeter
of the rectangle (2*width + 2*height).

* 6. Do a print of one of the objects created to test the class.
Implement the "__str__" method such that when you print one of the objects
it print the coordinates as (x1, y1)(x2, y2).

```python
class Rectangle():
    # get the coordinates as tuples
    def __init__(self, init_tL, init_bR):
        self.topLeft = init_tL
        self.topRight = (init_bR[0], init_tL[1])
        self.bottomLeft = (init_bR[1], init_tL[0])
        self.bottomRight = init_bR

        # Compute the width and height
        self.width = init_bR[0] - init_tL[0]
        self.height = init_bR[1] - init_tL[1]

    def __str__(self):
        return 'Top Left = ' + str(self.topLeft) + ', Top Right = '+ str(self.topRight)+', Bottom Left = '+ str(self.bottomLeft) + ', Bottom Right = ' +str(self.bottomRight)

    def area(self):
        return (self.width * self.height)

    def circumference(self):
        return (2 * self.width + 2 * self.height)
        

my_rectangle = Rectangle((5,5), (30, 20))
print(my_rectangle)
print(my_rectangle.width) #output 25
print(my_rectangle.height) #output 15
print(my_rectangle.area()) #output 375
print(my_rectangle.circumference()) # output 80
```

* Alternative solution:

```python
class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return 'coordinate:%s,%s'%((self.x1,self.y1),(self.x2,self.y2))

    def width(self):
        width = abs(self.x1-self.x2)
        return width

    def height(self):
        height = abs(self.y1-self.y2)
        return height

    def area(self):
        return self.width()*self.height()

    def circumference(self):
        return 2*self.width()+2*self.height()


my_rectangle = Rectangle(5, 5, 30, 20)

print(my_rectangle) # output: coordinate:(5, 5),(30, 20)

print(my_rectangle.width()) # output: 25

print(my_rectangle.height()) # output: 15

print(my_rectangle.area()) # # output: 375

print(my_rectangle.circumference()) # output: 80
```
