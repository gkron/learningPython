#artthmatic
a = 30
b = 20
c= a+b
# print(c)
# c = a*b
# print(c)
# c= a%b
# print(c)
# c= a/b
# print(c)
# c= a**b
# print(c)

#Comparison Operators
print(a==b)
print(a>=b)
print(a>b)
print(a<b)
print(a<=b)
print(a!=b)

#Assignment Operators

a = 30
d=40
# d +=a
# print(d)
# d-=a
# print(d)

print(a & b)

#Membership Operators

name = "this is me"
if('tz' in name):
    print("pass")
else:
    print("fail")

####################
if('tz' not in name):
    print("pass")
else:
    print("fail")

#Identity Operators
a = 30
b = 40
if(a is b):
    print("matching")
else:
    print("not matching")  

if(a is not b):
    print("matching")
else:
    print("not matching")  
                    
#########################

if(id(a) is not id(b)):
    print("matching")
else:
    print("not matching")          
