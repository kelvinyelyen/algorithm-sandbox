class SegmentTree:
    """
    Segment Tree implementation for Range Sum Query.
    """
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self._build(data, left_child, start, mid)
            self._build(data, right_child, mid + 1, end)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, idx, val):
        """
        Update the value at index idx to val.
        """
        print(f"Updating index {idx} to {val}")
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self._update(left_child, start, mid, idx, val)
            else:
                self._update(right_child, mid + 1, end, idx, val)
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, L, R):
        """
        Return the sum of the range [L, R] inclusive.
        """
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self._query(2 * node + 1, start, mid, L, R)
        p2 = self._query(2 * node + 2, mid + 1, end, L, R)
        return p1 + p2

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(arr)

    print(f"Original Array: {arr}")
    print(f"Sum of range(1, 3) [indices 1,2,3 -> 3+5+7]: {st.query(1, 3)}") # 15
    
    st.update(1, 10) # array is now [1, 10, 5, 7, 9, 11]
    print(f"Sum of range(1, 3) after update: {st.query(1, 3)}") # 10+5+7 = 22
