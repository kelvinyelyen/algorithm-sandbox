# Heap Sort

## What is it?
**Heap Sort** is a comparison-based sorting algorithm that uses a Binary Heap data structure. It is similar to Selection Sort where we first find the maximum element and place the maximum element at the end.

## How it works
1.  Build a max heap from the input data.
2.  At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of the heap by 1.
3.  Heapify the root of the tree.
4.  Repeat step 2 while the size of the heap is greater than 1.

## Complexity
- **Time**: **O(n log n)**.
- **Space**: **O(1)**.

## Example Usage
```bash
python3 heap_sort.py
```
