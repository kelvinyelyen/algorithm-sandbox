# Bucket Sort

## What is it?
**Bucket Sort** (or Bin Sort) is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sort algorithm.

## How it works
1.  **Scatter**: Go through the original array and put each element into an appropriate bucket. A simple hashing function (like `element_value * number_of_buckets`) is often used.
2.  **Order**: Sort each non-empty bucket. This can be done with any sorting algorithm (like Insertion Sort or Merge Sort).
3.  **Gather**: Visit the buckets in order and put all elements back into the original array.

## Complexity
- **Time**: Average case O(n + k), where n is the number of elements and k is the number of buckets. Worst case O(n^2) if all elements fall into the same bucket (depending on the inner sort used).
- **Space**: O(n + k).

## Use Cases
- Most effective when input is uniformly distributed over a range (e.g., floating point numbers in [0, 1]).

## Example Usage
```bash
python3 bucket_sort.py
```
