# Travelling Salesman Problem (TSP)

## What is it?
Given a set of cities and the distances between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the origin city.

## How it works
-   **Naive**: Check all (n-1)! permutations. O(n!).
-   **Dynamic Programming (Held-Karp)**:
    -   `dp[mask][i]` = min cost to visit set of cities represented by `mask`, ending at city `i`.
    -   Transition: `dp[mask | (1<<j)][j] = min(dp[mask | (1<<j)][j], dp[mask][i] + dist[i][j])`

## Complexity
- **Time**: **O(n^2 * 2^n)**.
- **Space**: **O(n * 2^n)**.

## Example Usage
```bash
python3 tsp.py
```
