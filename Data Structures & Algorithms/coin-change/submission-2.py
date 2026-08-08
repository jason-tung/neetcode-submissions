class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # opt(i+k) = opt(i) + 1 for all k in coins
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for k in coins:
                if i + k <= amount:
                    dp[i+k] = min(dp[i+k], dp[i] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1