class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-math.inf] * 2 for _ in prices]
        dp[-1][0] = 0
        dp[-1][1] = prices[-1]

        for i in range(n - 2, -1, -1):
            dp[i][0] = max(dp[i+1][0], dp[i+1][1] - prices[i])               
            if i == n - 2:
                dp[-2][1] = max(prices[-1], prices[-2])
            else:
                dp[i][1] = max(dp[i+1][1], dp[i+2][0] + prices[i])               
        return dp[0][0]


        # if not holding coin
        # dp(i, false) = max(dp(i+1, false), dp(i+1, true) - prices[i])
        # holding coin
        # dp(i, true) = max(dp(i+1, true), dp(i+2, false) +  prices[i])
