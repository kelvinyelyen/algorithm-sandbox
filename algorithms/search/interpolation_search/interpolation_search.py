def interpolation_search(arr, x):
    """
    Interpolation Search implementation.
    The array must be sorted and uniformly distributed for best performance.
    """
    # Find indexs of two corners
    low = 0
    high = len(arr) - 1

    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        # Probing the position with keeping
        # uniform distribution in mind.
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))

        # Condition of target found
        if arr[pos] == x:
            print(f"Element found at index {pos}")
            return pos

        # If x is larger, x is in upper part
        if arr[pos] < x:
            low = pos + 1
        # If x is smaller, x is in the lower part
        else:
            high = pos - 1
            
    return -1

if __name__ == "__main__":
    # Array of items on which search will be conducted
    # Note: Interpolation search works best on uniformly distributed sorted arrays
    data = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    x = 18 
    
    print(f"Array: {data}")
    print(f"Searching for: {x}")
    
    index = interpolation_search(data, x)

    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")
