class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]
        def sol(i,j):
            if i == m or j == n:
                return 0
            if dp[i][j] == -1:
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + sol(i+1, j + 1)
                else:
                    dp[i][j] = max(sol(i+1, j), sol(i, j+1), sol(i+1,j+1))
            return dp[i][j]
        return sol(0,0)