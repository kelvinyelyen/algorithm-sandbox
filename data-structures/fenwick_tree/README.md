# Fenwick Tree (Binary Indexed Tree)

## What is it?
A **Fenwick Tree** or **Binary Indexed Tree (BIT)** is a data structure that provides efficient methods for calculation and manipulation of the prefix sums of a table of values.

## Comparison with Segment Tree
- **Pros**:
    - Easier to implement.
    - Uses less memory (O(n) array vs O(4n) for Segment Tree).
    - Slightly faster in practice due to smaller constant factors.
- **Cons**:
    - Less flexible. While mainly used for prefix sums, adapting it for Range Minimum Query (RMQ) is more complex than with a Segment Tree.

## Complexity
- **Update**: O(log n)
- **Prefix Query**: O(log n)
- **Space**: O(n)

## Key Logic
It relies on the binary representation of the index.
- `i & (-i)` gives the least significant bit (LSB) of `i`.
- Adding LSB allows traversing "up" the tree for updates.
- Subtracting LSB allows traversing "down" for queries.

## Example Usage
```bash
python3 fenwick_tree.py
```
