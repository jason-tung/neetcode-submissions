class MedianFinder:

    def __init__(self):
        self.lt = []
        self.gt = []

    def addNum(self, num: int) -> None:
        if not self.lt and not self.gt:
            self.lt.append(num)
            return
        if num >= self.lt[0]:
            heapq.heappush(self.gt, num)
        else:
            heapq.heappush_max(self.lt, num)
        diff = len(self.lt) - len(self.gt)
        if diff > 1:
            heapq.heappush(self.gt, heapq.heappop_max(self.lt))
        elif diff < -1:
            heapq.heappush_max(self.lt, heapq.heappop(self.gt))

    def findMedian(self) -> float:
        if len(self.lt) == len(self.gt):
            return (self.lt[0] + self.gt[0])/2
        return self.lt[0] if len(self.lt) > len(self.gt) else self.gt[0]
        
        