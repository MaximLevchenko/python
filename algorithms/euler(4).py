x = 999
y = 999
z = []
z1 = 0
while y > 100:
    c = x * y
    if str(c) == str(c)[::-1] and c > z1:  # We check whether the number is palindrome or not
        z1 = c
        z.clear()
        z.append([x, y])  # Then if it is we append the value to the list
    else:
        x -= 1  # If is is not a palindrome--> We decrement x up to 100
        if x == 100:  # When x is 100 we enter this block of code
            y -= 1  # Decrementing y by 1
            x = 999  # And making the x value again 999. Then we start the while code again with value x=999 and y =999, the process starts again until we find the palindrome

print(z, z1)
