# Subset Sum Problem (Backtracking)

## What is it?
The **Subset Sum Problem** asks whether a subset of a given set of integers sums up to a specific target value. It is a famous NP-complete problem.

## How it works (Backtracking)
We explore all possible subsets of the array to check if their sum equals the target.
1.  Start with an empty set and a sum of 0.
2.  Iterate through the array elements.
3.  For each element, we have two choices:
    - **Include** it in the current subset.
    - **Exclude** it from the current subset.
4.  Recursively check both possibilities.
5.  If the current sum equals the target, store/print the subset.
6.  If the current sum exceeds the target, prune the search branch (backtrack).

## Complexity
- **Time**: **O(2^n)** in the worst case, as there are 2^n total subsets.
- **Space**: **O(n)** for recursion stack.

## Example Usage
```bash
python3 subset_sum.py
```
