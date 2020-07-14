number = 23;
running = True
while running: #making infinite loop
    guess = int(input('Write down your number'))
    if guess == number:
        print("you got it")
        running = False #if this block is entered, the loop will be over
    elif guess > number:
        print("this is slightly bigger")
    else:
        print("this is slightly lower")
else:
    print("The end")
