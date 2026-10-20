class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            prev = nums[i-1] if i - 1 >= 0 else 0
            prev2 = nums[i-2] if i - 2 >= 0 else 0
            nums[i] = max(prev, prev2 + nums[i])
        return nums[-1]