# Fibonacci Series

## What is it?
The **Fibonacci Series** is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

## How it works (Dynamic Programming)
Instead of a naive recursive approach which takes exponential time O(2^n), we store the results of subproblems.
1.  Create an array `f` where `f[i]` stores the i-th Fibonacci number.
2.  Base cases: `f[0] = 0`, `f[1] = 1`.
3.  Fill the rest: `f[i] = f[i-1] + f[i-2]`.

## Complexity
- **Time**: **O(n)**.
- **Space**: **O(n)** (can be optimized to O(1) by storing only last two numbers).

## Example Usage
```bash
python3 fibonacci_series.py
```
