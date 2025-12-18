def subset_sum(arr, target):
    """
    Finds if there exists a subset of the given array whose sum is equal to the target.
    Uses backtracking to print all such subsets.
    """
    subsets = []
    n = len(arr)
    
    def backtrack(start_index, current_subset, current_sum):
        # Base case: if sum matches target
        if current_sum == target:
            subsets.append(list(current_subset))
            return
        
        # If sum exceeds target or we run out of elements
        if current_sum > target or start_index == n:
            return

        # Iterate through remaining elements
        for i in range(start_index, n):
            # Include arr[i]
            current_subset.append(arr[i])
            backtrack(i + 1, current_subset, current_sum + arr[i])
            # Backtrack: remove arr[i]
            current_subset.pop()
            
            # Optimization: if array is sorted, we can stop early if sum + arr[i] > target
            # ignoring duplicates etc. could be added here.

    # Sort array to potentially handle duplicates or optimizations nicely
    # arr.sort() 
    backtrack(0, [], 0)
    return subsets

if __name__ == "__main__":
    data = [10, 7, 5, 18, 12, 20, 15]
    target = 35
    print(f"Data: {data}")
    print(f"Target: {target}")
    
    solutions = subset_sum(data, target)
    if solutions:
        print(f"Found {len(solutions)} subset(s) with sum {target}:")
        for s in solutions:
            print(s)
    else:
        print("No subset found.")
    
    # Expected: [10, 5, 20], [18, 12, 5] ... ? 
    # 10+5+20=35. 18+12+5=35.
    
    data2 = [1, 2, 1]
    target2 = 3
    print(f"\nData: {data2}, Target: {target2}")
    print(f"Subsets: {subset_sum(data2, target2)}")
