# 1 ----given a list of integers , return True if the sequence of numbers 1,2,3
#appears in the list

from ast import Num
from itertools import count


def arrayCheck(nums):
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    else:
        return False
nums=[1,2,4,4,5,6,7,8,9]
result=arrayCheck(nums)
print(result)


# 2------ given a string, return a new string made of every other character starting with first, so "Hello" yields "Hlo".

def stringBits(mystring):
    result = ""
    for i in range(len(mystring)):
        if i%2 == 0:
            result = result + mystring[i]
    return result
mystring = "string"
out = stringBits(mystring)
print(out) 

# 3------ 

def end_other(a,b):
    a = a.lower()
    b = b.lower()
    """return (b.endwith(a) or a.endwith(b))"""
    return a[-(len(b)):] == a or b == b[-len(a):]
output = end_other('Hiabc','abc')
print(output)

#4----

def doubleChar(my_string):
    result = ''
    for char in my_string:
        result += char*2
    return result
x = doubleChar('The')
print(x)

#5----
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
    if n [13,14,15,16,17,18]:
        return 0
    return n


#6 ---
def count_evans(nums):
    count = 0
    for elements in nums:
        if elements % 2 == 0:
            count += 1
    return count
nums = 1,2,3,4,5,6,7,8,9,10,11,12
z = count_evans(nums)
print(z)