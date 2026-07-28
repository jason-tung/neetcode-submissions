class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for k in nums:
            n ^= k
        return n