from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.heap = nums
        self.k = k
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k:
            heappushpop(self.heap, val)
        else:
            heappush(self.heap, val)
        return self.heap[0]
