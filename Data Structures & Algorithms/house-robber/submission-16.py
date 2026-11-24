class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for k in nums:
            a, b = b, max(b, a + k)
        return b