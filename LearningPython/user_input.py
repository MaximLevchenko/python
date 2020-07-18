def reverse(text):
    return text[::-1]  # Text in the opposite order. For example 'nice' will be 'ecin'


def is_palindrome(text):
    return text == reverse(text)


forbidden = ('.', '?', '!', ':', ';', '-', '(', ')', '[', ']', '"', ',')
something = input("Enter your text: ")
something.lower()

for i in range(len(something)):
    for x in forbidden:
        if something[i] == x:
            something = something.replace(x, ' ')
list = something.split()  # разбивка на части по символам пробела
# print(list)
s = ""
for x in list:
    s += x
if (is_palindrome(something)):
    print("Yeah")

else:
    print('Not')

captains = ['Janeway', 'Picard', 'Sisko']

for i in range(len(captains)):
    print(captains[i])
    #TODO undertand this part of code
