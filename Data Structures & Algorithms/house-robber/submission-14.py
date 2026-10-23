class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b = 0,0
        for k in nums:
            a,b = max(b + k, a), a
        return a