import smtplib

from Tools.demo.mcast import sender
from smtplib import SMTPException

class SMPTP:
    
    def sendEmail(self):
        sender = 'from@ganesh.kumar@impetus.co.in'
        receivers = ['to@ganesh.kumar@impetus.co.in']
        messsage= "Hello this is test mail using python api"
        try:
            #IMPETUS-N472.impetus.co.in
            smtpobj = smtplib.SMTP('192.168.56.1')
            smtpobj.sendmail(sender,receivers, messsage)
            print("Successfully sent the mail to mr kumar")
        except SMTPException:
            print("this is exception")
  
mp= SMPTP()
mp.sendEmail()

                