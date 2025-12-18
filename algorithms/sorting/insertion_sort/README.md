# Insertion Sort

## What is it?
**Insertion Sort** is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

## How it works
1.  Iterate from the second element to the last.
2.  Compare the current element with the largest value in the sorted sub-list (to its left).
3.  Shift all the elements in the sorted sub-list that are greater than the value to be sorted.
4.  Insert the value.

## Complexity
- **Time**: **O(n^2)**.
- **Space**: **O(1)**.

## Example Usage
```bash
python3 insertion_sort.py
```
