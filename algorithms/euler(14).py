import time
def main():
    current_largest_chain = 0  # This holds the longest chain produced
    number_to_collatz_up_to = 1000000  # This holds the edge number we are gonna collatz up to
    x = 1
    number_that_produced_largest_chain = 0  # We store the information about the number that produced the longest chain
    while x < number_to_collatz_up_to:  # We are gonna iterate over x in this cycle up to 1000000
        current_chain = 1  # We make a  local variable 'current chain' which will hold the current chain
        current_number = x  # We make a local variable 'current_number' which will hold the info about our current number iterated
        while current_number != 1:
            current_number = checking_devision(current_number)  # We invoke the collatz method and equaling it to the current number, it cannot go lower than 1, as described in the while loop
            current_chain += 1 # Iterate current chain over and over after executing collatz method
        if current_chain > current_largest_chain: # Then we rewrite the current longest chain if the current chain is longer then the previous longest chain|
            current_largest_chain = current_chain
            number_that_produced_largest_chain = x# And saving the number to understand which number produced the current longest chain, simple as that:)
        current_chain=1
        x += 1
    print(number_that_produced_largest_chain, current_largest_chain)


def checking_devision(number): # Standard collatz method, nothing special
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    return number


main()
# print(checking_devision)
