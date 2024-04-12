import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.node_id = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    if len(char_freq) == 1:  # Special case handling when there's only one character
        char, freq = char_freq.popitem()
        return Node(char, freq)

    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    node_id_counter = 0

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        merged.node_id = node_id_counter
        node_id_counter += 1
        heapq.heappush(heap, merged)

    root = heap[0]
    root.node_id = node_id_counter  # Set the ID for the root node
    return root

def generate_huffman_codes(root, current_code="", codes={}):
    if root is None:
        return
    
    if root.char is not None:
        codes[root.char] = current_code
        return

    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)

def encode(text, codes):
    return ''.join(codes[char] for char in text)

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

char_freq = {'A': 10, 'E': 15, 'I': 12, 'O': 3, 'U': 4, 'S': 13, 'T': 1}

root = build_huffman_tree(char_freq)
codes = {}
generate_huffman_codes(root, "", codes)
text = "AEIOUST"
encoded_text = encode(text, codes)
decoded_text = decode(encoded_text, root)

# Calculate average code length
total_symbols = sum(char_freq.values())
average_code_length = sum(char_freq[char] * len(codes[char]) for char in char_freq) / total_symbols

# Calculate length of Huffman coded message
huffman_coded_length_bits = total_symbols * average_code_length

print("Original text:", text)
print("Encoded text:", encoded_text)
print("Decoded text:", decoded_text)
print("Average code length:", average_code_length)
print("Length of Huffman coded message (in bits):", huffman_coded_length_bits)

# G = nx.Graph()

# def add_edges(node):
#     if node is None:
#         return

#     if node.left is not None:
#         G.add_edge(node.node_id, node.left.node_id)
#         add_edges(node.left)

#     if node.right is not None:
#         G.add_edge(node.node_id, node.right.node_id)
#         add_edges(node.right)

# root.node_id = 0
# add_edges(root)

# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_size=3000, font_size=10, node_color="lightblue", font_color="black")
# plt.show()
