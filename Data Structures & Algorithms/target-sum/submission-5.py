class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n):
            for total in dp[i]:
                dp[i + 1][total + nums[i]] += dp[i][total]
                dp[i + 1][total - nums[i]] += dp[i][total]
        return dp[n][target]
        
