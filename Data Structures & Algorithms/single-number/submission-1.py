class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for k in nums:
            r ^= k
        return r