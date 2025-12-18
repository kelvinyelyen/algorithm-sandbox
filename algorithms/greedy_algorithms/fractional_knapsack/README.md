# Fractional Knapsack Problem

## What is it?
In the **Fractional Knapsack Problem**, we can break items for maximizing the total value of the knapsack. This is different from 0/1 Knapsack where items are indivisible.

## How it works (Greedy)
1.  Calculate value-to-weight ratio for each item.
2.  Sort items in descending order of this ratio.
3.  Take items with the highest ratio.
4.  If the whole item fits, take it.
5.  If not, take as much fraction as possible to fill the knapsack.

## Complexity
- **Time**: **O(N log N)**.
- **Space**: **O(1)**.

## Example Usage
```bash
python3 fractional_knapsack.py
```
