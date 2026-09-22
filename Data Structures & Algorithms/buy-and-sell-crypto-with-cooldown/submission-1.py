class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        def dfs(i, can_sell):
            if i >= n:
                return 0
            if dp[i][can_sell] == -1:
                if can_sell:
                    sell_now = prices[i] + dfs(i+2, 0)
                    hold = dfs(i+1, 1)
                    dp[i][can_sell] = max(sell_now, hold)
                else:
                    buy_now = dfs(i + 1, 1) - prices[i]
                    buy_later = dfs(i + 1, 0)
                    dp[i][can_sell] = max(buy_now, buy_later)
            return dp[i][can_sell]
        return dfs(0,0)
