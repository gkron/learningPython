class employe:
    empcount = 10
    
    def __init__(self,name,value):
        self.name = name
        self.value= value
        print("name is: ", name)
        print("value is: ",value)
        employe.empcount += 1
        
        
    def test1(self):
        print("hello word")
        

            
def empcount1(self):
            print("total emp is" , employe.empcount)    
        
emp1 = employe("ganesh",32)
emp2 = employe("sarb",32)

#emp1.test1()
#emp2.test1()
emp1.empcount1()

emp1.age =7
emp1.age =8

print(getattr(emp1, 'age'))
print(hasattr(emp1,'name'))
