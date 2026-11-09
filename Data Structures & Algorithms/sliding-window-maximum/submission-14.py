class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i, n in enumerate(nums):
            while dq and n >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            start_index = i - k + 1
            while dq and start_index > dq[0]:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
