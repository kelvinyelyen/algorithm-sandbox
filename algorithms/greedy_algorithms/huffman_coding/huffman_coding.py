import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # For heap comparison
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    # Calculate frequency of each character
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    # Create a priority queue (min-heap) of nodes
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Extract two nodes with the lowest frequency
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        # Create a new internal node with these two nodes as children
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        # Add the new node to the heap
        heapq.heappush(heap, merged)

    return heap[0] # Root of the tree

def build_codes_helper(root, current_code, codes):
    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    build_codes_helper(root.left, current_code + "0", codes)
    build_codes_helper(root.right, current_code + "1", codes)

def huffman_encoding(data):
    if not data:
        return "", None

    root = build_huffman_tree(data)
    codes = {}
    build_codes_helper(root, "", codes)
    
    encoded_output = "".join([codes[char] for char in data])
    return encoded_output, root

def huffman_decoding(encoded_data, root):
    if not encoded_data or root is None:
        return ""

    decoded_output = []
    current_node = root
    
    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.left is None and current_node.right is None:
            decoded_output.append(current_node.char)
            current_node = root
            
    return "".join(decoded_output)

if __name__ == "__main__":
    string = "BCAADDDCCACACAC"
    print(f"Input string: {string}")
    
    encoded, tree = huffman_encoding(string)
    print(f"Encoded string: {encoded}")
    
    decoded = huffman_decoding(encoded, tree)
    print(f"Decoded string: {decoded}")
