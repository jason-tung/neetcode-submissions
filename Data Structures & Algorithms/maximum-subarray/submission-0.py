class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = -math.inf
        cur = 0
        for k in nums:
            cur += k
            m = max(cur, m)
            cur = max(0, cur)
        return m