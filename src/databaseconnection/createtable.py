import mysql.connector
from mysql.connector import Error

class table():
   
    def createtable(self):
       sql = """CREATE TABLE EMPLOYEE1 (FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT )"""
       con = mysql.connector.connect(host='127.0.0.1',
                             database='demoqa',
                             user='root'
                            )         
      
# Create table as per requirement
       cursor= con.cursor()    
       cursor.execute(sql)
# disconnect from server
       con.close()
        
t1 = table()
t1.createtable()       