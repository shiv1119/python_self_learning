#booleans --- true, false, 0 , 1
#tuples

t = (1,2,3,4,5)
print(t[0])

tup = ('a', True , 123) #can hold different data types...
#tup[0]= 'new'  # it will give error because tuples are immutables 
print(tup)

#sets

x = set()  #it have unique elements  and it returns value in arranged  order 
x.add(1)
x.add(2)
x.add(4)
x.add(4)
x.add(0.1)
print(x)