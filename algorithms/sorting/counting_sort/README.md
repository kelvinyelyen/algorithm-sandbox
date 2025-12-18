# Counting Sort

## What is it?
**Counting Sort** is an integer sorting algorithm that operates by counting the number of objects that possess distinct key values. It uses arithmetic on those counts to determine the positions of each key value in the output sequence.

## How it works
1.  **Count**: Iterate through the input array and count the frequency of each element.
2.  **Accumulate**: Modify the count array such that each element at each index stores the sum of previous counts. This indicates the position of each element in the sorted output.
3.  **Build**: Iterate through the input array (usually in reverse to maintain stability), place each element at its correct sorted position based on the count array, and decrement the count.

## Complexity
- **Time**: O(n + k), where n is the number of elements and k is the range of the input.
- **Space**: O(n + k).

## Limitations
- It is efficient only when the range of potential items (k) is not significantly greater than the number of items (n).
- It is typically used for positive integers. Handling negative integers or floating-point numbers requires adaptation (e.g., shifting values).

## Example Usage
```bash
python3 counting_sort.py
```
