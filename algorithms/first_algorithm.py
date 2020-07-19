def binary_search(list, item):
    low = 0
    high = len(list)

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        print(guess)
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 5))
