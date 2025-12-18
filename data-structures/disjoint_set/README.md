# Disjoint Set (Union-Find)

## What is it?
The **Disjoint Set** (or **Union-Find**) data structure keeps track of elements partitioned into a number of disjoint (non-overlapping) sets. It provides near-constant-time operations to add new sets, merge existing sets, and determine whether elements are in the same set.

## How it works
It maintains a collection of sets where each set is represented by a representative element (often called the "root").
- **Find**: Determine which subset a particular element is in.
- **Union**: Join two subsets into a single subset.

## Optimizations
1.  **Path Compression**: During `find`, flatten the structure of the tree by making nodes point directly to the root.
2.  **Union by Rank/Size**: Always attach the smaller tree to the root of the larger tree to keep the tree height small.

## Complexity
With both optimizations, the amortized time complexity is **O(α(n))**, where α is the inverse Ackermann function, which is practically constant for all reasonable inputs.

## Example Usage
Execute the script:
```bash
python3 disjoint_set.py
```
