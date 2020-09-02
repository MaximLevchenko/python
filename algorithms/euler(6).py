l = []
l1 = []


def suma_kvadratov():
    for i in range(1, 101):
        sqrt = i ** 2
        l.append(sqrt)


suma_kvadratov()

sumofthefirstlist = sum(l)
print(sumofthefirstlist)


def kvadrat_summy():
    for x in range(1, 101):
        l1.append(x)


kvadrat_summy()

sqrtofthesum = sum(l1) *sum(l1)

print(sqrtofthesum)

print("The difference between these two numbers is:", end=' ')


def difference(number1, number2):
    if number2 > number1:
        print(number2 - number1)
    else:
        print(number1 - number2)


difference(sumofthefirstlist, sqrtofthesum)
