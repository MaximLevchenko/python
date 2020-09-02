from math import *


def main():
    sum = 1000
    for c in range(sum):
        for b in range(500):
            for a in range(b):
                if a + b + c == sum:
                    if isTriplet(a, b, c):
                        print(a, b, c)
                        print(a * b * c)


def isTriplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False


main()