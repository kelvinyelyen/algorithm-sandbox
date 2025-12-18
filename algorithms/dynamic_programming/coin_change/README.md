# Coin Change Problem

## What is it?
The **Coin Change Problem** is a classic dynamic programming problem. Given a set of coin denominations and a total amount of money, we need to determine the fewest number of coins required to make up that amount.

## How it works
We build a table `dp` where `dp[i]` represents the minimum number of coins needed to make amount `i`.
1.  Initialize `dp[0] = 0` (0 coins for 0 amount).
2.  Initialize all other values to infinity (or a value larger than `amount`).
3.  Iterate through every amount from 1 to the target amount.
4.  For each amount, try every coin. If the coin value is smaller than or equal to the current amount, we can potentially use it.
    `dp[i] = min(dp[i], dp[i - coin] + 1)`

## Complexity
- **Time**: **O(S * n)**, where S is the amount and n is the number of coin denominations.
- **Space**: **O(S)** for the DP table.

## Example Usage
```bash
python3 coin_change.py
```
