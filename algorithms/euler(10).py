l=[]
for n in range(2, 2000000):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        # loop fell through without finding a factor
            l.append(n)




print(sum(l))






