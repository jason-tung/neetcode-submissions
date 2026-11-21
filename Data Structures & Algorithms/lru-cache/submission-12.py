class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.nxt, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
    
    def bump(self, node):
        head_next = self.head.nxt
        node.prev, node.nxt = self.head, head_next
        self.head.nxt = head_next.prev = node

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
            self.remove(node)
        self.d[key] = node = Node(key, value)
        self.bump(node)
        if self.cap < len(self.d):
            last = self.tail.prev
            self.remove(last)
            del self.d[last.key]

        
            
        
        
        
