def my_func(param1='default'):
    print("my first python function! {}".format(param1))
my_func()

def hello():
    print("hello")
hello()

def hello():
    return "hello"
result = hello()
print(result)

def addNum(num1,num2):
    return num1+num2
result = addNum(2,3)
print(result)

def addNum1(num1,num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "sorry i need integer"
result = addNum1('2',3)
print(result)


#lambda expression also called anonymous function
my_list = [1,2,3,4,5,6,7,8]
evan = filter(lambda num:num%2 == 0,my_list)
print(list(evan))



#filter

mylist = [1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2 == 0

evans = filter(even_bool,mylist)
print(list(evans))


tweet = "Go Sports! #Sports"
result = tweet.split('#')[1]
print(result)


