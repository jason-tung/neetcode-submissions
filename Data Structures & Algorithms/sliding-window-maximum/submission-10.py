class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for r in range(len(nums)):
            l = r - k + 1
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)
            while l > dq[0]:
                dq.popleft()
            if r >= k - 1:
                res.append(nums[dq[0]])
        return res