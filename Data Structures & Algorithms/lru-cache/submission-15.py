class Node:
    def __init__(self, key, val):
        self.next = self.prev = None
        self.key, self.val = key, val

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.cap = capacity
        self.head, self.tail = Node(0,0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def bump(self, node):
        first = self.head.next
        node.next, node.prev = first, self.head
        first.prev = self.head.next = node

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.remove(node)
            self.bump(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.remove(node)
        else:
            node = Node(key, value)
            self.d[key] = node
        self.bump(node)
        if len(self.d) > self.cap:
            last = self.tail.prev
            self.remove(last)
            del self.d[last.key]

        
