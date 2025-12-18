class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self._hash(key)
        key_value = [key, value]

        # Check for update
        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self._hash(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        key_hash = self._hash(key)
        for i, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                self.table[key_hash].pop(i)
                return True
        return False

    def __str__(self):
        return str(self.table)

if __name__ == "__main__":
    h = HashTable()
    h.insert('a', 1)
    h.insert('b', 2)
    h.insert('c', 3)
    
    print(f"Get 'a': {h.get('a')}")
    print(f"Get 'z': {h.get('z')}")
    
    h.insert('a', 100) # update
    print(f"Get 'a' after update: {h.get('a')}")
    
    h.delete('b')
    print(f"Table: {h}")
