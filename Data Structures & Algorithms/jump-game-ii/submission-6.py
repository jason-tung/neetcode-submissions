class Solution:
    def jump(self, nums: List[int]) -> int:
        d = [float('inf')] * len(nums)
        d[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            r = min(len(nums), i + nums[i] + 1)
            d[i] = (min(d[i:r]) if i < r else d[i]) + 1
        return d[0]