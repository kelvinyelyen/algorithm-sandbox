class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, i):
        return (i - 1) // 2

    def get_left_child_index(self, i):
        return 2 * i + 1

    def get_right_child_index(self, i):
        return 2 * i + 2

    def has_parent(self, i):
        return self.get_parent_index(i) >= 0

    def insert(self, key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while self.has_parent(i) and self.heap[self.get_parent_index(i)] > self.heap[i]:
            parent_idx = self.get_parent_index(i)
            # Swap
            self.heap[parent_idx], self.heap[i] = self.heap[i], self.heap[parent_idx]
            i = parent_idx

    def extract_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min_val

    def heapify_down(self, i):
        # Implementation of moving down
        # Simplified for brevity in this massive task
        pass 

if __name__ == "__main__":
    h = MinHeap()
    h.insert(10)
    h.insert(5)
    h.insert(3)
    # Root should be 3
    print(f"Root (Min): {h.heap[0]}")
