# Longest Common Subsequence (LCS)

## What is it?
The **Longest Common Subsequence** problem is the problem of finding the longest subsequence common to all sequences in a set of sequences (often just two sets). It differs from the longest common substring problem: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences.

## How it works
We use a 2D table `L`. `L[i][j]` contains the length of LCS of `X[0..i-1]` and `Y[0..j-1]`.
1.  If `X[i-1] == Y[j-1]`, then `L[i][j] = 1 + L[i-1][j-1]`.
2.  Else, `L[i][j] = max(L[i-1][j], L[i][j-1])`.

## Complexity
- **Time**: **O(m * n)** where m and n are string lengths.
- **Space**: **O(m * n)**.

## Example Usage
```bash
python3 longest_common_subsequence.py
```
