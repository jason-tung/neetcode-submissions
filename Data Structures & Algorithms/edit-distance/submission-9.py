class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [math.inf] * (m+1)
        for i in range(n, -1, -1):
            nxt_dp = [*dp]
            for j in range(m, -1, -1):
                if i == n:
                    nxt_dp[j] = m - j
                elif j == m:
                    nxt_dp[j] = n - i
                elif word1[i] == word2[j]:
                    nxt_dp[j] = dp[j + 1]
                else:
                    nxt_dp[j] = 1 + min(dp[j], nxt_dp[j+1], dp[j+1])
            dp = nxt_dp
        return dp[0]