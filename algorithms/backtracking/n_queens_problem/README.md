# N-Queens Problem

## What is it?
The **N-Queens Problem** is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.

## How it works (Backtracking)
1.  Start in the leftmost column.
2.  If all queens are placed, return true.
3.  Try all rows in the current column.
4.  If a queen can be safely placed in this row, mark this [row, column] as part of the solution and recursively check if placing a queen here leads to a solution.
5.  If placing the queen in [row, column] leads to a solution, return true.
6.  If placing queen doesn't lead to a solution, unmark this [row, column] (backtrack) and try other rows.

## Complexity
- **Time**: **O(N!)**.
- **Space**: **O(N^2)**.

## Example Usage
```bash
python3 n_queens_problem.py
```
