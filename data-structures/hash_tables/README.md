# Hash Table

## What is it?
A **Hash Table** is a data structure which stores data in an associative manner (key-value pairs). In a hash table, data is stored in an array format, where each data value has its own unique index value.

## How it works
-   **Hash Function**: Converts key into an integer index.
-   **Collision Handling**:
    -   **Chaining**: Use a linked list at each index.
    -   **Open Addressing**: Probe for next empty slot.

## Complexity
-   **Insert/Delete/Search**: **O(1)** on average. **O(N)** worst case (collisions).

## Example Usage
```bash
python3 hash_table.py
```
