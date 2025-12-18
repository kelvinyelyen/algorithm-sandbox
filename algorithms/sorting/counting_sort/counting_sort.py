def counting_sort(arr):
    """
    Counting Sort implementation.
    Suitable for sorting integers within a specific range.
    """
    if not arr:
        return arr

    # Find the maximum element to determine the range
    max_val = max(arr)
    # Check for negative numbers (Counting Sort typically needs non-negative integers)
    min_val = min(arr)
    if min_val < 0:
        print("Note: This simple Counting Sort implementation expects non-negative integers.")
        # Shift values to handle negative numbers if needed, or raise error. 
        # For simplicity, we'll shift if min_val < 0
        shift = -min_val
        print(f"Shifting all values by {shift} to handle negative numbers.")
        arr = [x + shift for x in arr]
        max_val += shift
    else:
        shift = 0

    # Initialize count array
    count = [0] * (max_val + 1)

    # Store count of each character
    for num in arr:
        count[num] += 1

    # Store cumulative count
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # Output array
    output = [0] * len(arr)
    
    # Build the output array
    # Iterate in reverse order to ensure stability
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # Initial array shifted back if necessary
    if shift > 0:
        return [x - shift for x in output]
    return output

if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print(f"Original: {data}")
    sorted_data = counting_sort(data)
    print(f"Sorted:   {sorted_data}")
    
    # Test with negative numbers
    data_neg = [-5, -10, 0, -3, 8, 5, -1, 10]
    print(f"Original (Mixed): {data_neg}")
    sorted_data_neg = counting_sort(data_neg)
    print(f"Sorted (Mixed):   {sorted_data_neg}")
