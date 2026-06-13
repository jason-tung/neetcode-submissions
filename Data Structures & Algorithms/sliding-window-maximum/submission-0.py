class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-n, i) for i,n in enumerate(nums[:k - 1])]
        heapq.heapify(heap)
        res = [0] * (len(nums) - k + 1)
        for r in range(k-1, len(nums)):
            l = r-k+1
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1] < l:
                heapq.heappop(heap)
            res[l] = heap[0]
        return [-t[0] for t in res]

