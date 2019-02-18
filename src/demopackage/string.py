val1 = "this is hello world"
val2 = "thisispython language"

print(val1[0:7])
print(val2[:8])
# update string value
print(val1[:6] + ' new string')
print(val1[0])
print("worldd" in val1)
print("worldd" not in val1)
print("My name is %s and weight is %d kg!" % ('Zara', 21))

# triple quotes

para_str = """this is a long string\nthat is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

print(para_str)
print ('C:\\nowhere')
print(val1.capitalize())
print(val1.upper() or  val2.lower())

# substring count

str = "this is string example....wow!!!";
sub = 't'
print(str.count(sub))
print(str.count(sub, 2, 40))

# find string if string in another string if string not found return -1 else index of string

str1 = "this is string example....wow!!!";
str2 = "exddam";
str3 = "this"
print (str1.find(str3))
print (str1.find(str2, 10))

# index method if string not found return exception else index of string

str1 = "this is string example....wow!!!";
str2 = "exam";
str3 = "sonia"
print (str1.index(str2))
#print(str1.index(str3))


strstrp = "     this is string example....wow!!!     ";
print(strstrp.lstrip()) # remove space from bigning

print(strstrp.rstrip()) # re remove spce from end

print(strstrp.strip()) # remove spce frm both end
print(strstrp.strip('!'))
#split--return list of object

gk1 = "Line1-abcdef \nLine2-abc \nLine4-abcd";

print(gk1.split())

# swapcase
print(gk1.swapcase())

#title 
strnm = "this is string example....wow!!!";
print (strnm.title())


#rfind()  This method returns last index if found and -1 otherwise.
rever = "this is test based"
st= 'd'
print(rever.rfind(st))

strmm = "this-is-real-string-example....wow!!!";

print(min(strmm))

print(max(strmm))

#replace old char with new
replcename = "this is string example....wow!!! this is really string"

print(replcename.replace("is", "was"))

