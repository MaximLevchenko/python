from selenium import webdriver
app = True

while app:  # Infinite loop to check the input
    s = input('Enter your text')
    if s == ('Exit'):
        break # We tell our programm that we shpuld exit it, after this you will exit the whole while loop
    elif len(s)<3:
        print('Too small')
        continue

    print(len(s), '- This is the quantity of symbols in your word')
print('You have exited the program')


