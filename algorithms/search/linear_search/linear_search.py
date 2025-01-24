def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print("Found at index", i)
            return i
    return -1

# ls = linear_search([1, 2, 3, 4, 5], 3)