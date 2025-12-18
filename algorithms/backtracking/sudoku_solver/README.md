# Sudoku Solver

## What is it?
Given a partially filled 9×9 grid, the goal is to fill the grid so that each row, each column, and each of the nine 3×3 subgrids contains all of the digits from 1 to 9.

## How it works (Backtracking)
1.  Find an empty cell.
2.  Try digits 1-9 in that cell.
3.  Check if the digit is valid (not in the same row, column, or 3x3 box).
4.  If valid, place the digit and verify if it leads to a solution recursively.
5.  If not, reset the cell (backtrack) and try the next digit.

## Complexity
- **Time**: **O(9^(N*N))**.
- **Space**: **O(N*N)**.

## Example Usage
```bash
python3 sudoku_solver.py
```
