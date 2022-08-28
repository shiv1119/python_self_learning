# making program to find area of circle and radius using class object


#circle:-

class Circle():
    pi = 3.14
    
    def __init__(self, radius=1):       #if radius is not given it will take default value 1
        self.radius = radius
        
    def area(self):
        return self.radius*self.radius * Circle.pi
    
    def set_radius(self,new_radius):
        self.radius = new_radius
    
my_circle = Circle()
my_circle.set_radius(999)
print(my_circle.area())



#rectangle:-

class Rectangle():
    def __init__(self,length=1,width=1):      #if length and width not given then it will take default value of 1
        self.length = length
        self.width = width
    def area_rectangle(self):
        return self.length*self.width
    def set_dimension(self,new_length,new_width):
        self.length = new_length
        self.width = new_width        
my_rectangle = Rectangle()
my_rectangle.set_dimension(10,10)
print(my_rectangle.area_rectangle())