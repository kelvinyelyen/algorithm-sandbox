# Huffman Coding

## What is it?
**Huffman Coding** is a popular technique used for lossless data compression. It assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters.

## How it works
1.  Create a leaf node for each unique character and build a min heap of all leaf nodes.
2.  Extract two nodes with the minimum frequency from the min heap.
3.  Create a new internal node with a frequency equal to the sum of the two nodes' frequencies. Make the two extracted nodes its children.
4.  Add this new node to the min heap.
5.  Repeat steps 2 and 3 until the heap contains only one node (the root).

## Complexity
- **Time**: **O(N log N)**.
- **Space**: **O(N)**.

## Example Usage
```bash
python3 huffman_coding.py
```
