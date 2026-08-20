class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        dp = [1] * (n+1)
        dp[-1] = 0
        for i in range(m - 1, -1, -1):
            prev = 0 if i != m - 1 else 1
            for j in range(n - 1, -1, -1):
                tmp = dp[j]
                dp[j] = dp[j+1]
                if t[i] == s[j]:
                    dp[j] += prev
                prev = tmp
        return dp[0]