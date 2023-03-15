#functions
def function1():
    print("its a function")
function1()
def function2(num1,num2):
    print("num1=",num1,"num2=",num2)
    #print()__str__
function2(10,20)
def function3(num1,num2):
    num3=num1+num2
    return num3
function3(10,20)
print("value returned",function3(100,200))
