# Bellman-Ford Algorithm

## What is it?
The **Bellman-Ford algorithm** is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph.

## Key Feature
Unlike Dijkstra's algorithm, Bellman-Ford works correctly in graphs in which some of the edge weights are negative numbers. It can also detect negative cycles.

## How it works
1.  Initialize distance to source to 0 and all other vertices to infinity.
2.  Relax all edges `|V| - 1` times.
    - For each edge `(u, v)` with weight `w`:
    - `if dist[u] + w < dist[v]: dist[v] = dist[u] + w`
3.  Check for negative weight cycles. If we can still relax an edge, a negative cycle exists.

## Complexity
- **Time**: **O(V * E)**.
- **Space**: **O(V)**.

## Example Usage
```bash
python3 bellman_ford.py
```
