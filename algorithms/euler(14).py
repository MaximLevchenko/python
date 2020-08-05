start_number = 1
current_number_of_steps = 0

def main():

    pass

def checking_devision(number):
    list_of_numbers = [number]
    current_number_of_steps = 0

    while number >= 1:
        if number % 2 == 0:
            number = number / 2
            list_of_numbers.append(number)
            current_number_of_steps+=1

        else:
            number = number * 3 + 1
            list_of_numbers.append(number)
            current_number_of_steps+=1

        if number==1:
            break
    print(list_of_numbers)
    print(current_number_of_steps)
    return list_of_numbers



checking_devision(13)