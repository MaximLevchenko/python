def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


delims = ('.', '?', '!', ':', ';', '-', '(', ')', '[', ']', '"', ',')
something = input('Введите текст: ')
something = something.lower()  # перевод в нижний регистр
for i in range(len(something)):
    for x in delims:
        if something[i] == x:
            something = something.replace(x, ' ')  # замена разделителя на пробел
            print(something)
list = something.split()  # разбивка на части по символам пробела
print(list)
s = ""
for x2 in list:
    s += x2  # конкатенация частей в слово без разделителей
    print(s)
if (is_palindrome(s)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
