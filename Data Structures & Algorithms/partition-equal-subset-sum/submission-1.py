class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = [[-1] * (target + 1)] * len(nums)
        def dfs(i, cur):
            if cur == target:
                return 1
            if cur > target or i == len(nums):
                return 0
            if dp[i][cur] == -1:
                if dfs(i+1, cur + nums[i]) == 1:
                    dp[i][cur] = 1
                if dfs(i+1, cur) == 1:
                    dp[i][cur] = 1
            return dp[i][cur]
        return dfs(0, 0) == 1
        
            
