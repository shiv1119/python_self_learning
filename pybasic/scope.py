from re import X


x = 25
def my_func():
    x = 50
    return x
print(x)
print(my_func())
my_func()
print(x)


#enclosing function locals ---- nested function
name = 'this is global name!'
def greet():
    name = 'sammy'
    def hello():
        print ('hello '+name)
    hello()
greet()
print(name)

##

y = 50
def func(y):
    print('y is :',y)
    y = 1000
    print('local y changed to:',y)
func(y)
print(y)
