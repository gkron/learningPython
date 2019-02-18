from com.inheritnce.Parent import Parent

class Child(Parent):
    
    def mytest(self):
        print("hello child")
    

    def test3(self):
        print("calling child method") 
         

r = Child() # instance of child
pr = Parent() # instance of parent

r.test3()  # calling child method method overriding

pr.test3()  # calling parent method

r.mytest()
r.test() # method from parent
r.test2("ganesh")