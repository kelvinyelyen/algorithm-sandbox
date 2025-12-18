def bucket_sort(arr):
    """
    Bucket Sort implementation.
    Ideally checks that input is uniformly distributed over a range (0, 1).
    Here adapted to work with general float/int inputs by normalizing.
    """
    if not arr:
        return arr

    # Create empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    
    # Range of values
    max_val = max(arr)
    min_val = min(arr)
    rng = max_val - min_val
    
    if rng == 0:
        return arr

    # Put array elements in different buckets
    for num in arr:
        # Normalize to 0..1 range roughly, then scale to 0..num_buckets
        # For simple floats 0..1, index = int(num * num_buckets)
        # Generalized:
        idx = int(((num - min_val) / rng) * (num_buckets - 1))
        buckets[idx].append(num)

    # Sort individual buckets
    for i in range(num_buckets):
        buckets[i].sort() # Using standard sort (often Timsort) for individual buckets

    # Concatenate all buckets into arr[]
    k = 0
    for i in range(num_buckets):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    return arr

if __name__ == "__main__":
    data = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print(f"Original: {data}")
    bucket_sort(data)
    print(f"Sorted:   {data}")
    
    # Integer test
    data_int = [10, 4, 3, 2, 8, 11]
    print(f"Original (Int): {data_int}")
    bucket_sort(data_int)
    print(f"Sorted (Int):   {data_int}")
