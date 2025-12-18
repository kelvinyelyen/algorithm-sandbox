# Hamiltonian Cycle

## What is it?
A **Hamiltonian Cycle** (or Hamiltonian Circuit) is a cycle in an undirected or directed graph that visits each vertex exactly once and returns to the starting vertex.

## How it works (Backtracking)
1.  Create an empty path array and add vertex 0 to it.
2.  Add other vertices, one by one, to the path.
3.  Check if adding a vertex to the path is valid (adjacent to the previously added vertex and not already in the path).
4.  If valid, recursively try to build the rest of the path.
5.  If all vertices are included and there is an edge from the last vertex to the first, a cycle is found.

## Complexity
- **Time**: **O(N!)**.
- **Space**: **O(N)**.

## Example Usage
```bash
python3 hamiltonian_cycle.py
```
