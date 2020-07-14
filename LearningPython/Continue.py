while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    elif len(s) < 3:
        print('Слишком мало')
        continue
    else:
       print ('Введённая строка достаточной длины')
# Разные другие действия здесь...
