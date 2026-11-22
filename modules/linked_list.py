class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly linked list for sequential observation history."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def to_list(self):
        values, current = [], self.head
        while current:
            values.append(current.data)
            current = current.next
        return values

    def __len__(self):
        return self.size
