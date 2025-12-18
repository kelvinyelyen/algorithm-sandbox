# Prim's Algorithm

## What is it?
**Prim's Algorithm** is a greedy algorithm that finds a Minimum Spanning Tree (MST) for a weighted undirected graph.

## How it works
1.  Initialize a tree with a single vertex, chosen arbitrarily from the graph.
2.  Grow the tree by one edge: of the edges that connect the tree to vertices not yet in the tree, find the minimum-weight edge, and transfer it to the tree.
3.  Repeat step 2 until all vertices are in the tree.

## Complexity
- **Time**: **O(E log V)** or **O(E + V log V)** using Fibonacci Heap.
- **Space**: **O(V + E)**.

## Example Usage
```bash
python3 prims_algorithm.py
```
