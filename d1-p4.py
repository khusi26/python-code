#print()__str__
def function(num1,num2):
    num=float(num1)+num2
    return num
print("value returned",function('10',10.2))

#categories of functions
#based on argument
#1:positional argumemts

def functions(num1,num2,num3,num4):
    print(num1,num2,num3,num4)
functions(100,"500",20,500)
#can't tale lesser og greater values

#keyword arguments

def function2(num1,num2,num3,num4):
    print(num1,num2,num3,num4)
function2(num4=40,num2=1,num3=33,num1=20)

#default arguments
def function3(name,rollno,branch,collegename="GIETU"):
    print(name,rollno,branch,collegename)
function3("khusi",12,"cse")
function3("lopa",11,"cst")
function3("ashu",10,"eee")
function3("hira",13,"ee")


#variable no of arguments
def function4(*var):#tuple=
    for i in var:
        print(i,end=' ')
function4(10,20)
print()
function4(10,20,30,40)
print()
unction4(10,20,30,40,50,60)
    

def add(*var):#tuple=
    sum1=0
    for i in var:#10,20
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40,50,60))




                                
