#q6 
# Input
'''
marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)

# Function 1
def find_more_than_average():
    average = sum(marks)/len(marks)
    count = 0
    for mark in marks:
        if mark > average:
            count += 1
    return (count/len(marks))*100

# Function 2
def generate_frequency():
    freq = [0]*26
    for mark in marks:
        freq[mark] += 1
    return freq

# Function 3
def sort_marks():
    return sorted(marks)

# Output
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
'''
#q7
'''
bilingual_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
def translate(bilingual_dict, english_words):
    swedish_words = []
    for word in english_words:
        swedish_word = bilingual_dict.get(word)
        if swedish_word:
            swedish_words.append(swedish_word)
    return swedish_words
english_wishes = ["merry", "christmas", "and", "happy", "new", "year"]
swedish_wishes = translate(bilingual_dict, english_wishes)
print(swedish_wishes)
'''

##
'''
def tranlate(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict[i])
    return list2
dict1={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
list1=["merry", "christmas", "and", "happy", "new", "year"]
print(list2)
'''

#q8(imp)1

'''
def count_odd_subarrays(arr):
    n = len(arr)
    ans = 0
    for i in range(n):
        odd_count = 0
        for j in range(i, n):
            if arr[j] % 2 == 1:
                odd_count += 1
            if odd_count % 2 == 1:
                ans += 1
    return ans
arr = [1, 2, 3]
print(count_odd_subarrays(arr))
'''
##

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
result=[array[i:j+1]for i in range(len(array))for j in range(i,len(array))]
print(result)

    
    


























