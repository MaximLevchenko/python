def reverse(name, surname):
    name_username = (name[::-1] + ' ' + surname[::-1])
    print(name_username)


name_input = input('Enter your name pls ').lower()
surname_inpnut = input('Enter your surname pls ').lower()
reverse(name_input, surname_inpnut)
