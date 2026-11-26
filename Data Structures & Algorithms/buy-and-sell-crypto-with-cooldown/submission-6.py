class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-math.inf] * 2 for _ in prices]
        def sol(i, has_coin):
            if i >= len(prices):
                return 0
            if dp[i][has_coin] == -math.inf:
                if has_coin:
                    dp[i][has_coin] = max(sol(i+1, True), sol(i+2, False) + prices[i])
                else:
                    dp[i][has_coin] = max(sol(i+1, False), sol(i+1, True) -  prices[i])
            return dp[i][has_coin]
        return sol(0, False)


        # if not holding coin
        # dp(i, false) = max(dp(i+1, false), dp(i+1, true) - prices[i])
        # holding coin
        # dp(i, true) = max(dp(i+1, true), dp(i+2, false) +  prices[i])
