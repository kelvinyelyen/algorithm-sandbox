# Edit Distance (Levenshtein Distance)

## What is it?
**Edit Distance** is a way of quantifying how dissimilar two strings (e.g., words) are to one another by counting the minimum number of operations required to transform one string into the other. Operations allowed: Insert, Remove, Replace.

## How it works (Dynamic Programming)
We build a table `dp[i][j]` that stores the edit distance between the first `i` characters of string 1 and the first `j` characters of string 2.
1.  If `str1[i] == str2[j]`, then `dp[i][j] = dp[i-1][j-1]`.
2.  Else, `dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])`.

## Complexity
- **Time**: **O(m * n)**.
- **Space**: **O(m * n)**.

## Example Usage
```bash
python3 edit_distance.py
```
