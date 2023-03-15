'''input_string1,2, =input("Enter comma separated numbers: ")
input_list = input_string.split(",")
num1_sum = 0
num2 = " "
between_5_and_8 = False
for num in input_list:
    if num == "5":
        between_5_and_8 = True
    elif num == "8":
        between_5_and_8 = False
    elif not between_5_and_8:
        num1_sum += int(num)
    elif between_5_and_8:
        num2 += num
num2 = int(num2)
output = num1_sum + num2
print("Output:",output)
'''
#program
'''
array=list(map(int,input().split(",")))
number1=sum(array [:array.index(5)])+sum(array[array.index(8)+1:])
l=array[array.index(5):array.index(8)+1]
number2=""
for i in l:
        number2=number2+str(i)
print(int(number2)+number1)
'''
#task-4
'''
s=input().split(",")
stt=[]
num=[]
for i in s:
    s1,n=i.split(":")
    num.append(n)
    stt.append(n)
def rotate(ss,n):
    n=str(n)
    s=0
    for i in n:
        s+=int(i)**2
    if s%2==0:
        return ss[-1]+ss[:-1]
    else:
        return ss[2:]+ss[:2]
for i in range(len(num)):
    print(rotate(stt[i],num[i]))
'''
#task-5
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
def largest_prime_factor(num):
    i = 2
    while i <= num/i:
        if num % i == 0:
            num = num // i
        else:
            i += 1
    return num
def sum_of_largest_prime_factors(n):
   
    total = 0
    for i in range(n, n+9):
        total += largest_prime_factor(i)if is_prime(largest_prime_factor(i)) else 0
    return total
print(sum_of_largest_prime_factors(10))































    
