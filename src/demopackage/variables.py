#how to assign value
from builtins import str

value = 100 # int
print(value)

na1 = str(value)
print(na1)
print("#########################################################")
value1 = "this is test string"   #string
listnm = list(value1)
print(listnm[0:2])


print("#########################################################")

print(value1)

value2 = 456.78 #float
print(value2)

#how to assign Multiple Assignment
a=b=c=100
print(a)
print(b)
print(c)

a,b,c = 1,22,"ganesh"
print(a)
print(b)
print(c)

# pythn string
value = "hello world python"  # string
print(value[0])
print(value[0:])
print(value[2:5])
print(value[2:])
print(value * 2)
print(value + " new value")


#list data type

list = ['abcd', 786 , 2.23, 'sarb', 70.2,]
tinylist = [123, 'ganesh']

print(list) # print the comple list
print(list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])    # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists

newlist = list[3:] + tinylist # creating new list from existing as per need
print(newlist)

# tuples data btype

tuple = ( 'test', 555 , 2.2377, 'john', 170.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete list
print (tuple[0] )      # Prints first element of the list
print (tuple[1:3] )     # Prints elements starting from 2nd till 3rd 
print (tuple[2:]   )    # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists


#dictionary data types
dicttest = {'name':'ganesh','dept': 'qa','company':'impetus'}
print(dicttest)  # print complete dictionary
print(dicttest['dept']) # print 2nd key

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(tinydict.keys()) # get all key
print(tinydict.values())  # get all values




