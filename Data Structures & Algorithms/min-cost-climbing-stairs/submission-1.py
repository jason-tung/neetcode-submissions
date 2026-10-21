class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        def solve(i):
            if i >= len(cost):
                return 0
            if dp[i] == -1:
                dp[i] = cost[i] + min(solve(i+1), solve(i+2))
            return dp[i]
        return min(solve(0), solve(1))