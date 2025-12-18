# Kruskal's Algorithm

## What is it?
**Kruskal's Algorithm** finds the Minimum Spanning Tree (MST) for a connected, weighted graph.

## How it works (Greedy)
1.  Sort all edges in simplified non-decreasing order of their weight.
2.  Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3.  Repeat step 2 until there are (V-1) edges in the spanning tree.
*   Uses **Disjoint Set (Union-Find)** data structure to check for cycles.

## Complexity
- **Time**: **O(E log E)** or **O(E log V)**.
- **Space**: **O(V + E)**.

## Example Usage
```bash
python3 mst_kruskal.py
```
