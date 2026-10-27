class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [-1] * (n + 1)
        for i in range(m, -1, -1):
            nxt_dp = [0] * (n+1)
            for j in range(n, -1, -1):
                if i == m:
                    nxt_dp[j] = n - j
                elif j == n:
                    nxt_dp[j] = m - i
                elif word1[i] == word2[j]:
                    nxt_dp[j] = dp[j+1]
                else:
                    nxt_dp[j] = 1 + min(dp[j], nxt_dp[j+1], dp[j+1])
            dp = nxt_dp
        return dp[0]