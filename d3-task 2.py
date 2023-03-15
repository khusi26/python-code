input_string = input("Enter comma separated numbers: ")
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
print("Output:", output)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````++++++











































                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
