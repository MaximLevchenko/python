limit=4000000
num1=0
num2=1
s=0
while num2<=limit:
    if num2%2==0:
        s+=num2
    num1,num2=num2,num1+num2
print(s)

'''Secpnd Variant is below(more efficient)'''
def main():
    fib_seq=[0,1]
    while True:
        fib=fib_seq[-1]+fib_seq[-2]
        fib_seq.append(fib)
        if fib>4000000:
            break

    print(fib_seq)
main()

