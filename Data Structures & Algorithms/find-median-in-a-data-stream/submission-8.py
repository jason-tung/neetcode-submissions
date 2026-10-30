class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []

    def addNum(self, num: int) -> None:
        if not self.l:
            self.l.append(num)
            return
        if num > self.l[0]:
            heapq.heappush(self.r, num)
        else:
            heapq.heappush_max(self.l, num)
        if len(self.l) - len(self.r) > 1:
            heapq.heappush(self.r, heapq.heappop_max(self.l))
        elif len(self.r) - len(self.l) > 0:
            heapq.heappush_max(self.l, heapq.heappop(self.r))

    def findMedian(self) -> float:
        if len(self.l) > len(self.r):
            return self.l[0]
        return (self.l[0] + self.r[0]) / 2