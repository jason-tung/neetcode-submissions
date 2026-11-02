class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i, n in enumerate(nums):
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res