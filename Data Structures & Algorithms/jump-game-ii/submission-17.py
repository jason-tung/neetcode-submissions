class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = l = r = 0
        while r < len(nums) - 1:
            next_r = r
            for i in range(l,r+1):
                next_r = max(next_r, nums[i] + i)
            steps += 1
            l, r = r+1, next_r
        return steps