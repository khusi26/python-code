'''n1=int(input())
n2=int(input())
n3=int(input())
if n1==7:
    print(n2*n3)
elif n2==7:
    print(n3)
elif (n3==7):
    print(-1)
else:
    print(n1*n2*n3)

'''

#task-2
'''
def currencycal(AmountINR,curr):
    if curr=="Euro":
        print(AmountINR*0.01417)
    elif curr=="British pound":
        print(AmountINR*0.0100)
    elif curr=="Australian dollar":
        print(AmountINR*0.02140)
    else:
        print("-1")
currencycal(300,"Euro")
currencycal(300,"British pound")
currencycal(300,"Australian dollar")
'''

#task-3
'''
n_adults=int(input("Enter the number of adults"))
n_childs=int(input("Enter the number of child"))
total=((n_adults*37550.0) + (n_childs*37550.0/3))
print(total)
totall=total*0.07
total2=total+totall
print ("with ur service tax", total2)
total_amount=total2*0.90
print(total_amount)

'''

#task-4

def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    five = int(rupees_to_make/5)
    one_needed = rupees_to_make%5
    five_needed = five if five <= no_of_five else no_of_five
    if (five > no_of_five):
        one_needed = rupees_to_make - 5 * no_of_five     
    
    (print("No. of Five needed : {}\nNo. of One needed  : {}".format(five_needed,one_needed))) if one_needed <= no_of_one else (print(-1))

make_amount(28,8,5)

































