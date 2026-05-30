class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq_max_heap = [(-v,k) for k,v in freq.items()]
        heapq.heapify(freq_max_heap)
        return [heapq.heappop(freq_max_heap)[1] for _ in range(k)]
        
