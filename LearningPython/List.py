shopList = ['apples', 'oranges', 'watermelon', 'sausages']

print('I should buy', len(shopList), "groceries")

print("Groceries", end=': ')

# 'end' function is used to make
# strings together in one line(it means now they will not be
# transferred to another line)


for i in shopList:
    print(i, end=', ')
print('\n') # \n is used to transfer the str text to the next line

print('\nMore than that, i should buy some rice')

print('\n')

shopList.append('rice')

print('Now my groceries list is:', end=' ')

for i in shopList:
    print(i, end=', ')

print('\n')

print('Hmm, my groceries list is kinda messy, let me sort it')

shopList.sort()

print('\n')

print('Now my sorted groceries list is:', end=' ')

for i in shopList:
    print(i, end=', ')

print('\n')
oldItem = shopList[0]
print("I have already bought the first product, this is :", oldItem, ". Now i can delete it from my list")

print('\n')

del shopList[0]
print("So now my list is:", end=" ")
for i in shopList:
    print(i, end=', ')
