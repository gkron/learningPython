class B:
    
    COMP='IMPETUS'
    
    def d3(self):
            print("meeeeee@@@@@@@@@@@")
            return
    
    def d4(self,count):
        #count =10
        while count>0:
            print("count value is: ", count)
            if count<5:
                break
            else:
                print("value is ")
            count -=1
            
    
    
    
n2 = B()
print(n2.COMP)   
n2.d3()
n2.d4(12)        