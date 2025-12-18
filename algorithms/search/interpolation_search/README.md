# Interpolation Search

## What is it?
**Interpolation Search** is an improved variant of Binary Search. This search algorithm works on the probing position of the required value. For this algorithm to work properly, the data collection should be in a sorted form and equally distributed.

## How it works
Binary Search always goes to the middle element to check. Interpolation search may go to different locations according to the value of the key being searched. For example, if the value of the key is closer to the last element, interpolation search is likely to start search toward the end side.

The position is calculated using the formula:
`pos = lo + ((x - arr[lo]) * (hi - lo) / (arr[hi] - arr[lo]))`

## Complexity
- **Time**: 
    - Average case: **O(log(log n))** (for uniformly distributed data).
    - Worst case: **O(n)** (e.g., exponential distribution).
- **Space**: O(1).

## Example Usage
```bash
python3 interpolation_search.py
```
