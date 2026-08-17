class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * n for _ in range(amount + 1)]
        def dfs(i, val):
            if val > amount:
                return 0
            if dp[val][i] == -1:
                if val == amount:
                    dp[val][i] = 1
                else:
                    tot = 0
                    for j in range(i, n):
                        tot += dfs(j, val + coins[j])
                    dp[val][i] = tot
            return dp[val][i]
        return dfs(0,0)