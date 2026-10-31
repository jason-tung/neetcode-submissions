class Solution:
    def rob(self, nums: List[int]) -> int:
        a = b = 0
        for k in nums:
            a,b = b,max(a+k, b)
        return b