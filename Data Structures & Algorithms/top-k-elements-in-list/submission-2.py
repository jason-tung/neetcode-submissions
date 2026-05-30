class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        h = []
        for n,f in freq.items():
            heapq.heappush(h, (f,n))
            if len(h) > k:
                heapq.heappop(h)
        return [x[1] for x in h]
        
