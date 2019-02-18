import math
from math import sin
import random

# methometical function
print(max(10,20,1889))
print(min(10,20,1889))
print(pow(10,10)) #The value of x**y.

print(math.exp(10))

print(round(-1.5))
print(abs(-12)) # return positive value

print ("abs(-45) : ", abs(-45))

# trigonmatric function like sin tan cose and more
print(sin(5))

# Random Number Functions
print(random.randrange(10,20,3)) # start value in include,stop value is exluded,3 one is even/odd
print(random.randrange(100,200,2)) # last parameter eaither even or odd in o/p

print(random.random()) #random() returns a random float r, such that 0 is less than or equal to r and r is less than 1.

#choice() returns a random item from a list, tuple, or string.

print(random.choice((23,'ganesh',34,1.6,98)))
print(random.choice([23,'ganesh',34,1.6,98]))

print(random.choice(("this is random string")))


#seed() sets the integer starting value used in generating random numbers. Call this function before calling any other random module function

random.seed(10)
print("Random number with seed 10 :", random.random())

# shuffle() randomizes the items of a list in place. this could be list or tuple


listn1 = [23,45,56,78,99,1000]
random.shuffle(listn1)
print("list1 random shuffle is: " , listn1)

# uniform() returns a random float r, such that x is less than or equal to r and r is less than y.

print(random.uniform(5, 20))




