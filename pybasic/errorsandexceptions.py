# we ca use keywords to dictate our logic in case of error
#   1----Try
#   2----Except
#   3----Finally


from typing import IO

"""
try:
    f = open("error.txt","w")    #if i go with "w" the error could not be found and our last section gets deployed
    f.write("text write to simple text")
except IOError:
    print("ERROR: could not find file and read data")
else:
    print("success")
    f.close()"""
    

try:
    f = open("error.txt","r")    #in this error got catched and our last section code does not gets deployed
    f.write("text write to simple text")
except IOError:
    print("ERROR: could not find file and read data")
else:
    print("success")
    f.close()
print("hello world")


try:
    f = open("error.txt","r")    #in this error got catched and our last section code does not gets deployed
    f.write("text write to simple text")
except IOError:
    print("ERROR: could not find file and read data")
finally:
    print("I always work")
    f.close()
    
