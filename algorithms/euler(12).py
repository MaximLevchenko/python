import math
from math import *
def main():
    target_number_of_divisors = 500
    current_most_divisors = 0
    triangle_number = 1
    index = 2

    while True:
        current_divisors = find_divisors(triangle_number)
        number_of_current_divisors = len(current_divisors)
        if number_of_current_divisors > current_most_divisors:
            current_most_divisors = number_of_current_divisors
            print(triangle_number,end=' ')
            print(current_most_divisors)
        if current_most_divisors > target_number_of_divisors:
            print(triangle_number)
            break
        triangle_number, index = next_triangle_number(triangle_number, index)


def next_triangle_number(number, index):
    return number + index, index + 1


#def find_divisors(number):
#    potential_divisor = 1
#    list_of_divisors = []
#    while potential_divisor <= number:
#        if number % potential_divisor == 0:                INEFFICIENT WAY--> Takes too long but posiible
#            list_of_divisors.append(potential_divisor)
#        potential_divisor += 1
#    return list_of_divisors
def find_divisors(number):
    potential_divisor = 1
    half_list_of_divisors = []
    list_of_divisors=half_list_of_divisors
    sqrt=number**0.5
    sqrt=math.ceil(sqrt)
    while potential_divisor < sqrt:
        if number % potential_divisor == 0:
            half_list_of_divisors.append(potential_divisor)
        potential_divisor += 1

    for divisor in half_list_of_divisors[::-1]:
        list_of_divisors.append(number/divisor)
    return list_of_divisors

main()

