class MaxHeap:
    """Max Heap storing (priority, payload) pairs."""
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def push(self, priority, payload):
        item = {"_priority": float(priority), **payload}
        self._items.append(item)
        self._sift_up(len(self._items) - 1)

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._items[parent]["_priority"] >= self._items[i]["_priority"]:
                break
            self._items[parent], self._items[i] = self._items[i], self._items[parent]
            i = parent

    def pop(self):
        if not self._items:
            return None
        self._items[0], self._items[-1] = self._items[-1], self._items[0]
        result = self._items.pop()
        if self._items:
            self._sift_down(0)
        return result

    def _sift_down(self, i):
        n = len(self._items)
        while True:
            largest = i
            left, right = 2*i + 1, 2*i + 2
            if left < n and self._items[left]["_priority"] > self._items[largest]["_priority"]:
                largest = left
            if right < n and self._items[right]["_priority"] > self._items[largest]["_priority"]:
                largest = right
            if largest == i:
                break
            self._items[i], self._items[largest] = self._items[largest], self._items[i]
            i = largest

    def peek(self):
        return self._items[0] if self._items else None

    def pop_all(self):
        result = []
        while self._items:
            result.append(self.pop())
        return result

    def peek_many(self, count):
        ordered = sorted(self._items, key=lambda x: x["_priority"], reverse=True)
        return ordered[:count]
