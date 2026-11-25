class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [math.inf] * (n + 1)
        def sol(i):
            if i == 0 or i == 1:
                return 0
            if dp[i] == math.inf:
                dp[i] = min(sol(i-1) + cost[i-1], sol(i-2) + cost[i-2])
            return dp[i]
        return sol(n)