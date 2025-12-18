# Quick Sort

## What is it?
**Quick Sort** is a Divide and Conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.

## How it works
1.  **Partition**: Pick a pivot (e.g., last element). Reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it.
2.  **Recursion**: Recursively apply the above steps to the sub-array of elements with smaller values and the sub-array of elements with greater values.

## Complexity
- **Time**: Average **O(n log n)**, Worst **O(n^2)**.
- **Space**: **O(log n)** (stack space).

## Example Usage
```bash
python3 quick_sort.py
```
