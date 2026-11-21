class Node:
    def __init__(self, key = 0, val=0, prev=None, next=None):
        self.key, self.val, self.prev, self.next = key, val, prev , next

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        return node
    
    def bump(self, node):
        head_next = self.head.next
        node.prev, node.next = self.head, head_next
        self.head.next = head_next.prev = node
        return node

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            return self.bump(self.d[key]).val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            self.d[key] = Node(key=key,val=value)
        else:
            self.d[key].val = value
            self.remove(self.d[key])
        self.bump(self.d[key])
        if len(self.d) > self.cap:
            last = self.tail.prev
            self.remove(last)
            del self.d[last.key]
            
        
        
        
