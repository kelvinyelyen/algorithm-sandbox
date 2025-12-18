# Matrix Chain Multiplication

## What is it?
**Matrix Chain Multiplication** is an optimization problem regarding the most efficient way to multiply a given sequence of matrices. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications (i.e., parenthesization).

## How it works
We compute the optimal structure for multiplying subchains of matrices `M_i` through `M_j` and combine them.
`m[i, j] = min(m[i, k] + m[k+1, j] + p[i-1]*p[k]*p[j])` for all valid k.

## Complexity
- **Time**: **O(n^3)**.
- **Space**: **O(n^2)**.

## Example Usage
```bash
python3 matrix_chain_multiplication.py
```
