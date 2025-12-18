class TrieNode:
    """
    A node in the Trie structure.
    """
    def __init__(self):
        self.children = {}  # Dictionary to store children nodes
        self.is_end_of_word = False  # Flag to mark the end of a word

class Trie:
    """
    Trie (Prefix Tree) implementation.
    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        print(f"Inserted: {word}")

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

if __name__ == "__main__":
    trie = Trie()
    
    # Insert words
    trie.insert("apple")
    trie.insert("app")
    trie.insert("beer")
    trie.insert("add")
    trie.insert("jam")
    trie.insert("rental")

    # Search words
    print(f"Search 'apple': {trie.search('apple')}")   # True
    print(f"Search 'app': {trie.search('app')}")       # True
    print(f"Search 'ap': {trie.search('ap')}")         # False (prefix, not word)
    print(f"Search 'beer': {trie.search('beer')}")     # True
    
    # Check prefixes
    print(f"Starts with 'app': {trie.starts_with('app')}") # True
    print(f"Starts with 'ren': {trie.starts_with('ren')}") # True
    print(f"Starts with 'z': {trie.starts_with('z')}")     # False
