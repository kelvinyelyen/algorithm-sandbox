from heapq import heappush, heappop, heapify
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapify(heap)

    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heappush(heap, merged)

    return heap[0]

def generate_huffman_codes(root, current_code="", codes={}):
    if root is None:
        return
    
    if root.char is not None:
        codes[root.char] = current_code
        return

    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

def encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

def decode(encoded_text, root):
    decoded_text = ""
    current_node = root
    for bit in encoded_text:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = root
    
    return decoded_text

# Example usage
text = "this is an example for huffman encoding"
root = build_huffman_tree(text)
codes = {}
generate_huffman_codes(root, "", codes)
encoded_text = encode(text, codes)
decoded_text = decode(encoded_text, root)

print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)