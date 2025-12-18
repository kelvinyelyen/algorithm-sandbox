class FenwickTree:
    """
    Fenwick Tree (Binary Indexed Tree) implementation.
    1-based indexing is commonly used for BIT for easier bit manipulation logic.
    """
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        """
        Adds delta to element at index i (1-based).
        """
        print(f"Adding {delta} to index {i}")
        while i <= self.size:
            self.tree[i] += delta
            i += i & (-i) # Move to next node

    def query(self, i):
        """
        Returns the prefix sum from index 1 to i.
        """
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i) # Move to parent
        return s

    def range_query(self, l, r):
        """
        Returns the sum of range [l, r].
        """
        return self.query(r) - self.query(l - 1)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    ft = FenwickTree(len(data))
    
    # Initialize BIT
    for idx, val in enumerate(data):
        ft.update(idx + 1, val)

    print(f"Data: {data}")
    print(f"Prefix sum up to index 3 (1+2+3): {ft.query(3)}") # 6
    print(f"Range sum 2 to 4 (2+3+4): {ft.range_query(2, 4)}") # 9
    
    ft.update(3, 2) # Add 2 to index 3. Value becomes 3+2=5. Data: [1, 2, 5, 4, 5]
    print(f"Updated value at index 3 by +2")
    print(f"New range sum 2 to 4 (2+5+4): {ft.range_query(2, 4)}") # 11
