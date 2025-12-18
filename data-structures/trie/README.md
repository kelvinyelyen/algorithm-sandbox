# Trie (Prefix Tree)

## What is it?
A **Trie** (derived from re**trie**val) is a tree-like data structure used to efficiently store and retrieve keys in a dataset of strings. It is particularly useful for tasks involving prefixes, such as autocomplete or spell checking.

## How it works
- Each node represents a character of a string.
- The root represents an empty string.
- The path from the root to a node represents a prefix of a string.
- Nodes can be marked as "end of word" to indicate that a full word concludes at that character.

## Key Operations
1.  **Insert**: Walk down the tree, creating nodes for characters if they don't exist. Mark the last node as an end of word. Time complexity: O(L), where L is the length of the word.
2.  **Search**: Walk down the tree checking if characters exist. Return true if we reach the end of the word and the last node is marked as end of word. Time complexity: O(L).
3.  **StartsWith**: Distinct from search, checking if a prefix exists in the trie. Time complexity: O(L).

## Example Usage
Execute the script to see it in action:
```bash
python3 trie.py
```
