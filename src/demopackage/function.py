def demofunction(test):
    print(test)
    return
 
def hlo():
    print("this is python world")
    
hlo()     
demofunction("this is demo function")

# pass by refernse as value
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return
list = [34,5,6,9,100]
changeme(list)

def demo1(dd):
    print(dd)
    return;
demo1(dd = "My string") 

def printinfo( age, name):
    print("my name is: ", name)
    print("my age is :",age)
    
printinfo('ron',30)  


#Variable-length arguments
def demo2(value1, *multivalue):
    print(value1)
    for var in multivalue:
        print(var)
        
demo2(10)
demo2(34,677,'ganesh')      


# default arugment

def demo3(name, age=30):
    print("name: " , name)
    print ("Age: ", age)
demo3('ganesh')   


# lambda

sum = lambda v1,v2: v1+v2
print(sum(20,30))


  