#list-->ordered--default index
#
'''
list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print(list2,type(list2))
list3=[10,10.2,30+3j,True,"python"]
print(list3,type(list3))
list4=[101,201,301,401]
print(list4,type(list4))
list4.extend([101,202,301,401])
print(list4,type(list4))
list4.remove(401)
print(list4,type(list4))
list4.pop()
print(list4,type(list4))
del list4[1]
print(list4,type(list4))

'''
#q1
'''
def function(str1):
    l_count=0
    d_count=0
    for i in str1:
        if i.isalpha():
            l_count=l_count+1
        elif i.isdigit():
            d_count=d_count+1
        else:
            continue
    return [l_count,d_count]
print(function("Infosys 123"))
print(function("ABCEFG"))
'''
#q2
'''
def find_pairs_of_numbers(num_list,n):
    count=0
    for x in num_list:
        index=num_list.index(x)+1 
        for y in range(index,len(num_list)):
            if x+num_list[y]==n:
                count+=1
        return count
num_list=[1,2,7,4,5,6,0,3]
n=6
print(find_pairs_of_numbers(num_list,n))
'''
#q3
'''
def function(string):
    if len(string) < 2:
        return -1
    else:
        return string[0:2] + string[-2:]
    
print(function("w3resource")) 
print(function("W3"))
print(function("A"))
'''
#q4
'''
def add_string(string):
    if len(string) < 3:
        return string
    elif string[-3:] == 'ing':
        return string + 'ly'
    else:
        return string + 'ing'
print(add_string('sleep'))     
print(add_string('amazing'))
print(add_string('is'))        
    
'''
#q5
'''
def check_double(number):
    num1=str(number*2)
    number=str(number)
    count=0
    for x in number:
        if x in num1:
            count+=1
        else:
            return False 
    if count==len(number):
        return True
print(check_double (245))
print(check_double(125874))

'''


