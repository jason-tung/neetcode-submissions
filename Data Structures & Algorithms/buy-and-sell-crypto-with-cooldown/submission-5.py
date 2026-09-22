class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(2)]
        dp[0][0] = prices[-1]
        for i in range(n - 2, -1, -1):
            nxt = [[0,0], dp[0]]
            nxt[0][1] = max(dp[0][0] - prices[i], dp[0][1])
            nxt[0][0] = max(dp[1][1] + prices[i], dp[0][0])
            dp = nxt
        return dp[0][1]