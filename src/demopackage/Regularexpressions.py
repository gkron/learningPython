import re
from lib2to3.pgen2.tokenize import group

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
    
   print ("No match!!")
   
   # search experpssion
   
string1 = "sometimes friends are better then brother"

searchobj = re.search('(.*) better (.*?) .*',string1)

if searchobj:
  #  print(searchobj.group())
    print(searchobj.group(2))
else:
    print("no matching !!")    



# Matching Versus Searching

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'dogs', line)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")
   
   
# Search and Replace
phone = "2004-959-559 # This is Phone Number"

num  = re.sub('#.*$', "", phone)

print("Phone Number is: ", num)

num2 = re.sub(r'\D', "", phone)  # remove anything aprt from digit
print("phone Number is: ", num2)

str="x8f8dL:s://www.qqq.zzz/iziv8ds8f8.dafidsao.dsfsi"

m = re.search(r"//([^/]*)", str)
print(m.group(1))

m2 = re.search(r"(?<=//)[^/]*", str)

print(m2.group())

str="x8f8dL:s://www.qqq.zzz/iziv8ds8f8.dafidsao.dsfsi"
str2= re.findall('//([^a-z.]*)', str)
print(str2)


pattern = r"Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")

print(re.search(r'cake$', 'Eat cake').group())
print(re.search(r'Number: [0-5]', 'Number: 5').group())   

email_address = "Please contact us at: support@datacamp.com, xyz@datacamp.com"

addresses = re.findall(r'[\w\.-]+@[\w\.-]+', email_address)

for address in addresses:
    print("Email addresses is: " ,address)

   