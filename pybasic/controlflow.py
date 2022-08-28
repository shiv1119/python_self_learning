if 1>2:
    print("hello")
elif 3==3:
    print("elif ran")
else:
    print("last")


#loops
#for loops

seq = [1,2,3,4,5,6,7,8]

for item in seq:
    #code
    print(item)
    
    
d = {'sam': 1, 'frank': 2, 'dan':3}
for items in d:
    print(items)
for k in d:
    print(k)
    print(d[k])

mypairs = [(1,2),(3,4),(5,6)]
for (tup1,tup2) in mypairs:
    print(tup2)
    print(tup1)
    
#while loop

i = 1

while i<5:
    print("i is: {}".format(i))
    i = i+1
    
#range
for a in range(2,21,2):
    print(a)
    
x = [1,2,3,4,5]
output = []
for num in x:
    output.append(num**2)
print(output)

y = [1,2,3,4,5]
out = [num**2 for num in x]
print(out)