def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        # print(i)  # We are printing the number of objects in the array (from 1 to 9)because we exclude 0(it would be 0-10)
        # print('-----------------------------------------------')
        # print(arr[i]) #We are going through the objects in the massive which correspond to their indexes
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = 1
    print(smallest_index)

    # print(smallest)


find_smallest([5, 3, 1, 6, 7, 8, 9, 6, 5, 5])

