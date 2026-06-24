class Solution:
    def jump(self, nums: List[int]) -> int:
        d = [float('inf')] * len(nums)
        d[-1] = 0
        def dfs(i):
            if d[i] != float('inf'):
                return d[i]
            if i == len(nums) - 1:
                return 0
            r = min(i+nums[i] + 1, len(nums))
            for j in range(i + 1, r):
                if j < len(nums):
                    dfs(j)
            d[i] =( min(d[i+1:r]) if len(d[i+1:r]) else float('inf')) + 1
            return d[i]
        return dfs(0)