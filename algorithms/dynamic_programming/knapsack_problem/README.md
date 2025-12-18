# Knapsack Problem (0/1)

## What is it?
The **0/1 Knapsack Problem** is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

## How it works
We build a table `dp[i][w]` representing the maximum value attainable with the first `i` items and a capacity `w`.
1.  If weight of current item > current capacity, we don't include it.
2.  Else, max value is the maximum of:
    - Including the item: `val[i] + dp[i-1][w-weight[i]]`
    - Excluding the item: `dp[i-1][w]`

## Complexity
- **Time**: **O(N * W)** where N is number of items and W is capacity.
- **Space**: **O(N * W)**.

## Example Usage
```bash
python3 knapsack_problem.py
```
