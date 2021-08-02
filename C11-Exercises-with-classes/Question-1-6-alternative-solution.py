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
