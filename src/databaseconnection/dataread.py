import mysql.connector
import csv, itertools,sys
import pandas as pd
import compare
from symbol import comparison
from databaseconnection.ReadData import readData

class dataread:
    
    def readdata(self,sourceRow, targetRow):
      con = mysql.connector.connect(host='127.0.0.1',database='demoqa',user='root')
      con1 = mysql.connector.connect(host='127.0.0.1',database='demoqa',user='root')

      sql = "select * from employee"
      sql1= "select * from employee1"
      cursor = con.cursor()
      
      cursor1 = con1.cursor()
      cursor.execute(sql)
      cursor1.execute(sql1)
      result = cursor.fetchall()
      print(result)
      result1 = cursor1.fetchall()
      print(result1)
    def valid(self,result,result1):
      column_names = ['FIRST_NAME','LAST_NAME', 'AGE', 'SEX', 'INCOME']
      counter = 1
      row_length = min(len(result), len(result1))
      for i in range(row_length):
              if result[i] != result1[i]:
               print (i)
               yield (i) # UPDATED
               return 
      for source_row,target_row in itertools.zip_longest(result,result1):
          comparison_result = None
          for comparison_result in dataread.readdata(self, result, result1):
           print ("Mismatch in column %s on row number %d , source value %s, target value %s" % (column_names[comparison_result], counter, source_row[comparison_result], target_row[comparison_result]))
           counter += 1
      
#       df = pd.DataFrame(result)
#      # print(df)
#       df1 = pd.DataFrame(result1)
#     #  print(df1)
# 
#       df2 = pd.concat([df, df1])
#     #  print(df2.drop_duplicates(keep=False))  # removed duplicate data
#      
#       df2 = df2.reset_index(drop=True)
#     #  print(df2)
#         
#       df_gpby = df2.groupby(list(df2.columns))  #
# 
#       idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1] #get index of unique records
#         
#       print(df2.reindex(idx))
      
      #print(result)
#       for row in range(len(result)):
#         for row1 in range(len(result1)):
#               
#             if result[row] not in result1[row1]:
#                 print("row result is :", result[row])
#             else:
#                 print(result1[row])    
          #print(result[row])
#           for row1 in result1:
#               #if row1.contains(row):
#               if(row) not in row1:
#                   print(row,"matching")
#               else:
#                   print(row,"not matching")
    #print(row)
#        fname = row[0]
#        lastn = row[1]
#        age = row[2]
#        sex = row[3] 
#        incme = row[4]
#        print(fname, lastn, age, sex, incme )

read = dataread()
#read.readdata(result,result1)      