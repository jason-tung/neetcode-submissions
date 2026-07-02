class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None      

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.head = None
        self.tail = None

    def remove(self,key):
        n = self.d[key]
        np, nn = n.prev, n.next
        if np:
            np.next = nn
        if nn:
            nn.prev = np
        if n == self.head:
            self.head = nn
        if n == self.tail:
            self.tail = np
        del self.d[key]
        
    def insert(self,key, value):
        prev_head = self.head
        n = Node(key, value)
        self.head = n
        if not self.tail:
            self.tail = n
        n.next = prev_head
        if prev_head:
            prev_head.prev = n
        self.d[key] = n

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        n = self.d[key]
        self.remove(key)
        self.insert(n.key, n.val)
        return n.val
       

    def put(self, key: int, value: int) -> None:
        if key in self.d:     
            self.remove(key)
            self.insert(key, value)
        else:
            self.insert(key, value)
            if len(self.d) > self.cap:
                self.remove(self.tail.key)
            
        
        
