class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for k in range(target, -1, -1):
                if k-n >= 0 and dp[k-n]:
                    dp[k] = True
        return dp[-1]
        
            
