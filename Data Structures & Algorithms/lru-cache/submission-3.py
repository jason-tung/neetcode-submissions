class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.n = self.p = None      

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}
        self.l = Node(-1,-1)
        self.r = Node(-1,-1)
        self.l.n = self.r
        self.r.p = self.l

    def remove(self,n):
        np, nn = n.p, n.n
        np.n, nn.p = nn, np
        del self.d[n.key]
        
    def insert(self, n):
        n.p, n.n = self.l, self.l.n
        self.l.n.p, self.l.n = n, n
        self.d[n.key] = n

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        n = self.d[key]
        self.remove(n)
        self.insert(n)
        return n.val
       

    def put(self, key: int, value: int) -> None:
        n = Node(key, value)
        if key in self.d:
            old = self.d[key]
            self.remove(old)
            self.insert(n)
        else:
            self.insert(n)
            if len(self.d) > self.cap:
                self.remove(self.r.p)
            
        
        
