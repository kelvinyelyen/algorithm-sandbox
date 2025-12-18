# Segment Tree

## What is it?
A **Segment Tree** is a binary tree used for storing information about intervals or segments. It allows querying which of the stored segments contain a given point. It is strictly a static structure; it cannot be modified once built (though values can be updated).

## What is it useful for?
It is extremely efficient for:
1.  **Range Queries**: Finding the sum, minimum, maximum, GCD, etc., of a subarray `arr[L...R]`.
2.  **Point Updates**: Modifying an element `arr[i]` and keeping the tree consistent.

Both operations take **O(log n)** time.

## How it works (Sum Example)
- The root of the tree represents the sum of the entire array.
- The leaves represent the individual elements of the array.
- Internal nodes represent the sum of their children's ranges.

## Example Usage
```bash
python3 segment_tree.py
```
