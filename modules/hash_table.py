class HashTable:
    """Educational separate-chaining hash table."""
    def __init__(self, capacity=31):
        self.capacity = capacity
        self.buckets = [[] for _ in range(capacity)]

    def _index(self, key):
        return hash(str(key).lower()) % self.capacity

    def insert(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        for k, value in self.buckets[self._index(key)]:
            if k == key:
                return value
        return None

    def delete(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        return False
