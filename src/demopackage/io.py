#print("Python is really a great language,", "isn't it?")

#str = input("please enter your name: ")

#print("Entered name is: ", str)
#open


f1 = open("D:/testdata.txt")
for line in f1:
       words = line.split()
       print(words) # ['HELLO', 'qa', 'testing', 'big', 'data', 'world', 'for', 'hive', 'and', 'hbase']
       
       
# with for loop read the file
with open("D:/testdata.txt") as ronfile:
    for line in f1:
        print(line)
    
    
print(f1.read())  # read entire file
print(f1.tell())  # get count
f1.seek(0)  # from where want to read line
print(f1.readline()) # read line by line
 
f2 = open("D:/testdata.txt")
print(f2.read(5))  # read first 5 char

# how to write in file
# 
# f5 = open("D:/demotest.txt","w")
# f5.write("add some new data")
# f5.close
f6 = open("D:/demotest.txt")

print(f6.read())





