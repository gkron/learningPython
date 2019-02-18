class mydemo:
    
    value = 10
    
    
    def test1(self,val1):
        print("this is me")
        print("test value is: ", val1)
        
    def test2(self):
        print("hello word")
        
print(mydemo.value)     # class can directly call class veriable
t1 = mydemo()  
t1.test1(12)
print(t1.value)     



