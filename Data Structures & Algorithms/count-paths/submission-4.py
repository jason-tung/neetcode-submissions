class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        def sol(i):
            if i > 0:
                sol(i-1)
                for j in range(1,n):
                    dp[j] += dp[j-1]
            return dp[-1]
        return sol(m-1)
