import pandas as pd
import numpy as np
from email.header import Header
import matplotlib as plot 

#create data
# raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
#         'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
#         'age': [42, 52, 36, 24, 73], 
#         'preTestScore': [4, 24, 31, ".", "."],
#         'postTestScore': ["25,000", "94,000", 57, 62, 70]}
# 
# df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
# 
# #print(df)
# 
# #saving data frame into csv
# df.to_csv('C:/Users/ganesh.kumar/eclipse-workspace/QaDemoLearning/example.csv')

#now Load a csv
# dt = pd.read_csv('C:/Users/ganesh.kumar/eclipse-workspace/QaDemoLearning/example.csv')
# print(dt.plot(kind="hist"))  
# print(dt.iloc[4,5]) #rows from position 4 onwards, and columns from position 5 onwards.
# print(dt.iloc[:,0]) #the first column, and all of the rows for the column.
# print(dt.iloc[:5,:]) #the first 5 rows, and all of the columns for those rows.
# print(dt.iloc[4,:])  # the 4th row, and all of the columns for that row.
# 
# reviews = dt.iloc[:,1:]  #remove the first column
# print(reviews.head())
# 
# print(reviews.loc[0:5,:])
# print(reviews.index)  # see index
# 
# some_reviews = dt.iloc[0:5,] # from1st to 05 row
# print(some_reviews.head())
# 
# print(some_reviews.loc[:,"age"]) # singel column and get data from age labels
# 
# print(some_reviews["first_name"]) # retrive column by passing column name
# 
# print(some_reviews[["first_name","age"]]) # multiple column

# # Load a csv with no headers
# dt1 = pd.read_csv('C:/Users/ganesh.kumar/eclipse-workspace/QaDemoLearning/example.csv', header=None)
# 
# print(dt1)

#Load a csv while specifying column names

# df = pd.read_csv('C:/Users/ganesh.kumar/eclipse-workspace/QaDemoLearning/example.csv', names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
# 
# print(df)

#Load a csv while setting the index columns to First Name and Last Name

# df = pd.read_csv('C:/Users/ganesh.kumar/eclipse-workspace/QaDemoLearning/example.csv', index_col=['First Name', 'Last Name'], names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
# print(df.tail(2))
# 
# df = pd.read_csv('C:/Users/ganesh.kumar/eclipse-workspace/QaDemoLearning/example.csv', index_col=['First Name', 'Last Name'], names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
# print(df)

#print(df.shape)

#Load a csv while specifying "."as missing values
# 
# df = pd.read_csv('C:/Users/ganesh.kumar/eclipse-workspace/QaDemoLearning/example.csv', na_values=['.'])
# print(pd.isnull(df))
# 
# #Load a csv while skipping the top 3 rows
# df = pd.read_csv('C:/Users/ganesh.kumar/eclipse-workspace/QaDemoLearning/example.csv', na_values='sentinels', skiprows=3)
# print(df)

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
print(ts.plot())

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,columns=['A', 'B', 'C', 'D'])
df = df.cumsum()

                  
