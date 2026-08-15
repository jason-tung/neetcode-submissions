class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = [-1] * (target + 1)
        dp[0] = 1
        def sol(cur, i):
            if cur < 0:
                return 0
            if dp[cur] == -1:
                if i >= len(nums):
                    dp[cur] = 0
                elif sol(cur-nums[i], i+1) or sol(cur, i+1):
                    dp[cur] = 1
                else:
                    dp[cur] = 0
            return dp[cur]
        return sol(target, 0) == 1
        
            
