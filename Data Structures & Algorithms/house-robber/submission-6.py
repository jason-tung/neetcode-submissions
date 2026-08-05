class Solution:
    # opt(i) = Max(opt(i-2) + f(i), opt(i-1))
    # bottom up with 2 counter cnstant space instead of full cache
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        last_houses = [nums[0], max(nums[1], nums[0])]
        for i in range(2, len(nums)):
            n = nums[i]
            last_houses[0], last_houses[1] = last_houses[1], max(last_houses[0] + nums[i], last_houses[1])
        return last_houses[1]