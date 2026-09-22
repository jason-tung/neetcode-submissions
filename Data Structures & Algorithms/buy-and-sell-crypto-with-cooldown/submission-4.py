class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n-1][0] = prices[n-1]
        for i in range(n - 2, -1, -1):
            dp[i][1] = max(dp[i+1][0] - prices[i], dp[i+1][1])
            dp[i][0] = max(dp[i+2][1] + prices[i], dp[i+1][0])
        return dp[0][1]