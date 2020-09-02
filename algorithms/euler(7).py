def main():
    numbers_prime_to_find = 100
    x = 2
    list_of_primes = []
    while (len(list_of_primes) < numbers_prime_to_find):

        if all(x % prime != 0 for prime in list_of_primes):  # for prime in list_of_primes:

            list_of_primes.append(x)  # if x%prime
        x += 1
    print(list_of_primes)
    print(list_of_primes[-1])


main()


