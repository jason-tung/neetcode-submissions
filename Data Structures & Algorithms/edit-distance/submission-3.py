class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1), len(word2)
        dp = [0] * (m+1)
        prev = 0
        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                tmp = dp[j]
                if i == n and j == m:
                    continue
                elif i == n:
                    dp[j] = 1 + dp[j+1]
                elif j == m:
                    #  also equal to 1 + tmp
                    dp[j] = 1 + dp[j]
                elif word1[i] == word2[j]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j], prev, dp[j+1])
                prev = tmp
        return dp[0]