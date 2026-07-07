from heapq import * 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)
        while len(stones) > 1:
            s1,s2 = heappop_max(stones), heappop_max(stones)
            s3 = abs(s1-s2)
            heappush_max(stones, s3)
        return sum(stones)
        