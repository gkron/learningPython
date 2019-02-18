import mysql.connector
import csv, itertools,sys
sys.stdout=open("mismatch.txt","w")
import pandas as pd
import compare
from symbol import comparison

class readData:
    
    
   def getColumnHeaders(self):
        con = mysql.connector.connect(host='127.0.0.1',database='demoqa',user='root')
        con1 = mysql.connector.connect(host='127.0.0.1',database='demoqa',user='root')
        sql = "select * from employee"
        sql1= "select * from employee1"
        cursor = con.cursor()
      
        cursor1 = con1.cursor()
        cursor.execute(sql)
        column_names = [i[0] for i in cursor.description]
        print(column_names)
        
        
   def readdata(self):
      con = mysql.connector.connect(host='127.0.0.1',database='demoqa',user='root')
      con1 = mysql.connector.connect(host='127.0.0.1',database='demoqa',user='root')

      sql = "select * from employee"
      sql1= "select * from employee1"
      cursor = con.cursor()
      
      cursor1 = con1.cursor()
      cursor.execute(sql)
      cursor1.execute(sql1)
      result = cursor.fetchall()
 
     # print(result)
      result1 = cursor1.fetchall()
    #  print(result1)
      
      df = pd.DataFrame(result)
     # print(df)
      df1 = pd.DataFrame(result1)
    #  print(df1)

      df2 = pd.concat([df, df1])
    #  print(df2.drop_duplicates(keep=False))  # removed duplicate data
     
      df2 = df2.reset_index(drop=True)
    #  print(df2)
        
      df_gpby = df2.groupby(list(df2.columns))  #

      idx = [x[0] for x in df_gpby.groups.values() if len(x) == 1] #get index of unique records
        
      print(df2.reindex(idx))
      
        
      
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

read = readData()
read.readdata()
#read.getColumnHeaders()    

