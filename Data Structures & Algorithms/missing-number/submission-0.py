class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = len(nums) / 2 * (len(nums)+1)
        return int(target - sum(nums))