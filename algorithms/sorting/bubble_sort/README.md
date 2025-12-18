# Bubble Sort

## What is it?
**Bubble Sort** is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

## How it works
1.  Iterate through the array from the first element to the last.
2.  Compare each pair of adjacent items.
3.  If the first is greater than the second, swap them.
4.  Repeat this process for `n` passes. After the `i-th` pass, the `i-th` largest element will be in its correct position at the end.

## Complexity
- **Time**: **O(n^2)**.
- **Space**: **O(1)**.

## Example Usage
```bash
python3 bubble_sort.py
```
