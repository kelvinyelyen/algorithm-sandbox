# Floyd Warshall Algorithm

## What is it?
**Floyd Warshall** is an algorithm for finding shortest paths in a weighted graph with positive or negative edge weights (but no negative cycles). It finds shortest paths between **all pairs** of vertices.

## How it works (Dynamic Programming)
-   Initialize solution matrix `dist` same as input graph matrix.
-   Outer loop `k` from 0 to V:
    -   Inner loops `i`, `j` from 0 to V:
        -   `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

## Complexity
- **Time**: **O(V^3)**.
- **Space**: **O(V^2)**.

## Example Usage
```bash
python3 floyd-warshall.py
```
