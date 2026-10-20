class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prev2 = 0
        for i in range(len(nums)):
            nums[i] = max(prev, prev2 + nums[i])
            prev, prev2 = nums[i], prev
        return nums[-1]