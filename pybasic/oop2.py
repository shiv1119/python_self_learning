class Dog():
    
    #class object attributes...
    species = "mammal"
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
mydog = Dog(breed = "lab",name="sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)


class Circle():
    pi = 3.14
    
    def __init__(self,radius=1):
        self.radius = radius
        
    def area(self):
        return self.radius*self.radius * Circle.pi
    def set_radius(self,new_r):
        self.radius = new_r
    
my_circle = Circle(3)
my_circle.set_radius(999)
print(my_circle.area())


