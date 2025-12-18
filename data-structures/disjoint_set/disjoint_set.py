class DisjointSet:
    """
    Disjoint Set Union (DSU) with path compression and union by rank.
    """
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i):
        """
        Finds the representative (root) of the set containing element i.
        Uses path compression for optimization.
        """
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i, j):
        """
        Unions the sets containing elements i and j.
        Uses union by rank for optimization.
        """
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            print(f"Union({i}, {j}): Sets merged.")
            return True
        else:
            print(f"Union({i}, {j}): Already in the same set.")
            return False

if __name__ == "__main__":
    # Example: 5 elements, 0 to 4
    dsu = DisjointSet(5)

    dsu.union(0, 2)
    dsu.union(4, 2)
    dsu.union(3, 1)

    print(f"Find(4): {dsu.find(4)}")
    print(f"Find(0): {dsu.find(0)}")
    
    if dsu.find(4) == dsu.find(0):
        print("4 and 0 are in the same set")
    else:
        print("4 and 0 are in different sets")

    dsu.union(4, 0) # Should say already same set
