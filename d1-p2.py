#for loop
#range function
#1 to 100
#for in range 1 to 100
#print odd number between 1 to 100
#print even number between 1 to 100

for i in range (1,101):
    print(i)



#print(*no of objects,sep='',end='/n')
    
for i in range(1,101,2):
    print(i,end='')

    
#100 to 1


for i in range(99,0,-2):
    print(i,end='')
print()


#WAP using for loop iterating 1 to 100 but come out of loop at 50

for i in range(1,101):
    if i==50:
        break
    print(i,end='')
else:
    print("else statement")

#continue

for i in range (1,101):
    if i ==50:
        continue
    print(i,end=" ")
for i in range (1,101):
    if i ==50:
        pass
    print(i,end=" ")

