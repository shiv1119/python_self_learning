#inheritance 


class Animal():
    def __init__(self):
        print("Animal Created")
    def whoAmI(self):
        print("animal")
    def eat(self):
        print("eating")

class Dog(Animal):
    
    def __init__(self):
        #Animal.__init__(self)
        print("Dog created")
    def bark(self):
        print("woof")
        
    def eat(self):     #overwriting
        print('Dog Eating')
mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()




# special method

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)
    
    def __len__(self):
        return self.pages
    def __del__(self):
        print("the book got destroyed!")
    
        
b = Book("python","jose",200)
print(len(b))
del b
