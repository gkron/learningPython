print("happy learning big data")

x = 10
y =20
z= x+y
#print(z)


a = "this is one "
b = "this is two"
c = a+b
#print(c)

if 5 > 2:
    print("Five is greater than two!") 
    
"""This is a multiline docstring."""
print("Hello, World!") 

total = 'item1' +\
        'item2' +\
        'item3'
print(total)              

days = ['monday','tuesday','wednesday',
        'thuresday','friday']

print(days)



word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""

print(word)
print(sentence)
print(paragraph)

inputname= input("\n\nPress the enter key to exit.")


try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   