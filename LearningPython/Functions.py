#!/usr/bin/env python

import os
import sys
from math import *


def printMax(a, b):
    if a > b:
        print(a, "Maximum")
    elif a == b:
        print(a, "Equals", b)
    else:
        print(b, "Maximum")


printMax(7, 89)
x = 8
u = 56
printMax(x, u)

print('-------------------------------------------------------------')

x = 50


def func():
    global x  # We change the value of x in the main block of the programm by using identificator 'global
    print("x equals", x)
    x = 2
    print("Change x value on", x)


func()
print(x)

print('-------------------------------------------------------------')


def funcOuter():
    x = 2
    print('value of x is:', x)

    def funcInner():
        nonlocal x  # We say that the value of x will be changed only in the inside of the inner function
        x = 5

    funcInner()
    print('Local x is:', x)


funcOuter()
print(x)

print('-------------------------------------------------------------')


def say(message, times=1):
    print(message * times)


say('Hi', 5)
say('Hello', 3)

print('-------------------------------------------------------------')


def keyWord(a, b, c=100):
    print(a, b, c)


keyWord(20, 5, 20)
keyWord(1, 5, )

print('-------------------------------------------------------------')


def getUser(name, age, isMarried):
    print(name, age, isMarried)
    return name, age, isMarried


Max = getUser('Max', 22, True)

print('-------------------------------------------------------------')


def total(a=5, *numbers, **phonebook):
    print(a)

    for i in numbers:
        print(i)
    for r, t in phonebook.items():
        print(r, t)


print(total(10, 1, 2, 3, 4, 5, 'jack', 'jack2', jack=200))

print('-------------------------------------------------------------')


def total(initial=5, *numbers: int, extra_number):
    count = initial
    for number in numbers:
        count += number

    count += extra_number
    print(count)


total(10, 1, 2, 6, extra_number=50)

print('-------------------------------------------------------------')


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y


print(maximum(2, 3))

print('-------------------------------------------------------------')


def printMax(x, y):
    ''' Outputs max value of 2 numbers.

     Both values should be integers '''

    x = int(x)  # конвертируем в целые, если возможно
    y = int(y)
    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')


printMax(3, 5)
print(printMax.__doc__)

print('-------------------------------------------------------------')


class A:  # Для Python 2 - A(object)
    """Описание класса."""


def func():
    """Описание функции."""


# Для класса.
A.__doc__  # 'Описание класса.'

# Для объекта.
a = A()
a.__doc__  # 'Описание класса.'

# Для функции.

func.__doc__  # 'Описание функции.'

# Для модуля.
print(a.__doc__)  # OS routines for NT or Posix depending on what system ...

print('-------------------------------------------------------------')

n = int(input("Введите диапазон:- "))
p = [2, 3]
count = 2
a = 5

while (count < n):
    b = 0
    for i in range(2, a):
        if (i <= sqrt(a)):
            if (a % i == 0):
                print(a, "непростое")
                b = 1
            else:
                pass
    if (b != 1):
        print(a, "простое")
        p = p + [a]
    count = count + 1
    a = a + 2
print(p)

print('-------------------------------------------------------------')

print('Script 1. My name is: %s' % __name__)
print('This is simple code from script 1')


def func():
    print('This is code from function from script 1')


if __name__ == "__main__":
    func()



print('Script2. My name is: %s' % __name__)
print('Importing ifname1')



