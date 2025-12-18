# Directed and Undirected Graphs

## What is it?
-   **Undirected Graph**: Edges have no direction. The edge (u, v) is identical to (v, u).
-   **Directed Graph (Digraph)**: Edges have a direction. The edge (u, v) is different from (v, u).

## Implications
-   **Degree**: In undirected graphs, degree is the number of connecting edges. In digraphs, we track **in-degree** (incoming) and **out-degree** (outgoing) edges separately.
-   **Traversals**: Both BFS and DFS work on both types, but connectivity (strongly connected components) is more complex in digraphs.

## Example Usage
```bash
python3 directed_and_undirected_graphs.py
```
