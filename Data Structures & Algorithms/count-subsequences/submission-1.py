class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[-1] = [1] * (n+1)
        # dp[i][j] = dp[i+1][j+1] + 1 if s[i] == t[j] and dp[i+1][j+1]
        # look at j+1 letter of t - if fulfilled at i+1 idex of s, we can rock
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i][j+1]
                if t[i] == s[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i][j + 1]
        return dp[0][0]