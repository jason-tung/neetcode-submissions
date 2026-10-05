class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = steps = 0 
        while r < len(nums) - 1:
            next_r = r
            for i in range(l, r + 1):
                next_r = max(nums[i] + i, next_r)
            l, r = r + 1, next_r
            steps += 1
        return steps