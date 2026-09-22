class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        def dfs(i, can_buy):
            if i >= n:
                return 0
            if dp[i][can_buy] == -1:
                if can_buy:
                    dp[i][can_buy] = max(dfs(i + 1, 0) - prices[i], dfs(i+1, 1))
                else:
                    sell_now = prices[i] + dfs(i+2, 1)
                    hold = dfs(i+1, 0)
                    dp[i][can_buy] = max(sell_now, hold)
            return dp[i][can_buy]
        return dfs(0,1)
