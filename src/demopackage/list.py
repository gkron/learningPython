from filecmp import cmp
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 10,45,99, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

# we can do indexing, slicing, adding, multiplying,
print(list1)
print(list2[2:3])

# we can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator, and you can add to elements in a list with the append() 


# delete list element
del list1[0]
print(len(list1))
print(list1+list2)
print(list1*2)

print(1997 in list1)
print(19973 in list1)

# built in funation in list
#cmp(list1, list2)Compares elements of both lists. # not supported in python 3 cmp

#max & min value from list
print(max(list2))
print(min(list2))

# convert tuple to list
aTuple = (123, 'xyz', 'zara', 'abc');
newls = list(aTuple)
print(newls)

# how to get length of list
print(len(newls))

# how to add new value in list
print(list1)
list1.append(2020)

print(list1)


#count()-- how amny time obj occur in list

aList = [123, 'xyz', 'zara', 'abc', 123];
print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))

# extend() appends the contents of seq to list.

list1.extend(aList)
print(list1)

# index() returns the lowest index in list that obj appears.
print(list1.index('chemistry'))
# reverse a list
list1.reverse()
print(list1)

# insert() inserts object obj into list at offset index.
mylist = [23,45,'ganesh','gold']
mylist.insert(7, 503)
print(mylist)

# pop remove the object frm list bat last
# mylist.pop()
# print(mylist)

list2.sort()
print(list2)
