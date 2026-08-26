class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_jump = 0
        i = 0
        while i <= furthest_jump and i < len(nums):
            furthest_jump = max(i + nums[i], furthest_jump)
            i += 1
        return i == len(nums)