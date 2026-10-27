class MedianFinder:

    def __init__(self):
        self.l, self.r = [], []

    def addNum(self, num: int) -> None:
        if not self.l:
            heapq.heappush_max(self.l, num)
        else:
            if num <= self.l[0]:
                heapq.heappush_max(self.l, num)
            else:
                heapq.heappush(self.r, num)
            if len(self.l) - len(self.r) > 1:
                n = heapq.heappop_max(self.l)
                heapq.heappush(self.r, n)
            elif len(self.r) > len(self.l):
                n = heapq.heappop(self.r)
                heapq.heappush_max(self.l, n)
    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return self.l[0]
        return (self.l[0] + self.r[0]) / 2
        
        