# Dijkstra's Algorithm

## What is it?
**Dijkstra's Algorithm** finds the shortest paths from a single source vertex to all other vertices in a weighted graph (with non-negative weights).

## How it works (Greedy)
1.  Initialize distances to infinity, except source (0).
2.  Use a priority queue (min-heap) to pick the unvisited vertex with the smallest distance.
3.  "Relax" all adjacent edges: if a shorter path to a neighbor is found through the current vertex, update the neighbor's distance.
4.  Repeat until all vertices are visited or the queue is empty.

## Complexity
- **Time**: **O(E log V)** using a binary heap.
- **Space**: **O(V + E)**.

## Example Usage
```bash
python3 dijkstra.py
```
