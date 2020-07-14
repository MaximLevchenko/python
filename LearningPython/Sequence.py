shoplist = ['apples', 'mangoes', 'carrots', 'bananas']
name = 'swaroop'
# Операция индексирования
print('Element 0 -', shoplist[0])
print('Element 1 -', shoplist[1])
print('Element 2 -', shoplist[2])
print('Element 3 -', shoplist[3])
print('Element -1 -', shoplist[-1])
print('Element -2 -', shoplist[-2])
print('Symbol 0 -', name[0])
# Вырезка из списка
print('Elements from 1 to 3:', shoplist[1:3])
print('Elements from 2 to the end', shoplist[2:])
print('Elements from 1 to -1:', shoplist[1:-1])
print('Elements from beginning to the end:', shoplist[:])
# Вырезка из строки
print('Symbols from 1 to 3:', name[1:3])
print('Symbols from 2 to the end:', name[2:])
print('Symbols from 1 to -1:', name[1:-1])
print('Symbols from beginning to the end:', name[:])

print(shoplist[::1])
print(shoplist[::2])
print(shoplist[::3])
print(shoplist[::-1])
