class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')] * (len(cost) + 2)
        dp[0] = 0
        dp[1] = 0
        for i in range(0, len(cost)):
            dp[i + 1] = min(dp[i + 1], cost[i] + dp[i])
            dp[i+2] = min(dp[i + 2], cost[i] + dp[i])
        return dp[-2]

