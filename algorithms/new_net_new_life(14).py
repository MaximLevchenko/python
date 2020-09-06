def main():
    number_produced_chain = 0
    the_max_num_to_collatz = 1000000
    longest_chain = 0
    num = 1
    while num < the_max_num_to_collatz:
        current_chain = 1
        current_num = num
        while current_num != 1:
            current_num = collatz(current_num)
            current_chain += 1
        if current_chain > longest_chain:
            longest_chain = current_chain
            number_produced_chain = num
        num += 1
        current_chain = 1

    print(longest_chain, number_produced_chain)


def collatz(number):
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    return number


main()
