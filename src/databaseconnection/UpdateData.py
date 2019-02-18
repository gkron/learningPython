import mysql.connector

class UpdateData:
    
    def updatedata(self):
        con = mysql.connector.connect(host='127.0.0.1',database='demoqa',user='root')
        sql = "UPDATE EMPLOYEE SET AGE= AGE+1"
        cursor= con.cursor()
        try:
            cursor.execute(sql)
            con.commit()
        except:
            con.rollback()
            
ud = UpdateData()
ud.updatedata()            