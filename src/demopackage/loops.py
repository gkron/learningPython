# count = 0
# while(count<=9):
#     print('The count is:', count)
#     count = count+1
# 
# # revers order
# count = 9
# while(count>0):
#     print('The count is:', count)
#     count = count-1
# #infinit loo[
# var = 1
# while var == 1 :  # This constructs an infinite loop
#    num = input("Enter a number  :")
#    print ("You entered: ", num)
from _ast import Num

# count = 10
# while count<5:
#     print(count, "is less then 5")
#     count = count+1
# else:
#     print(count,"is not less then 5")  
# 
# # single statement with while loop
# flag = 1
# while(flag): print(flag," value is  true")   
# print("good bye")



#############################################

# for letter in 'python':
#     print('current letter is '+letter)
#     print("**********************************")
#     print('current letter is ', letter)


# fruitlist = ['bannan','apple','lammon','mango','watermelon']
# print(len(fruitlist))
# print(fruitlist[0])
# #print(fruitlist)
# # for value in fruitlist:
# #     print(value)
# for index in range(len(fruitlist)):
#     print('current fruit is', fruitlist[index])    
#     


for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print ('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print (num, 'is a prime number')
      
      
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print( i, " is prime")
   i = i + 1      


# break statement
# var = 10                    # Second Example
# while var > 0:              
#    print ('Current variable value :', var)
#    var = var -1
#    if var == 5:
#       break
#   
  
# continue statement
var = 10                    # Second Example
while var > 0:              
    var = var -1
    if var == 5:
        continue
    print ('Current variable value :', var)
    
    
    

