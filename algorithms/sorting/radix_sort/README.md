# Radix Sort

## What is it?
**Radix Sort** is a non-comparative sorting algorithm. It sorts integers by processing individual digits. It avoids comparison by creating and distributing elements into buckets according to their radix (base).

## How it works
1.  Find the maximum number to determine the number of digits to process.
2.  Start from the least significant digit (LSD) and sort the numbers based on that digit. A stable sorting algorithm (usually Counting Sort) is used for this step.
3.  Move to the next significant digit and repeat the process until the most significant digit is processed.

## Complexity
- **Time**: O(nk), where n is the number of elements and k is the number of digits (or bits) in the largest number.
- **Space**: O(n + k) (for the intermediate counting sort).

## Use Cases
- Useful for sorting large lists of integers or strings where the length of the keys (k) is small compared to the number of items (n).

## Example Usage
```bash
python3 radix_sort.py
```
