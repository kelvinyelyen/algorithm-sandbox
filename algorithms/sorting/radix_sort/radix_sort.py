def counting_sort_for_radix(arr, exp):
    """
    A modified counting sort function to sort arr[] according to
    the digit represented by exp.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10 

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    # Iterate reverse to maintain stability
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    # Copy the output array to arr[], so that arr now
    # contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Radix Sort implementation.
    """
    if not arr:
        return arr

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr

if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Original: {data}")
    radix_sort(data)
    print(f"Sorted:   {data}")
