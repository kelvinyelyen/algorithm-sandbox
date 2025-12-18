# Adjacency Matrix and List Representations

## What is it?
Graphs can be represented in multiple ways. The two most common are:

1.  **Adjacency Matrix**: A 2D array where `matrix[i][j]` represents an edge from vertex `i` to vertex `j`.
2.  **Adjacency List**: An array of lists. The list at index `i` contains all vertices adjacent to vertex `i`.

## Comparison
| Feature | Adjacency Matrix | Adjacency List |
| :--- | :--- | :--- |
| **Space** | O(V^2) | O(V + E) |
| **Check Edge** | O(1) | O(degree(V)) |
| **Find Neighbors** | O(V) | O(degree(V)) |
| **Usage** | Dense graphs | Sparse graphs |

## Example Usage
```bash
python3 adjacency_matrix_and_list.py
```
