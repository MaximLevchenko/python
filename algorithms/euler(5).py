def isDividableBy1to20(number):
    for i in range(1,21):
        if number%i!=0:
            return False
    return True

number=20

while True:
    if isDividableBy1to20(number):
        break
    number+=20

print(number)
