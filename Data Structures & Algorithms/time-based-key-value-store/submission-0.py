class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        return self.search(self.store[key], timestamp)
        
    def search(self, ary, value):
        l, r = 0, len(ary) - 1
        if not len(ary) or ary[0][0] > value:
            return ''
        while l<r:
            m = (l + r)//2
            p = ary[m][0]
            if p == value or p < value and m != r and ary[m+1][0] > value:
                return ary[m][1]
            if p > value:
                r = m - 1
            else:
                l = m + 1
        return ary[r][1]
            
        
