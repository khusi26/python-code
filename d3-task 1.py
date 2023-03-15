#D3-task 1
'''mylist = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]

result = []

for num in list_b:
    if num in mylist:
        index = mylist.index(num)
        result.append((num, index))

print(result)
print([(num,mylist.index(num))for num in list_b])'''

''' list comprehansion

mylist = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]
result = []
print([(num,mylist.index(num))for num in list_b])
'''
#dictionary
'''
mylist = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]

result = []

for num in list_b:
    if num in mylist:
        index = mylist.index(num)
        result.append((num, index))
        
print(result)
print([(num,mylist.index(num))for i in list_b])
result={}
for num in list_b:
    result[num]=mylist.index(num)
print(result)
print({num:mylist.index(num)for num in list_b})
'''
#task-3
"""
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
"""
sentences = ["a new world record was set", "in the holy city of ayodhya", "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']
result=[]
for sentences in sentences:
    row_data= []
    for word in sentences.split():
        if word not in stopwords:
            row_data.append(word)
    result.append(row_data)
print(result)
'''
print([[word for word in sentence.split()if word not in spotword]for
      sentence in sentences])
'''












'''
tokenized_sentences = []
for sentence in sentences:
    tokens = word_tokenize(sentence.lower())
    filtered_tokens = [token for token in tokens if token not in stopwords]
    tokenized_sentences.append(filtered_tokens)
print(tokenized_sentences)
'''






































































