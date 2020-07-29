limit=4000000
num1=1
num2=2
s=0
while num2<=limit:
    if num2%2==0:
        s+=num2
    temp=num2+num1
    num1=num2
    num2=temp
print(s)


