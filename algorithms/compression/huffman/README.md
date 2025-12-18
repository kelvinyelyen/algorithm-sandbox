# Huffman Coding

## What is it?
**Huffman Coding** is a popular technique used for lossless data compression. It assigns variable-length codes to input characters, ensuring that the most frequent characters get the shortest codes.

## How it works
1.  Count frequency of all characters.
2.  Create a leaf node for each character.
3.  Add all nodes to a min-priority queue.
4.  Extract two minimum nodes, combine them into a new internal node with sum of frequencies.
5.  Add new node back to queue.
6.  Repeat until one node remains (Root).
7.  Traverse tree to assign 0 (left) and 1 (right) codes.

## Complexity
- **Time**: **O(N log N)** where N is number of unique characters.
- **Space**: **O(N)**.

## Example Usage
```bash
python3 huffman-coding.py
```
