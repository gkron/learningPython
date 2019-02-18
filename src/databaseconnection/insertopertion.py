import mysql.connector

class insert:
    
    def insertData(self):
        con  = mysql.connector.connect(host='127.0.0.1',database='demoqa',user='root')      
       # sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        sql1 = "INSERT INTO employee1(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       ('RID', 'SINGH', 18, 'M', 30000)


        cursor = con.cursor()   
  
        cursor.execute(sql1)
         
        con.commit()
         
         
insert = insert()
insert.insertData()
        