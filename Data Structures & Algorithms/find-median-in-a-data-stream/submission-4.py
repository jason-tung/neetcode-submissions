class MedianFinder:

    def __init__(self):
        self.l, self.r, self.size = [], [], 0

    def addNum(self, num: int) -> None:
        if not self.r or num <= self.r[0]:
            heapq.heappush_max(self.l, num)
        else:
            heapq.heappush(self.r, num)
        if abs(len(self.l) - len(self.r)) > 1:
            if len(self.l) > len(self.r):
                n = heapq.heappop_max(self.l)
                heapq.heappush(self.r, n)
            else:
                n = heapq.heappop(self.r)
                heapq.heappush_max(self.l, n)
        self.size += 1
    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return self.l[0]
        elif len(self.l) < len(self.r):
            return self.r[0] 
        return (self.l[0] + self.r[0]) / 2
        
        