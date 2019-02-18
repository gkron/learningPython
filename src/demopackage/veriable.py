#local and global variable
#import demopackage.function
#from demopackage.function import*   # get all the function
from demopackage.function import hlo  # get sepecifc method

gl = 100  # global variable

def demo4(value):
    print("value is: " , value)
    print(gl)
    

print(gl)


hlo()

