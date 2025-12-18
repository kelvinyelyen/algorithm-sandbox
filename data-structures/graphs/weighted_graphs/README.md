# Weighted Graphs

## What is it?
A **Weighted Graph** is a graph in which a number (the weight) is assigned to each edge. Such weights might represent costs, lengths, or capacities, depending on the problem.

## Uses
-   Shortest Path Problems (Dijkstra, Bellman-Ford).
-   Minimum Spanning Tree Problems (Prim, Kruskal).
-   Network Flow Problems.

## Representation
-   **Adjacency List**: Store tuples `(neighbor, weight)` in the list.
-   **Adjacency Matrix**: Store `weight` in `matrix[i][j]` (use infinity for no edge).

## Example Usage
```bash
python3 weighted_graphs.py
```
