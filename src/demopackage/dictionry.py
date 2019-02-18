dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# 
# print(dict.keys())
# print(dict.values())
# print(dict['Name'])
# print(len(dict))

#dict = {'Name': 'Zara', 'Age': 7};
# print ("Equivalent String : %s" % str (dict))
# 
# #  copy() returns a shallow copy of the dictionary.
# dict2 = dict.copy()
# print(dict2)
# 
# #get() returns a value for the given key.
# print(dict2.get('Age'))

#create new dictionary with empty value
# dict3 = dict.fromkeys(dict2)
# print(dict3)

#print(dict)

for key , value in dict.items():
    if value==7:
        print("this is value")
        break
    else:  
        print(value)

for value in dict.items():
    print()
