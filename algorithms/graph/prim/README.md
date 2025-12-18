# Prim's Algorithm

## What is it?
**Prim's Algorithm** is a greedy algorithm that finds a Minimum Spanning Tree (MST) for a weighted undirected graph.

## How it works
1.  Initialize a tree with a single vertex.
2.  Grow the tree by one edge: found the minimum-weight edge connecting the tree to vertices not yet in the tree.
3.  Repeat until all vertices are in the tree.

## Complexity
- **Time**: **O(E log V)** with binary heap.
- **Space**: **O(V + E)**.

## Example Usage
```bash
python3 prim.py
```
