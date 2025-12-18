# Shortest Paths (Floyd-Warshall)

## What is it?
Dynamic programming can be used to solve shortest path problems for all pairs of nodes. The **Floyd-Warshall algorithm** is a prime example.

## How it works
We consider a graph with vertices 1 through N. We define `dist[i][j][k]` as the shortest path from `i` to `j` using only intermediate vertices from the set `{1, ..., k}`.
Recursive step: `dist[k][i][j] = min(dist[k-1][i][j], dist[k-1][i][k] + dist[k-1][k][j])`.

(Note: The directory name is generic, assuming it refers to general DP shortest path approaches or specifically Floyd-Warshall/Bellman-Ford in a DP context).

## Complexity
- **Time**: **O(V^3)**.
- **Space**: **O(V^2)**.

## Example Usage
```bash
python3 shortest_paths.py
```
