class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # faster bottom up but a little unreadable
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            if dp[i] != -1: 
                for k in coins:
                    if i + k <= amount:
                        if dp[i+k] == -1:
                            dp[i+k] = dp[i] + 1
                        else:
                            dp[i+k] = min(dp[i+k], dp[i] + 1)
        return dp[-1]