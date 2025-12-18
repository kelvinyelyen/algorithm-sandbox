# Binary Search

## What is it?
**Binary Search** is a fast search algorithm that works on a sorted array. It repeatedly divides the search interval in half.

## How it works
1.  Compare the target value to the middle element of the array.
2.  If they are equal, the target is found.
3.  If the target is smaller, search the left half.
4.  If the target is larger, search the right half.
5.  Repeat until the target is found or the interval is empty.

## Complexity
- **Time**: **O(log n)**.
- **Space**: **O(1)** (iterative) or **O(log n)** (recursive stack).

## Example Usage
```bash
python3 binary_search.py
```
