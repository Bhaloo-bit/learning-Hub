# i was treating list as array  ...but it is acutally true beccause most of the time we will use list 
# as array .// therefore i have to learn array first to begin DSA :)
# 
from array import *

mynums = array('i', [1,2,3,4,5,6,])
# print(mynums)
# print(type(mynums))

mynumns = ('1','2','3','4')
# print(type(mynumns))

myname = ('bipul', 'kumar', 'nirala')
# print(type(myname))


mydec = {
    "name" : "bipul",
    "age": 18

}

mydec["age"] = 23,
# print(mydec["age"])
# print(type(mynums))

# Newarry = array(mynums.typecode, (x for x in array))
# print(Newarry)

mylist = [1,3,4,5,6,7,8]
newlist = mylist.copy()
print(mylist)
print(newlist)


#/**********  /
from array import *

val = array('i',[1,2,3,4,5,6,7,8,9,])

copyArray = array(val.typecode, (x for x in val))
# print(copyArray)

# copyArray.pop(3)
# print(val[2:5])

# print(val[::-1])

# for i in range(0,len(copyArray)):
#     print(copyArray[i], end=', ')


#taking input from user and make an array out of it

userarry = array('i',[])
 
n = int(input("Enter the lenth of arry :"))
for i in range(0 ,n):
    num = int(input('Enter the next no: '))
    userarry.append(num)

print(userarry)    

