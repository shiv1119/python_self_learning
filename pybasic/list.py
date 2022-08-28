#mylist = [1, 2, 3]
#print(len(mylist))

#adding items into list
#li = ['a', 'b', 'c', 'd', 'e']
#li[0] = 'New item'
#print(li)

mylist = [1, 2, 3, 8, 5, 7]
#mylist.append(["new ","item"])
listtwo = [10,12]
mylist.extend(listtwo)
print(mylist)
item = mylist.pop(2)
print(mylist)
print(item)
mylist.reverse()
print(mylist)
mylist.sort()
print(mylist)

# nested list
my_list = [1, 2, 3, ['x', 'y', 'z']]
print(my_list[3][1])

#list comprehension
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
first_col = [row[0] for row in matrix]
print(first_col)