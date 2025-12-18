# Z Algorithm

## What is it?
The **Z Algorithm** is a linear time string matching algorithm. It finds all occurrences of a pattern in a text.

## How it works
It constructs a **Z array**.
For a string `S` of length `n`, the Z-array is an array of length `n` where `Z[i]` is the length of the longest substring starting from `S[i]` which is also a prefix of `S`.

To use it for pattern matching:
1.  Concatenate the pattern `P` and text `T` with a special character `$`: `S = P + "$" + T`.
2.  Compute the Z-array for `S`.
3.  If `Z[i]` equals the length of `P`, then the pattern occurs in `T` starting at that position.

## Complexity
- **Time**: **O(n + m)**, where n is the length of text and m is the length of pattern.
- **Space**: **O(n + m)** for the Z-array.

## Comparison
It is similar in efficiency to KMP (Knuth-Morris-Pratt) but uses a different preprocessing approach (Z-array vs LPS array).

## Example Usage
```bash
python3 z_algorithm.py
```
