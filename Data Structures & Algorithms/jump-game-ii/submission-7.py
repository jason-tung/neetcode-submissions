class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = jumps = 0
        while l <= r < len(nums) - 1:
            l_new = r + 1
            for i in range(l, r + 1):
                r = max(i + nums[i], r)
            jumps += 1
            l = l_new
        return jumps