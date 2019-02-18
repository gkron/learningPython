def demoexcp():
    try:
        a = 5/0
    except Exception:
        print("THIS IS ERROR MESSAGE")    
    else:
        print("###################")
    finally:
        print("i always wanted this message")        
        
      
def demo():
 try:
     a = int(input("Enter a positive integer: "))
     if a <= 0:
      raise ValueError("That is not a positive number!")
 except ValueError as ve:
    print(ve)
 else:
    print("user have entered postive number")    



#demoexcp()  
demo()