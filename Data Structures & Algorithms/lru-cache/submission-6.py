class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.last_updated = {}
        self.keys = deque()
        self.cap = capacity
        self.counter = 0

    def getCount(self):
        self.counter += 1
        return self.counter

    def get(self, key: int) -> int:
        timestamp = self.getCount()
        self.keys.appendleft((key, timestamp))
        self.last_updated[key] = timestamp
        return self.d[key] if key in self.d else -1

    def put(self, key: int, value: int) -> None:
        self.get(key)
        self.d[key] = value
        while len(self.d) > self.cap:
            k,t = self.keys.pop()
            if t == self.last_updated[k] and k in self.d:
                del self.d[k]

