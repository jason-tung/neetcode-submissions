class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, h = [], []
        for r in range(len(nums)):
            heapq.heappush_max(h, (nums[r], r))
            l = max(0, r - k + 1)
            if r - l + 1 == k:
                while h[0][1] < l:
                    heapq.heappop_max(h)
                res.append(h[0][0])
        return res