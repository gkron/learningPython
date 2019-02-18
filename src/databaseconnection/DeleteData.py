import mysql.connector

class DeleteData:
    
    def deletedata(self):
        con = mysql.connector.connect(host='127.0.0.1',database='demoqa',user='root')
        sql = "DELETE FROM EMPLOYEE WHERE AGE=25"
        cursor= con.cursor()
        try:
            cursor.execute(sql)
            con.commit()
        except:
            con.rollback()
            print("unable to complete the tracnsaction")
            
dd = DeleteData()
dd.deletedata()                