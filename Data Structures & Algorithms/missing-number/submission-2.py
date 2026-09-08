class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for k in range(0, len(nums) + 1):
            if k not in nums:
                return k