class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        for i, n in enumerate(nums):
            while d and n >= nums[d[-1]]:
                d.pop()
            d.append(i)
            j = i - k + 1
            if d[0] < j:
                d.popleft()
            if i >= k - 1:
                res.append(nums[d[0]])
        return res