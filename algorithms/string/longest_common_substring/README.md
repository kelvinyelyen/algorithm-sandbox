# Longest Common Substring

## What is it?
The **Longest Common Substring** problem is to find the longest string that is a substring of two or more strings.

## How it works (Dynamic Programming)
Similar to LCS (Subsequence), but we reset the count if characters don't match.
1.  Create `dp[i][j]` table.
2.  If `str1[i] == str2[j]`, `dp[i][j] = dp[i-1][j-1] + 1` and update max length found so far.
3.  Else, `dp[i][j] = 0`.

## Complexity
- **Time**: **O(m * n)**.
- **Space**: **O(m * n)** (can be optimized to O(min(m, n))).

## Example Usage
```bash
python3 longest_common_substring.py
```
