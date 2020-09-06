import time
import math

def main():
    current_longest_chain = 0
    number_that_produced_chain = 0
    x = 1
    number_to_collatz_up_to = 1000000
    while x < number_to_collatz_up_to:
        current_number = x
        current_chain = 1
        while current_number != 1:
            current_number = collatz(current_number)
            current_chain += 1

        if current_chain > current_longest_chain:
            current_longest_chain = current_chain
            number_that_produced_chain = x
            print(number_that_produced_chain, current_longest_chain)

        current_chain = 1
        x += 1
    print(number_that_produced_chain, current_longest_chain)


def collatz(number):
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    # print(number)
    return number

main()
