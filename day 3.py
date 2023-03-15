#previous questio11n
'''
n1=int (input ("enter a value n1") )
n2=int (input ("enter a value n2") )
result=[]
for i in range (n1,n2+1):
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result)
array=[i for i in range(n1,n2+1)]
print(array)
result=[]
for i in range(len(array)) :
    for j in range(i,len(array)):
        result.append(array[i:j+1])
print(result)
11==[array[i:j+1]for i in range(len(array))for j in range(i,len(array))]
print(result)
print(11)
c=0
for i in 11:
    if sum(i)%2!=0:
        c+=1
print(c)

'''
#DAY-3
#LIST comprihansion
#for loop version
'''
result=[]
for i in range(11):
    result.append(i)
print(result)

#list comprihansion version
print([i for i in range(11)])

#for loop version-->odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
print([i for i in range(11)if i%2!=0])

result=[]
for i in range(11):
        if i%2!=0:
         result.append(i)
        else:
         result.append(i**2)
print(result)
print([i if i%2!=0 else i**2 for i in range(11)])
            
'''
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

#for loop--odd-->square it
#even-->cube it
result=[]
for row in mat:
    row_data=[]
    for ele in row:
        if ele%2!=0:
            row_data.append(ele**2)
        else:
            row_data.append(ele**3)
    result.append(row_data)
print(result)

#list comprehansion
print([ele**2 if ele%2!=0 else ele*3 for row in mat for ele in row])
print([[ele**2 if ele%2!=0 else ele*3 for ele in row]for row in mat])






































