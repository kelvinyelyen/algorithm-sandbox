# Pattern Searching (Naive)

## What is it?
**Naive Pattern Searching** is the simplest method for finding a pattern in a text.

## How it works
1.  Slide the pattern over text one by one.
2.  Check for a match.
3.  If a match is found, print/store the starting index.

## Complexity
- **Time**: **O(n * m)** worst case (e.g., text="AAAAA", pattern="AAA").
- **Space**: **O(1)**.

## Optimizations
Better algorithms like KMP, Rabin-Karp, or Z Algorithm (also implemented in this repo) are preferred for large texts.

## Example Usage
```bash
python3 pattern_searching.py
```
