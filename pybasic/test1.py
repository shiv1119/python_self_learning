#problem 1
s = "django"
# use indexing to print
# 'd'
print(s[0])

#'0'
print(s[-1])

#'djan'
print(s[:-2])

#'jan'
print(s[1:-2])

#'go'
print(s[4:])

#bonus : use indexing to reverse
print(s[::-1])

#problem 2

l = [3, 7, [1, 4,'hello']]
#reassign hello to goodbye
l[2][2] = 'goodbye'
print(l)


#problem 3

d1 = {'simple_key': ' hello'}
d2 = { 'k1': {'k2': 'hello'}}
d3 = { 'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])

#problem 4
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
mylist = set(mylist)
print(mylist)

#problem 5

age = 4
name = "Sammy"

#Use print formatting to print the following string
#"Hello my dog's name is Sammy and he is 4 years old "
dog="Hello my dog's name is {name} and he is {age} years old".format(name="Sammy", age="4")
print(dog)